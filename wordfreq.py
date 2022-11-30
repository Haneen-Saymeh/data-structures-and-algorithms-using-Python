# Given a list(array) containing different words, define a function count_words that returns each word and the 
# frequency(how many times) they appear in the list.

# # Example List
# test_list = ["the", "name","of", "the", "rose", "the","english", "patient", "the","greatest", "person", "in", "the", "world", "test", "the", "person","hello"]

def count_freq(list):
    dict= {}
    for item in list:
        if item not in dict:
            dict[item] =1
        else:
            dict[item] = dict[item]+1
    
    for key,value in dict.items():
        print(key,value)

test_list = ["the", "name","of", "the", "rose", "the","english", "patient", "the","greatest", "person", "in", "the", "world", "test", "the", "person","hello"]
count_freq(test_list)


