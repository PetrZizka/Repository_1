import string
from sys import exit
from collections import Counter
import matplotlib.pyplot as plt

def Text_processing():
     presence_of_words = {}
     for word in clean_words:
         if word not in  presence_of_words:
             presence_of_words[word] = 1
         else:
            presence_of_words[word] += 1
            
            presence_of_words = {word : clean_words.count(word) for word in clean_words}
            print("There are", len(clean_words), " words in the selected text.")
            title_case_word = {word : clean_words.count(word) for word in clean_words if word.istitle()}
            print("There are", len(title_case_word), "titlecase words in the selected text.")
            upper_case_word = {word : clean_words.count(word) for word in clean_words if word.isupper()}
            print("There are", len(upper_case_word), "uppercase words in the selected text.")
            lower_case_word = {word : clean_words.count(word) for word in clean_words if word.islower()}
            print("There are", len(lower_case_word), "lowercase words in the selected text.")
            numeric_string = {word : clean_words.count(word) for word in clean_words if word.isnumeric()}
            print("There are", len(numeric_string), " numeric strings in the selected text.")
            sum_of_numbers = [int(word) for word in numeric_string]
            print("The sum of all the numbers", sum(sum_of_numbers))
            sorted_list = sorted(clean_words, key=len)
            word_and_len = {word: len(word) for word in sorted_list}
            occurences = Counter(word_and_len.values())
            plt.bar(occurences.keys(), occurences.values())
            plt.title("frequency of different word lengths in text")
            plt.xlabel("word length")
            plt.ylabel("word frequency")
            plt.show()
            break

users = dict({"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"})

username = input ("Your Username: ")
password = input("Password:")

if users.get(username) == password:
    print("access granted.", "Hi,", username.title(), "Welcome to our application" )
    
else :
    print("incorrect password or Username")
    exit(0)
    
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
text_number = int(input("We have 3 texts to be analyzed\n Enter a number btw. 1 and 3 to select:"))

if (text_number) == 1:
    clean_words = [word.strip(string.punctuation) for word in TEXTS[0].split() if len(word) >= 1]
    Text_processing()

elif (text_number) == 2:
     clean_words = [word.strip(string.punctuation) for word in TEXTS[1].split() if len(word) >= 1]
     Text_processing()
elif (text_number) == 3:
     clean_words = [word.strip(string.punctuation) for word in TEXTS[2].split() if len(word) >= 1]
     Text_processing()
