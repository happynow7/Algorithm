def solution(s, skip, index):
    answer = []
    alphabet = set('abcdefghijklmnopqrstuvwxyz') - set(skip)
    ordered_alphabet = ''.join(sorted(alphabet))
    alphabet_len = len(ordered_alphabet)
    
    for char in s:
        current_index = ordered_alphabet.index(char)
        new_index = (current_index + index) % alphabet_len
        answer.append(ordered_alphabet[new_index])
    
    return ''.join(answer)

def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    valid_chars = [c for c in alphabet if c not in skip]
    char_to_index = {c: i for i, c in enumerate(valid_chars)}
    len_valid = len(valid_chars)
    
    return ''.join(valid_chars[(char_to_index[c] + index) % len_valid] for c in s)


def solution(s, skip, index):
    alphabet = ''.join(chr(i) for i in range(97, 123) if chr(i) not in skip)
    return ''.join(alphabet[(alphabet.index(c) + index) % len(alphabet)] for c in s)

