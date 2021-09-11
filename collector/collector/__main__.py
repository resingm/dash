import json
from datetime import timezone

from collector.api.http import HttpApi
from collector import state, utils

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pyredis import RedisConnection


def main():
    weather = HttpApi(
        "https://api.openweathermap.org/data/2.5/onecall",
        response_type="json",
        appid="6b71c264c9b9614ea166c12ded20c08d",
        lat="52.22086",
        lon="6.89527",
        units="metric",
        exclude="hourly,daily",
        post_proc=utils.post_proc_weather,
    )

    cfg = {}
    with open("./config.json", "r") as f:
        cfg = json.load(f)

    rc = RedisConnection(**cfg["redis"])

    state_mgr = state.StateManager()
    scheduler = BlockingScheduler(
        {
            "apscheduler.executors.default": {
                "class": "apscheduler.executors.pool:ThreadPoolExecutor",
                "max_workers": "5",
            },
            "apscheduler.timezone": "UTC",
        }
    )

    # Weather Enschede - type: card
    args = (
        state_mgr,
        "card",
        "1",
        "Weather Enschede",
        weather.get,
    )
    scheduler.add_job(
        state.update,
        args=args,
        # trigger=IntervalTrigger(seconds=60 * 5),
        trigger=IntervalTrigger(seconds=10),
        id="openweathermap-enschede",
        replace_existing=True,
    )
    #
    # Weather Enschede - type: weather
    args = (
        state_mgr,
        "weather",
        "2",
        "Weather Enschede",
        weather.get,
    )
    scheduler.add_job(
        state.update,
        args=args,
        # trigger=IntervalTrigger(seconds=60 * 5),
        trigger=IntervalTrigger(seconds=10),
        id="openweathermap-enschede-2",
        replace_existing=True,
    )

    args = (state_mgr, rc, "dash")
    scheduler.add_job(
        state.upload,
        args=args,
        trigger=IntervalTrigger(seconds=3),
        id="redis-upload",
        replace_existing=True,
    )

    try:
        scheduler.start()
    except Exception as e:
        # TODO: use logging
        print(e)


if __name__ == "__main__":
    main()
