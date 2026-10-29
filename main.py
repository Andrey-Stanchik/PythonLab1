import sys

def get_filepath():
    if len(sys.argv) < 2:
        sys.stderr.write("Ошибка, не указан путь к файлу!")
        sys.exit(1)
    else:
        return sys.argv[1]

def main() -> None:
    filepath = get_filepath()

if __name__ == '__main__':
    main()