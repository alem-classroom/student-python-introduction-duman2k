def reverse_dict(dict):
    # swap keys and values within dict and return dict
    for key in list(dict.keys()):
        dict[dict[key]] = key
        dict.pop(key)
        
    return dict