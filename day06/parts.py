import numpy as np


with open("./input.txt", 'r') as f:
    lines = f.readlines()

lines_copy = lines.copy()

lines = [i.strip() for i in lines]

actions = [i for i in lines.pop().split(" ") if i != ""]
problems: list[list[int]] = []

for line in lines:
    problems.append([
        int(i)
        for i in line.split(" ")
        if i != ""
    ])

total: int = 0
total_max: int = 0
problems_np = np.array(problems, dtype = np.uint64)
actions_np = np.array(
    tuple(
        bool(i.replace("+",""))
        for i in actions
    ),
    dtype = np.bool
)

for idx, act in enumerate(actions_np):
    column = problems_np[:, idx]

    if act: 
        # multiply
        total += column.prod()
    else:
        # add
        total += column.sum()

print(f"Part 1 output:\t{total}")

# Part 2

total = 0

char_lines: list[list[str]] = [
    [i for i in j]
    for j in lines_copy
]

char_lines_np = np.array(char_lines).T[:-1]
problems_np = char_lines_np[:,:-1]
actions_np = char_lines_np[:,-1]

problems_np = np.array(
    list(
        map(
            lambda row: [
                # -1 is our "null"
                int(i) if i != " " else -1 for i in row
            ],
            problems_np
        )
    )
)

for idx, (prob, act) in enumerate(zip(problems_np, actions_np)):
    if act in ("+", "*"):
        end_idx = idx
        temp_total = 0

        while actions_np[end_idx + 1] == " ":
            end_idx += 1
            if end_idx >= actions_np.shape[0] - 1:
                end_idx = -1
                break

        if end_idx == -1:
            subsection = problems_np[idx:]
        else:
            subsection = problems_np[idx:end_idx]

        if act == "+":
            for row in subsection:
                temp_total += int(
                    "".join(
                        str(i) for i in row[row > -1]
                    )
                )

        elif act == "*":
            temp_total = 1
            for row in subsection:
                temp_total *= int(
                    "".join(
                        str(i) for i in row[row > -1]
                    )
                )
        
        total += temp_total
    
    else:
        continue

print(f"Part 2 output:\t{total}")
