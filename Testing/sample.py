
inputSentence = input("Enter the Sentence : ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
consonants = ""
for word in inputSentence.split(): 
     first_vowel_index = 0
    
     for index, char in enumerate(word): 
          print(index,char)