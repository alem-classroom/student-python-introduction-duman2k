def reverse_dict(dict):
    # swap keys and values within dict and return dict
    keys = list(dict.keys())
    values = list(dict.values())
    i = 0
    for item in values:
        dict[item] = keys[i]
        dict.pop(keys[i])
        i += 1
    return dict