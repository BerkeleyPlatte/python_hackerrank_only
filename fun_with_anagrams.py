# removes words that are anagrams of the original word and
# returns a sorted list of the original words

string = ['poke', 'kope', 'opke', 'eopk']

string2 = ['code', 'ecod', 'doce', 'framer', 'frame']

string3 = ['code', 'ecod', 'anagrams', 'aanmgrsa']

def fun_with_anagrams(text):
    for i in range(len(text)):
        try:
            j = 1
            # you always want to start with looking at
            # the second index in the list
            if i >= j:
                # this ensures that program is never having a word
                # look at itself, and allows me to check a word
                # against every word in the list before moving
                # on
                j = i + 1
            while j < len(text):
                if sorted(text[i]) == sorted(text[j]):
                    text.remove(text[j])
                    # you don't want to iterate if a word is 
                    # removed, since the next word to be 
                    # checked will just slide down to take
                    # its place
                else:
                    j += 1
        except IndexError:
            break
    return sorted(text)

print(fun_with_anagrams(string3))