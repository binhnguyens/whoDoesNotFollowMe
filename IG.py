# Imports
import os
import json

# Check Path
cwd = os.getcwd()
print (cwd)

# Path
path = '/Users/binhnguyen/Downloads/connections/followers_and_following/'
f1 = 'followers_1.json'
f2 = 'following.json'

def load_file (path, ff, boolean):
    f = open (path + ff)
    parse = json.load (f)
    
    if (boolean == 1):    
        followers = []
        for i in parse: 
            followers.append(i['string_list_data'][0]['value'])
        return (followers)

    else:
        following = []
        for i in parse['relationships_following']:
            following.append(i['title'])
        return (following)

followers = load_file (path,f1,1)
following = load_file (path,f2,0)

# Compare following and follower: The person I am following is not in my followers
set = []
for i in following:
    if (i not in followers):
        set.append(i)

[print (i) for i in set]
