import os

# Get username from git config
username = os.popen("git config -l | grep user.name=").read()
# Slice out user.name= and the ending newline
username = username[10:-1]

print(f"Greetings git user {username}!")
