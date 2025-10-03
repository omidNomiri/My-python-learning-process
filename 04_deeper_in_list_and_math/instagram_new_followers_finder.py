import instaloader
import getpass

instagram_account = instaloader.Instaloader()

username = input("Please enter your user name: ")
password = getpass.getpass("Please enter your password: ")

instagram_account.login(username, password)
print("You successfully login!")

profile = instaloader.Profile.from_username(instagram_account, username)

with ("followers.txt", "r") as unfollowers_file:
    for unfollowers in unfollowers_file:
        if unfollowers not in unfollowers_file:
            print(unfollowers)

new_follwers = []
for follower in profile.get_followers():
    new_follwers.append(follower)

new_followers = set(new_follwers) - set(follower) 

with ("followers.txt", "w") as text_log:
    for follower in new_follwers:
        text_log.write(follower+ "\n")
