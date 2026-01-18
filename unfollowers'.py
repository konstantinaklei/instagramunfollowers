from instagrapi import Client
import time
import numpy as np
import matplotlib.pyplot as plt


# Στοιχεία σύνδεσης
user_name = 'username'
password = '********'













client = Client()

try:
    client.login(user_name, password)
    print("Succes sign in")
except Exception as e:
    print(f"No sign in: {e}")
try:
    client.insights_media_feed_all("VIDEO", "ONE_WEEK", "LIKE_COUNT", 42)
    client.insights_account()

    media_pk = client.media_pk_from_url('https://www.instagram.com/p/CP5h-I1FuPr/')
    client.insights_media(media_pk)
    print("Succes data")
except Exception as e:
    print(f"No data: {e}")
user_id = client.user_id
followers = client.user_followers(user_id)  # Όσοι σε ακολουθούν
following = client.user_following(user_id)  # Όσους ακολουθείς
non_followers = {user for user in following if user not in followers}

print(f"vrika {len(non_followers)} xristes pou de se akolouthoun piso:")
for user_id in non_followers:
    user_info = following[user_id]
    print(f"{user_info.username} ")


