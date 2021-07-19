from loginSignup.resources import CustomUserResourece
from hacking_challenge.wsgi import *

custom_user_resource = CustomUserResource()
dataset = custom_user_resource.export()
dataset.csv
