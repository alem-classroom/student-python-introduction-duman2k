def reverse_dict(dict):
    # swap keys and values within dict and return dict
    return {value:key for key, value in dict.items()}