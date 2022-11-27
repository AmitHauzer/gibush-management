from django.test import TestCase
from datetime import datetime, timedelta, timezone
import time



# Create your tests here.
# now = datetime.now(tz=timezone.utc).timestamp()
now = datetime.now(tz=timezone.utc)
print(type(now))
print(now)
time.sleep(2)
# now2 = datetime.now(tz=timezone.utc).timestamp()
now2 = datetime.now(tz=timezone.utc)

result = now2.timestamp() - now.timestamp()
print(type(result))
print(result)

t = datetime.fromtimestamp(result, tz=timezone.utc).strftime("%H:%M:%S:%f")[:-4]
print(type(t))
print(t)
