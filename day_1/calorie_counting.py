elvesCaloriesArray = []
maxCalories = 0
total = 0

lines = open('input').read().splitlines()

for line in lines:
    if line != '':
        total += int(line)
    else:
        elvesCaloriesArray.append(total)

        if total > maxCalories:
            maxCalories = total

        total = 0

elvesCaloriesArray.sort(reverse=True)
print(elvesCaloriesArray)

print(sum(elvesCaloriesArray[:3]))
