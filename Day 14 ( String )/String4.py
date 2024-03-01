########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

# inputSentence = #FillinMissingCode
# pigLatinKey = 'ay'
# vowels = ['a','e','i','o','u']

# for word in inputSentence.split(): #gets the word in a sentence
#     #take the first chars until a vowel
#     first_vowel_index = 0
#     #FillinMissingCode - check if the word has more than one char
#     for index, char in enumerate(word): #returns both the index and the char in the word
#          #FillinMissingCode - check if the char is vowel or not
        
#     word = #FillinMissingCode  
#     print( #FillinMissingCode)
        

inputSentence = input("Enter the Sentence : ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
consonants = ""
for word in inputSentence.split(): 
     first_vowel_index = 0
    
     for index, char in enumerate(word): 
          if char in vowels:       #check if the char is vowel or not
               consonants += char
               first_vowel_index = index
               break
          else:
               consonants += char
     print(word[first_vowel_index+1:] + consonants + pigLatinKey ,end=" ")
     consonants = ""

# OUTPUT:

# Enter the Sentence : I am Python
# Iay maay nPythoay
     