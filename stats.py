def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict

def sort_dict(character_dict):
    dict_list = []
    new = {}
    for key, value in character_dict.items():
        new['char'] = key
        new['num'] = value
        dict_list.append(new.copy())
    
    def sort_key(item):
        return item['num']
    
    dict_list.sort(key=sort_key, reverse=True)
    
    return dict_list


