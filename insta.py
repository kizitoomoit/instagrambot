from instapy import InstaPy
import getpass
from time import sleep

session = InstaPy(username=input('username: '), password=getpass.getpass('password: '))

#if you want to use headless browsing and you want to enter your password and username once enable the code below and disable the one above
#session = InstaPy(username="your username ", password="your password", headless_browser=True)
session.login()

sleep(20)

#It is used to like posts with tags below you have to edit that to fit your situtation
session.like_by_tags(["kimkardashian", "fashion"], amount=5)

#It is used to avoid liking posts with tags you don't like edit to suit your situation
session.set_dont_like(["naked", "nsfw"])i

#following
session.set_do_follow(enabled=True, percentage=10, times=2)

#this will follow each account from a list of instagram nicknames
follow_by_list(followlist=['name', 'name1'], times=1, sleep_delay=600, interact=False)

#follow user based on hashtags (without liking the image)
session.follow_by_tags(['tag1', 'tag2'], amount=10)

#this will follow the poeple those liked photos of given list of users
session.follow_likers(['user1', 'user2'], photos_grab_amount = 1, follow_likers_per_photo, randomize=True, sleep_delay=600, interact=False

#follow people those commented on photos of given list of users
session.follow_commenters(['user1', 'user2', 'user3'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)

#unfollow the users who do not follow you back
session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, slee-_delay=655)


#This will be your custom comments whenever you like it will comment with what you have put below
session.set_do_comment(enabled=True, percentage=10)
session.set_comments(["Nice!", "Sweet!", "Beautiful"])

# comments fo specific media types (photo / video)
session.set_comments(['Nice shot!'], media='Photo')
session.set_commnets(['Great video'], media='Video')

# adding the username of the poster to the comment
session.set_comments(['Nice shot! @{}', media='Photo')

#This will limit the interaction with people whow have alot of followers
session.set_relationship_bounds(enabled=True, max_followers=8500)

#This api is used to help your bot analyze the picture and it will avoid some pictures which you have described not to like you have to register with clarifai to get the api token key
session.set_use_clarifai(enabled=True, api_key='replace this with your clarifai token key')
session.clarifai_check_img_for(['nsfw'])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

# end bot session
session.end()

