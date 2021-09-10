import requests


class HttpApi:
    def __init__(
        self,
        base_url: str,
        response_type: str = "json",
        username: str = None,
        password: str = None,
        post_proc: callable = None,
        **kwargs,
    ):
        self._base_url = base_url
        self._params = kwargs
        self._username = username
        self._password = password

        assert response_type in ["json", "raw", "text"]

        self._type = response_type
        self._post_proc = post_proc

    def get(self):
        r = None

        if self._username and self._password:
            r = requests.get(
                self._base_url,
                params=self._params,
                auth=(self._username, self._password),
            )
        else:
            r = requests.get(
                self._base_url,
                params=self._params,
            )

        if r is None:
            return None

        val = ""

        if self._type == "json":
            val = r.json()
        elif self._type == "raw":
            val = r.raw.read()
        elif self._type == "text":
            val = r.text

        if self._post_proc is not None:
            val = self._post_proc(val)

        return val
