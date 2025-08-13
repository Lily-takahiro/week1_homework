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

    # 温度データを抽出
    temperatures = [entry["temperature"] for entry in weather_information]

    # 平均温度を計算
    average_temperature = sum(temperatures) / len(temperatures)
    
    # 結果を表示
    print(f"全国の平均温度を計算すると: {average_temperature:.1f}℃です")


# Q1. 全国の平均気温を計算してください(9.5となればOK)
    osaka_stations = [info["station"] for info in weather_information if info["prefecture"] == "大阪府"]
    print(f"大阪府のすべての駅名をカンマ区切りで出力してください {",".join(osaka_stations)}")


# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    fukuoka_temperatures = [info["temperature"] for info in weather_information if info["prefecture"] == "福岡県"]
    print(f"福岡県の平均気温を計算してください {(sum(fukuoka_temperatures) / len(fukuoka_temperatures))}")


# Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == "__main__":
    main()
