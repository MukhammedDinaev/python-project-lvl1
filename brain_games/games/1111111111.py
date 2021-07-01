progression_list = [1, 2, 3]
progression_list = str(progression_list).strip('[]')
progression_list = ''.join(progression_list)
progression_list = progression_list.replace(',', '')
print(progression_list)