def remove_dup(sth):
    sth2= set(sth)
    return list(sth2)

str= ["a", "a", "r"]
numbs = [1,1,3,4,5,5]
print(remove_dup(str))
print(remove_dup(numbs))