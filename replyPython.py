
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# reddit.login("DeepThought_101010", "ZarkingNo")

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        # stores the list of unique post ids in the list posts_replied_to
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        # removes the null values from the list
        posts_replied_to = list(filter(None, posts_replied_to))


# Get the top (hot) 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')

for submission in subreddit.hot(limit=15):
    #print(submission.title)

    # If we haven't replied to this post before, submission.id gets the unique id of that submission
    if submission.id not in posts_replied_to:

        # Do a case insensitive search (that is upper/lower case is considered the same)
        # re that is regular expressions is used here
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Hal 9000 says: You are correct. Python happens to be agreeable.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)


# The reason why a file is maintained, since just storing the ids in a list is not enough, since if the
# program is run again the list would be reset to empty.
# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
