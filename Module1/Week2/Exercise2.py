def split_tex(text):
    sub_text =  list(set(text))
    return sub_text
def count_tex(text, sub_text):
    count_list = []
    for i in sub_text:
        count_list.append(text.count(i))
    return count_list

def exercise2(str):
    text = list(str)
    list_character = split_tex(text)
    list_count = count_tex(text, list_character)
    result = dict(zip(list_character, list_count))
    return result
print(exercise2("kkkaaa"))    