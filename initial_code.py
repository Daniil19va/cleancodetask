cost = input("Скільки коштують квитки A: ").split()
cost_2 = input("Скільки коштують квитки B: ").split()
cost_3 = input("Скільки коштують квитки C: ").split()


def first_func() -> tuple:
    sold = input("Скільки продано квитків A: ").split()
    sold_2 = input("Скільки продано квитків B: ").split()
    sold_3 = input("Скільки продано квитків C: ").split()

    return sold
    return sold_2
    return sold_3


def second_func() -> None:
    sold = first_func()

    i = 0
    j = 0
    k = 0

    tickets = ["A"]
    tickets_j = ["B"]
    tickets_k = ["C"]

    for num in sold:
        print(f"З продажу квитків {tickets[i]} отримано {int(num) * int(cost[i])}")
        print(f"З продажу квитків {tickets_j[j]} отримано {int(num) * int(cost_2[i])}")
        print(f"З продажу квитків {tickets_k[k]} отримано {int(num) * int(cost_3[i])}")

        i += 1
        j += 1
        k += 1

    i = 0
    j = 0
    k = 0

    all = 0

    for nume in sold:
        all += int(nume) * int(cost[i])
        all += int(nume) * int(cost_2[i])
        all += int(nume) * int(cost_3[i])

        i += 1
        j += 1
        k += 1

    print(f"Весь виторг: {all}")


second_func()
