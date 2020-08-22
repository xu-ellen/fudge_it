import pandas as pd
import numpy as np
import random
import math

df = pd.read_csv("example-response.csv")
print(df)

user = {"0":"Ellen", "1":"Kate", "2":"Boba", "3":"Bob1", "4":"Bob2", "5":"Bob3"} # dynamically do this later so that their usernames correspond to the index
user_key = list(user.keys())
user_val = list(user.values())
print("The users are", user_key)

# any pair of users; outer loop goes through 1-#users, inner loop goes through user[index] to #user
user_table = {}
total = 10 # how many traits there are to compare with; change to connecting

#matrix = np.identity(len(user))
x = []
for i in range(len(user)):
    x.append(-100)
score = np.diag(x)
print(score)

### Match based on traits/personality ###
for i in range(len(user)):
    user_table["user"+str(i)] = df.iloc[i] # get the respective row for each user, store in dict
    #print(i)

    if i > 0:
        for j in range(i):
            score[i,j]= total-1-sum(abs(user_table["user"+str(i)][0:9] - user_table["user"+str(j)][0:9]))
            print("The similarity score between user",str(i)," and user",str(j)," is",str(total-1-sum(abs(user_table["user"+str(i)][0:9] - user_table["user"+str(j)][0:9]))))

print(score)
#print(user_table)

### Match based on personality type ###
# https://www.business2community.com/leadership/key-personality-types-work-well-together-01934388
types = {"0":"ENFJ","1":"INFJ","2":"ENFP","3":"INFP","4":"INTJ","5":"ENTJ","6":"INTP","7":"ENTP","8":"ESFP","9":"ISFP","10":"ESFJ","11":"ISFJ","12":"ISTP","13":"ESTP","14":"ISTJ","15":"ESTJ"}
types_pair = {"14":"13", "6":"4", "3":"1", "5":"12", "9":"8", "7":"0", "11":"3", "10":"15"}

# print(np.max(score))
result = np.where(score == np.amax(score))
print('Tuple of arrays returned : ', result)

print('List of coordinates of maximum value in Numpy array : ')
result_coord = list(zip(result[0], result[1]))
for max_coord in result_coord:
    print(max_coord)

total_pair = math.floor(len(user)/2) # works for odd or even
print("The total number of pairs is ", total_pair)

pair = {}

for i in range(int(total_pair)):
    if len(max_coord) > 1:  # if there is more than one max similarity score
        pair["pair"+str(i)] = random.choice(result_coord)
        print("The", i, "matched pair is ", pair["pair"+str(i)])
        print("The names of the", i, " matched pair is ", user[str(pair["pair"+str(i)][0])], "and", user[str(pair["pair"+str(i)][1])])

        score[pair["pair"+str(i)][0]] = -1
        score[:,pair["pair"+str(i)][0]] = -1
        score[pair["pair"+str(i)][1]] = -1
        score[:,pair["pair"+str(i)][1]] = -1

        result = np.where(score == np.amax(score))
        result_coord = list(zip(result[0], result[1]))
    # else:   # if there is only one max similarity score

print(pair)

print(score)