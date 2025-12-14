with open("input.txt", 'r') as f:
    lines = f.readlines()

# Part 1

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

# Part 2
pos = 50
times_at_0 = 0

"""
for i in lines:
    direction = -1 if i[0] == "L" else 1

    for j in range(int(i[1:])):
        pos += direction
        pos = numbers[pos % 100]
        if pos == 0:
            times_at_0 += 1
"""

# the below code produces the incorrect value by 1 more than the above code
for i in lines:
    direction = -1 if i[0] == "L" else 1

    new_pos = pos + direction * int(i[1:])
    
    if new_pos > 99 or new_pos < 0:
        times_at_0 += abs(new_pos // 100)
        new_pos %= 100
        pos = numbers[new_pos]
    else:
        pos = new_pos
    
    if pos > 99 or pos < 0:
        raise ValueError(f"Pos is out of bounds. {pos=}")

print(f"Part 2 output:\t{times_at_0}")

