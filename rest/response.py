import traceback

from sanic.response import empty, json, HTTPResponse


def _wrap(tag: str, payload: dict):
    return {tag: payload}


def _body(status: int, desc: str, msg: str):
    return _wrap(
        "errors",
        {
            "status": status,
            "description": desc,
            "message": msg,
        },
    )


def _debug(e: Exception):
    return _wrap(
        "meta",
        {
            "debug": {
                "message": traceback.format_exc(),
                "cause": "" if e.__cause__ is None else str(e.__cause__),
                "context": "" if e.__context__ is None else str(e.__context__),
                "traceback": traceback.format_tb(e.__traceback__),
            }
        },
    )


def _json(body: dict, wrap: str = None, status: int = 200):
    _body = body if wrap is None else {str(wrap).lower(): body}
    return json(
        _body,
        status=status,
        # dumps=<custom json dump>,
    )


def _204():
    return empty()


def _400(msg: str = None):
    msg = "Request wsa invalid." if msg is None else msg
    body = _body(400, "Bad request", msg)
    return _json(body, status=400)


def _500(msg: str = None, e: Exception = None):
    if msg is None:
        msg = "Uups, that was our fault... We will look into that!"

    body = _body(500, "Internal server error", msg)

    if e is not None:
        body.update(_debug(e))

    return _json(body, status=500)
