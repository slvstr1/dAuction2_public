# creates any number of users

# passwords are set as plain$$PASSWORD in DB but can be created in normal way using User.objects.create_user
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dAuction2.settings")
django.setup()



import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()

# create superuser
try:
    user = User.objects.create_user(username="admin", is_staff=True, is_superuser=True, password="admin")
    user.save()
except:
    print("no superuser created")


# generate and createusers 01 - 40
to_add_user=[]
for user_number in range(1,41):
    # transform 2 to 02
    user_number=str(user_number).zfill(2)
    # create username and pass
    user_name = "u" + user_number
    user_password = user_name

    # create user object itself and save it to db
    user = User.objects.create_user(username=user_name, password=user_password)
    to_add_user.append(user)
    # user.save()
msg = User.objects.bulk_create(to_add_user)

