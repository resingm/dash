import json

from pyredis import RedisConnection
from sanic import Sanic
from sanic.log import logger
from sanic.response import HTTPResponse

import response

app = Sanic("Dash")


@app.get("/")
async def index(req) -> HTTPResponse:
    logger.info("Requesting /")

    data = None

    try:
        with req.app.ctx.rc as rc:
            data = rc.get("dash")

    except Exception as e:
        # logger.error(f"Query data failed: {str(e)}")
        logger.debug("Details: ", exc_info=e)
        response._500(e=e)

    return response._json(data)


def main(app: Sanic):
    try:
        logger.setLevel("DEBUG")

        logger.info("Loading configuration...")
        cfg = {}
        with open("./config.json", "r") as f:
            cfg = json.load(f)

        logger.info("Configuration loaded successfully.")
        logger.debug(f"{str(cfg)}")

        # setup redis connection
        logger.info("Configuring Redis...")
        redis_args = {}
        redis_cfg = cfg.get("redis", {})

        if redis_cfg.get("host"):
            redis_args["host"] = redis_cfg["host"]
        if redis_cfg.get("port"):
            redis_args["port"] = redis_cfg["port"]
        if redis_cfg.get("username"):
            redis_args["username"] = redis_cfg["username"]
        if redis_cfg.get("password"):
            redis_args["password"] = redis_cfg["password"]

        app.ctx.rc = RedisConnection(**redis_args)

        with app.ctx.rc as rc:
            logger.debug("Pinging Redis instance...")
            rc.set("PING", "PONG")
            logger.debug(f"Redis PING response: {rc.get('PING')}")
            logger.debug("Connection to Redis established.")

        logger.info("Redis configured successfully.")

        logger.info("Starting REST service...")

        debug = cfg.get("debug", False)
        access_log = cfg.get("access_log", True)

        logger.debug("REST configuration parameters:")
        logger.debug(f"\tDebug:      {debug}")
        logger.debug(f"\tAccess Log: {access_log}")

        app.run(debug=debug, access_log=access_log)

        logger.info("REST service started.")
    except Exception as e:
        # logger.critical(f"Unknown error occured: {str(e)}")
        logger.debug("Details: ", exc_info=e)


if __name__ == "__main__":
    main(app)
