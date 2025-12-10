with open("input.txt", 'r') as f:
    lines = f.readlines()

pos = 50
times_at_0 = 0

numbers = range(100)

for i in lines:
    assert i[0] in {"L", "R"}

    direction = -1 if i[0] == "L" else 1

    pos += direction * int(i[1:])

    if numbers[pos % 100] == 0:
        times_at_0 += 1


print(f"Part 1 output:\t{times_at_0}")

