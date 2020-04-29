# for list a rotate d number of times

def rotLeft(a, d):
    for each in range(d):
        first = a[0]
        # you're basically just taking
        # each element off the beginning
        # of the list and sticking it on
        # the end
        a.remove(first)
        a.append(first)
    return a
    
        
print(rotLeft([1, 2, 3, 4, 5], 4))