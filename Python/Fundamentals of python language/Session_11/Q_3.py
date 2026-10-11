def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers / 1000:.1f}K followers")


friends = {
    "priya": 2300,
    "rahul": 5400,
    "amit": 1800
}

display_friends(friends)