import string

letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority_letters_dictionary = {
    letters_list[i]: range(1, 53)[i] for i in range(len(letters_list))
}
lines = open('input').readlines()

priority_sum = sum([
    priority_letters_dictionary[''.join(set(i[:int(len(i) / 2)]).intersection(i[int(len(i) / 2):]))] for i in
    [line.strip() for line in lines]
])
second_priority_sum = sum([
    priority_letters_dictionary[''.join(set(i[0]) & set(i[1]) & set(i[2]))] for i in
    [[line.strip() for line in lines][x:x + 3] for x in range(0, len([line.strip() for line in lines]), 3)]
])

print(priority_sum)
print(second_priority_sum)
