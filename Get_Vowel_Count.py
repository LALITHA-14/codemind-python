def get_vowel_count(string):
    vowels='aeiou'
    cnt=0
    for i in string:
        if i in vowels:
            cnt+=1
    return cnt

names = [ 'skylerr', 'waaalter', 'jesse', 'siaul']
#              1       4            2        3
# 1 2 3 4
# [ 'skylerr', 'jesse', 'saul', 'walter']
names.sort(key=get_vowel_count,reverse=True) # reversing after sorting
print(names)
names.sort(key=get_vowel_count) # sorting
print(names)
