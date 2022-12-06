lines = open('input').readlines()[0]
size = 14

for i in range(3, len(lines)):
    if len(''.join(set(lines[i - size:i]))) == size:
        print(i)
        break
