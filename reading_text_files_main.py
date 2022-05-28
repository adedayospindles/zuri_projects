# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")
    data = file.read()
    # print (data)
    # return "Hello World"

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here

    #create empty dictionary
    dict_words = dict()

    #Loop through each line of the file
    for line in text:
        stripped_text = line.strip()
        #Convert to lowercase
        text_to_lower = stripped_text.lower()
        #Split into words
        words = text_to_lower.split(" ")
        #Iteration 
        for word in words:
            #Check word in the dictionary
            if word in dict_words:
                dict_words[word] += 1
                #dict_words[word] = dict_words[word] + 1
            else:
                #Add word to dictionary
                dict_words[word] = 1

    #Print Contents in the dictionary
    for key in list(dict_words.keys()):
        print(key, ":", dict_words[key])
        #return {"as": 10, "would": 20}
