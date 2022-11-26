from django.test import TestCase
from datetime import datetime



# Create your tests here.
def start1():
    start = datetime.now()
    return start


def now1(start):
    now = datetime.now()
    now.strftime("%H:%M:%S:%f")[:-4]
    print(now-start)



