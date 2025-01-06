#Good morning , Good Evening , Good Night

import time
current = time.localtime(time.time())
if current.tm_hour < 12:
    print("good morning")
elif current.tm_hour < 18:
    print("good afternoon")
elif current.tm_hour > 18:
    print("good evening")
else:
    print(".")
