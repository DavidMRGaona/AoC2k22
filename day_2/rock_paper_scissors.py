lines = open('input', 'r').read().splitlines()

score_dictionary = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

second_score_dictionary = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

int_list = []
second_int_list = []

for item in lines:
    int_list.append(score_dictionary[item])
    second_int_list.append(second_score_dictionary[item])

total_score = sum(int_list)
second_total_score = sum(second_int_list)

print(total_score)
print(second_total_score)
