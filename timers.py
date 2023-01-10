import time
from datetime import datetime, timedelta


a = time.time()
b = datetime.now()

print(type(a))
print(a)

print('\n', type(b))
print(b.strftime("%I %p"))
print(b.strftime("%H:%M"))
print(b.strftime("%H:%M"))
print("{}:{}".format(b.hour, b.minute))
