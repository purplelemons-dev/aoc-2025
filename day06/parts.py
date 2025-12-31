import numpy as np


with open("./input.txt", 'r') as f:
    lines = [i.strip() for i in f.readlines()]

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

