# ############## Problem  1 #################### 
# #Ask first friend the movies they like. Save it in a list
# #Ask another friend the same question. If the movie is in the first friend's list, 
# #Print "You both like "name of the movie"
# #Continue until they is atleast 3 movies they both like

# #init variables
# movies = input("What movies you like ? ):
# #convert movies into a List
# #FillinMissingCode

# commonMoviewCount = 0
# while (True) :
#     #ask the second friend for one movie at a time
#     movie = input ( )#FillinMissingCode)
#     #Check if this movie is in the movie list
#     #FillinMissingCode

#     #if present, 
#     commonMoviewCount ++
#     #check if we reached the max
#     if(commmonMovieCount >= 3):
#         break;
#     else
#         print ("Try again")

# print () #FillinMissingCode - list all the common movies

commonMovieCountList = []
commonMovieCount = 0
movies = input("What movies you like ? ")
first_frnd_movies_list = movies.split(",")
print(first_frnd_movies_list)
while (True) :
        movie = input("What movies you like ? ")
        if movie in first_frnd_movies_list:
            commonMovieCountList.append(movie)
            commonMovieCount = commonMovieCount+1
            print(f"You both like {movie}")
            print(commonMovieCount)
            if commonMovieCount >= 3 :
                break
            else:
                print ("Try again")
print(commonMovieCountList)


               

