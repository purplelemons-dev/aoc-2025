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

