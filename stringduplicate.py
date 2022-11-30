#set method

def remove_dups(str):
   
    str3 = list(set(str))
    print(str3)
   

sth= "aaabbcc"
remove_dups(sth)

#dictionary method
def remove_dups2(str):
    str2 = list(dict.fromkeys(str))
    print(str2)

sth2= "aaabbccd"
remove_dups2(sth2)