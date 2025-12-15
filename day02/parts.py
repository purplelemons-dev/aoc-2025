with open("./input.txt", 'r') as f:
    lines = f.readlines()

line = lines[0].strip("\n")
ranges = line.split(',')

# Part 1
invalid_IDs: list[int] = []

for i in ranges:
    start, stop = map(int, i.split('-'))
    
    for j in range(start, stop + 1):
        number = str(j)
        length = len(number)

        # Skip odd length
        if not length % 2:
            halfway = length // 2
            if number[halfway:] == number[:halfway]:
                invalid_IDs.append(j)

print(f"Part 1 output:\t{sum(invalid_IDs)}")

# Part 2
invalid_IDs = []

for i in ranges:
    start, stop = map(int, i.split('-'))
    
    for j in range(start, stop + 1):
        number = str(j)
        length = len(number)
        halfway = round(length/2)

        for k in range(1, halfway + 1):
            subsection = number[:k]
            if number == (subsection * (length // k)):
                invalid_IDs.append(j)
                break

print(f"Part 2 output:\t{sum(invalid_IDs)}")

