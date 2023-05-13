cost = input("Скільки коштують квитки A B и C введіть через пробіл: ").split()


def first_func() -> tuple:
    sold = input("Скільки продано квитків A B и C введіть через пробіл: ").split()

    return sold


def second_func() -> None:
    sold = first_func()

    i = 0

    tickets = ["A", "B", "C"]

    for num in sold:
        print(f"З продажу квітків {tickets[i]} отримано {int(num) * int(cost[i])}")

        i += 1

    i = 0

    all = 0

    for nume in sold:
        all += int(nume) * int(cost[i])

        i += 1

    print(f"Весь виторг: {all}")


second_func()
