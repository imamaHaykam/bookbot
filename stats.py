def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    return {
        't': text.lower().count('t'),
        'p': text.lower().count('p'),
        'c': text.lower().count('c')
    }

def sort_on(items):
    return items["count"]

def character_frequency(text):
    text_lower = text.lower()
    characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'â', 'æ', 'ê', 'ë', 'ô'
    ]
    
    char_list = []
    for char in characters:
        char_list.append({'char': char, 'count': text_lower.count(char)})
    
    # Sort by count in descending order
    char_list.sort(key=lambda x: x['count'], reverse=True)
    return char_list