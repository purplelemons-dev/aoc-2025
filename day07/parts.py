with open("./input.txt", 'r') as f:
    lines = f.readlines()

current_beam: list[int] = [
    lines.pop(0).index("S")
]

def indexes(char: str, string: str):
    for idx, c in enumerate(string):
        if c == char:
            yield idx

total = 0

for row in lines:
    for split_idx in indexes("^", row):
        if split_idx in current_beam:
            total += 1

            for offset in (1, -1):
                offset += split_idx
                if offset not in current_beam:
                    current_beam.append(offset)

            current_beam.remove(split_idx)

print(f"Part 1 output:\t{total}")

