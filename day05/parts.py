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
    if any(int(i) in rng for rng in parsed_ranges):
        total += 1

print(f"Part 1 output:\t{total}")

