with open('./input.txt', 'r') as f:
    lines = f.read()

ranges, IDs = lines.split("\n\n")
ranges = tuple(i for i in ranges.split("\n") if i)
IDs = tuple(i for i in IDs.split("\n") if i)

parsed_ranges: set[range] = set()
for i in ranges:
    start, stop = i.split("-")
    start = int(start)
    stop = int(stop)

    parsed_ranges.add(range(start, stop + 1))

total = 0
for i in IDs:
    if any(int(i) in range(rng.start, rng.stop) for rng in parsed_ranges):
        total += 1

print(f"Part 1 output:\t{total}")

# Part 2

newRanges: list[list[int]] = []

sortedRanges: list[tuple[int, int]] = [
    (rng.start, rng.stop)
    for rng in parsed_ranges
]

sortedRanges.sort()

newRanges.append(list(sortedRanges[0]))

for start, stop in sortedRanges[1:]:
    last_range = newRanges[-1]
    prev_rng = range(last_range[0], last_range[1])

    if stop in prev_rng and start in prev_rng:
        continue
    elif last_range[1] >= start:
        newRanges[-1][1] = stop
    elif last_range[1] < start:
        newRanges.append([start, stop])
    else:
        raise RuntimeError(f"Undefined condition for: {prev_rng= } {start= } {stop= }")

total2 = sum(len(range(start, stop)) for start, stop in newRanges)

print(f"Part 2 output:\t{total2}")

