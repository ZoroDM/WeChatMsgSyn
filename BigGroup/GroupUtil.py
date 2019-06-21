
def get_groups_name(groups):
    result = []
    for group in groups:
        result.append(group.name)
    return "，".join(result)
