with open("input.txt", 'r') as f:
    lines = [
        i.strip() for i in f.readlines()
    ]

banks: list[int] = []
numbers = tuple(
    str(i) for i in range(9, 0, -1)
)

for bank in lines:
    for number in numbers:
        split = bank.split(number)

        if (split[-1] == "" and len(split) == 2) or (len(split) == 1):
            # case that largest number is last or is not found
            continue
        else:
            banks.append(
                max(
                    int(f"{number}{char}")
                    for char in number.join(
                        split[1:]
                    )
                )
            )
            break

print(f"Part 1 output:\t{sum(banks)}")

# Part 2

def get_joltage(input: str, counter: int, current: int = 0) -> int | None:
    if len(input) < counter:
        return None

    elif counter == 1:
        return max(
            current * 10 + int(i)
            for i in input
        )

    else:
        for num in numbers:
            idx = input.find(num)

            if idx >= 0:
                next_joltage = get_joltage(
                    input[idx + 1:],
                    counter - 1,
                    current * 10 + int(num)
                )

                if next_joltage == None:
                    continue

                else:
                    return next_joltage

            else:
                continue


part_2_banks: list[int] = []

for bank in lines:
    joltage = get_joltage(bank, 12)

    if joltage != None:
        part_2_banks.append(joltage)

print(f"Part 2 output:\t{sum(part_2_banks)}")

