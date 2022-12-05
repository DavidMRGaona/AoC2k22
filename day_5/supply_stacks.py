import re


def apply_one_order(dictionary, sequence, reverse):
    cut = dictionary[sequence[1]][-sequence[0]:]

    if reverse:
        cut.reverse()

    dictionary[sequence[2]] = dictionary[sequence[2]] + cut
    dictionary[sequence[1]] = dictionary[sequence[1]][:len(dictionary[sequence[1]]) - sequence[0]]

    return dictionary


lines = [line.replace('    ', 'A ').strip() for line in open('input').readlines()]

br = lines.index('')
boxes = lines[:br - 1]
orders = lines[br + 1:]
col_number = int(re.findall('[0-9]+', lines[br - 1])[-1])
order_list = [[int(i) for i in t] for t in [re.findall('[0-9]+', c) for c in orders]]
box_dict = dict.fromkeys(range(1, col_number + 1), [])

for e in boxes:
    elem = re.findall('[A-Z]+', e)
    for i in range(len(elem)):
        if elem[i] != 'A':
            box_dict[i + 1] = [elem[i]] + box_dict[i + 1]

part_one = box_dict.copy()
part_two = box_dict.copy()

for order in order_list:
    part_one = apply_one_order(part_one, order, 1)
    part_two = apply_one_order(part_two, order, 0)

ans_one = ''
ans_two = ''

for value in part_one.values():
    ans_one += value[-1][0]

for value in part_two.values():
    ans_two += value[-1][0]

print(ans_one)
print(ans_two)
