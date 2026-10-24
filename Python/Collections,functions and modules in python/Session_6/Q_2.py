usernames = ["rahul", "amit", "priya"]
followers = [1200, 2500, 5000]

result = {}

for i in range(len(usernames)):
    result[usernames[i]] = followers[i]

print(result)