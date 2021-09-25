import json
from datetime import datetime
from typing import Union
from utils import wrap_component

from pyredis import RedisConnection


class StateManager:
    def __init__(self):
        self._state = {}

    @property
    def state(self):
        # Ensure an order by iterating over keys
        return {
            "data": [self._state[k] for k in self._state.keys()],
        }

    def update(self, key: str, val: Union[str, dict]):
        self._state[key] = val


def update(
    mgr: StateManager,
    card_type: str,
    id: str,
    title: str,
    f: callable,
    subtitle: str = None,
    *args,
    **kwargs,
):
    val = f(*args, **kwargs)
    ts = datetime.utcnow().isoformat(timespec="seconds")
    ts = f"{ts} GMT"
    comp = wrap_component(
        id=id,
        title=title,
        subtitle=subtitle,
        ts=ts,
        card_type=card_type,
        attributes=val,
    )
    mgr.update(id, comp)


def upload(mgr: StateManager, rc: RedisConnection, topic: str):
    try:
        # val = json.dumps(mgr.state)
        rc.set(topic, mgr.state)
    except Exception as e:
        raise e
