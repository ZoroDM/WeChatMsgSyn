
def get_groups_name(groups):
    result = []
    for group in groups:
        print(group.name)
        result.append(group.name)
    return "，".join(result)
