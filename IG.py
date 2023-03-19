# Imports
import os
import json

# Check Path
cwd = os.getcwd()
print (cwd)

# Path
path = '/Users/binhnguyen/Desktop/'
f1 = 'followers_1.json'
f2 = 'following.json'

def load_file (path, ff, followers):
    f = open (path + ff)
    parse = json.load (f)

    # Loop through to load files into follwering
    if (followers == 1):    
    # Number of follwers/following
        n = len (parse)
        followering = ['']*n

        for i in range (n):
            followering [i] = parse [i]['string_list_data'][0]['value']
    else:
        # Number of follwers/following
        n = len (parse['relationships_following'])
        followering = ['']*n
        
        for i in range (n):
            followering [i] = parse ['relationships_following'][i]['string_list_data'][0]['value']

    return (followering)

followers = load_file (path,f1,1)
following = load_file (path,f2,0)

# Compare following and followers
# Condition: the person I am following is not in my followers [They do not follow me back]
set = []
for i in following:
    if (i not in followers):
        set.append(i)

[print (i) for i in set]
