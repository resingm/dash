from collector.api.http import HttpApi


def main():
    weather = HttpApi(
        "https://api.openweathermap.org/data/2.5/onecall",
        response_type="json",
        appid="6b71c264c9b9614ea166c12ded20c08d",
        lat="52.22086",
        lon="6.89527",
        units="metric",
        exclude="hourly,daily",
    )

    test = weather.get()
    print(test)


if __name__ == "__main__":
    main()
