"""Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov" 
Note: how you replace each * in the pattern with the letter in the message, the space in the message doesn't
matter, but the space(s) in the pattern matters."""

message=input("Enter the message:")
pattern=input("Enter the pattern:")

message = message.replace(" ","")
result = ""
k=0
for i in pattern:
      if i == " ":
            result = result + " "
      else:
            result = result + message[k]
            k = k+1
      if k >= len(message):
            k=0
print(result)


# OUTPUT:

# Enter the message:I Love India
# Enter the pattern:*** **** ** **********     *****
# ILo veIn di aILoveIndi     aILov


