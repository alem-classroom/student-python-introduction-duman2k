def clear_dict(dict):
    # delete everything in dict and return it
    dict.clear()
    return dict

def get_dict_items(dict):
    # return keys and values of dict
    return dict.items()

def get_dict_keys(dict):
    # return keys of dict
    return dict.keys()

def get_dict_value_by_key(dict, key):
    # return values of dict that is stored in key
    return dict.get(key)

def delete_dict_element_by_key(dict, key):
    # delete and return element from dict, such that its key is the argument key
    
    if key in dict:
        return dict.pop(key)
        
    #0
    #if key in dict:
    #    dict.pop(key)
    #    return dict
    

    #1
    #dict.pop(key)
    #return dict

    #2
    #if key in dict:
    #    return dict.pop(key)
    #return dict
    #3
    #if key in dict:
    #    return dict.pop(key)
    #4
    #return dict.pop(key)
    #5
    #if key in dict:
    #    dict.pop(key)
    #return dict
    #6
    #if key in dict:
    #    dict.pop(key)
    #    return dict
    #return