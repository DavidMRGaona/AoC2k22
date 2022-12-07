import re
import numpy as np

lines = [l.strip() for l in open('input').readlines()]

files = {}
current = ''
i = 0

while i < len(lines):

    if lines[i] == '$ cd ..':
        current = current[:current.rfind('/')]
    elif lines[i][:4] == '$ cd':
        current = current + '/' + lines[i][5:]
        if current not in files.keys():
            files[current] = []

    elif lines[i][:4] == '$ ls':
        pass

    elif lines[i][:3] == 'dir':
        files[current].append(current + '/' + lines[i][4:])

    else:
        files[current].append(int(re.findall('[0-9]+', lines[i])[0]))
    i += 1

toRemove = []
i = 0

for folder in files:
    for item in files[folder]:
        if isinstance(item, str):
            toRemove.append(item)
            for n in files[item]:
                files[folder].append(n)
    for l in toRemove:
        files[folder].remove(l)
    toRemove = []
    i += 1

score = 0
needed = 30000000 - (70000000 - np.array(files['//']).sum())
prev = np.inf

for key in files:
    arrays = np.array(files[key]).sum()
    if arrays <= 100000:
        score += arrays
    if (arrays >= needed) & (arrays < prev):
        prev = arrays

print(score)
print(prev)
