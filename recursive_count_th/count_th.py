'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#traverse string characters
#search for th in string
#if th in string, add to count
#need to count AND keep traversing to end of str
#if not in string, continue traverse
#base-string end
#case for string 0?
#case for string less than 2 letters
#what if string is only "th"?
#return the count of th
def count_th(word):
    
    if len(word) == 0: #if word is 0? (not sure needed)
        return 0

    if len(word) < 2: #if less than 2, cant contain both chars
        return 0

    else:
    
    
    return count_th()
