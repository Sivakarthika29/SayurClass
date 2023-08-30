"""Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov" 
Note: how you replace each * in the pattern with the letter in the message, the space in the message doesn't
matter, but the space(s) in the pattern matters."""
import re
message=input("Enter the message:")
pattern=input("Enter the pattern:")

