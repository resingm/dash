def wrap_component(
    id: str,
    title: str,
    subtitle: str = None,
    card_type: str = "card",
    attributes: dict = {},
) -> dict:
    """Wraps data into a component, including meta data, etc.

    :param id: Unique ID to identify the component
    :type id: str
    :param title: Title of the card component
    :type title: str
    :param subtitle: Subtitle of the card, defaults to None
    :type subtitle: str, optional
    :param card_type: Type of the card, defaults to "card"
    :type card_type: str, optional
    :param attributes: Set of attributes, defaults to {}
    :type attributes: dict, optional
    :return: Prepared dictionary, wrapped as a dictionary
    :rtype: dict
    """
    meta = {}
    meta["title"] = title

    if subtitle:
        meta["subtitle"] = subtitle

    return {
        "type": card_type,
        "id": id,
        "attributes": attributes,
        "meta": meta,
    }


def post_proc_weather(data: dict) -> dict:
    """Postprocesses API responses from openweathermap.org.

    :param data: Raw JSON data parsed as dictionary
    :type data: dict
    :return: Postprocessed weather data with relevant information
    :rtype: dict
    """
    params = {
        "lat": "latitude",
        "lon": "longitude",
        "current.temp": "temperature",
        "current.feels_like": "temperate_feeling",
        "current.clouds": "clouds",
        "current.wind_speed": "wind",
    }

    result = {}

    for key, val in params.items():
        ks = key.split(".")

        v = data
        while len(ks):
            v = v[ks.pop(0)]

        if v is not None:
            result[val] = v

    return result
