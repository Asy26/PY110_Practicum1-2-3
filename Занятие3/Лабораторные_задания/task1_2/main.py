OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:   # TODO записать лесенку в файл
        for asterisk in range(1, 11):
            asterisk = f.write(f"{asterisk * '*':>10}\n")

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
