import sys
from turtledemo.chaos import line


def get_filepath():
    if len(sys.argv) < 2:
        sys.stderr.write("Ошибка, не указан путь к файлу!")
        sys.exit(1)
    else:
        return sys.argv[1]

def main() -> None:
    filepath = get_filepath()
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for i,line in enumerate(file):
                if i >= 5:
                    break
                print(line.rstrip("\n"))
    except FileNotFoundError:
        sys.stderr.write(f"Ошибка, файл {filepath} не найден ")
        sys.exit(1)


if __name__ == '__main__':
    main()