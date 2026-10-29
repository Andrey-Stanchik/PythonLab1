import sys
import math

def get_filepath() -> str:
    if len(sys.argv) < 2:
        sys.stderr.write("Ошибка, не указан путь к файлу!")
        sys.exit(1)
    else:
        return sys.argv[1]

def collect_stats(file_object) -> dict:
    stats = {}

    for line in file_object:
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue

        station, temperature_str = line.split(";",1)
        temperature = float(temperature_str)

        if station in stats:
            data = stats[station]

            if data[0] > temperature:
                data[0] = temperature
            if data[2] < temperature:
                data[2] = temperature

            data[1] += temperature
            data[3] += 1
        else:
            stats[station] = [temperature, temperature,temperature, 1]

    return stats

def round_value(value: float) -> float:
    return math.floor(value * 10.0 + 0.5) / 10.0

def print_sort_stats(stats: dict) -> None:
    for station in sorted(stats.keys()):
        min_temperature,sum_temperature, max_temperature, count = stats[station]
        mean_temperature = round_value(sum_temperature / count)
        print(f"{station};{min_temperature:.1f};{mean_temperature:.1f};{max_temperature:.1f}")

def main() -> None:
    filepath = get_filepath()
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            stats = collect_stats(file)
        print_sort_stats(stats)
    except FileNotFoundError:
        sys.stderr.write(f"Ошибка, файл {filepath} не найден ")
        sys.exit(1)


if __name__ == '__main__':
    main()