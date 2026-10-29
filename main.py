import sys


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


def main() -> None:
    filepath = get_filepath()
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            stats = collect_stats(file)
            for station in list(stats.keys())[:3]:
                print(station, stats[station])
    except FileNotFoundError:
        sys.stderr.write(f"Ошибка, файл {filepath} не найден ")
        sys.exit(1)


if __name__ == '__main__':
    main()