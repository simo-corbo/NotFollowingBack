# Small Python script to see who doesn't follow you back on instagram
import json

if __name__ == '__main__':
    # Opening JSON file
    followerFile = open('followers_1.json')
    followingFile =open('following.json')
    # returns JSON object as
    # a dictionary
    dataFollower = json.load(followerFile)
    dataFollowing = json.load(followingFile)
    # Iterating through the json
    followers = []
    followings =[]

    for i in dataFollower:
        followers.append(i['string_list_data'][0]['value'])
    for i in dataFollowing['relationships_following']:
        followings.append(i['string_list_data'][0]['value'])

    print("Follower: ", len(followers))
    print("Following: ", len(followings))
    followerFile.close()
    followingFile.close()
    followers.sort()
    followings.sort()
    print("Not following me back: ")
    for following in followings:
        if following not in followers:
            print(following)
    print("\n -------------------\n")
    print("I don't follow back: ")
    for follower in followers:
        if follower not in followings:
            print(follower)