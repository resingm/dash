import requests


class HttpApi:
    def __init__(
        self,
        base_url: str,
        response_type: str = "json",
        username: str = None,
        password: str = None,
        **kwargs,
    ):
        self._base_url = base_url
        self._params = kwargs
        self._username = username
        self._password = password

        assert response_type in ["json", "raw", "text"]

        self._type = response_type

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

        if self._type == "json":
            return r.json()
        elif self._type == "raw":
            return r.raw.read()
        elif self._type == "text":
            return r.text
