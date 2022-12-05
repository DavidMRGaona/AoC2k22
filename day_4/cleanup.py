import re

lines = open('input').readlines()

total_overlap = sum([
    ((j[0] >= j[2]) & (j[1] <= j[3])) | ((j[2] >= j[0]) & (j[3] <= j[1])) for j in
    [[int(i) for i in k] for k in [re.findall('[0-9]+', c) for c in [line.strip() for line in lines]]]
])
partial_overlap = sum([
    not ((j[1] < j[2]) | (j[3] < j[0])) for j in
    [[int(i) for i in k] for k in [re.findall('[0-9]+', c) for c in [line.strip() for line in lines]]]
])

print(total_overlap)
print(partial_overlap)
