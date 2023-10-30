def find_common_participants(participants_first_group, participants_second_group, \
separator=','):
    group1 = set(participants_first_group.split(separator))
    group2 = set(participants_second_group.split(separator))
    common_participants = sorted(list(group1.intersection(group2)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group,\
participants_second_group, separator='|')

print("Общие участники:", common_participants)