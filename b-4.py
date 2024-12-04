def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    values = [weather["temperature"] for weather in weather_information]
    if not values:
        return None
    result_1 = sum(values) / len(values) if values else None

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    osaka_stations = [
        weather["station"] for weather in weather_information if weather.get("prefecture") == "大阪府"
    ]
    if not osaka_stations:
        return None
    result_2 = (",").join(osaka_stations) if osaka_stations else None

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    hukuoka_temperatures = [
        float(weather["temperature"])
        for weather in weather_information
        if weather.get("prefecture") == "福岡県"
    ]
    if not hukuoka_temperatures:
        return None
    result_3 = sum(hukuoka_temperatures) / len(hukuoka_temperatures) if hukuoka_temperatures else None

    return result_1, result_2, result_3


if __name__ == "__main__":
    print(main())
