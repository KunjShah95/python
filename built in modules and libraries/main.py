import math
from datetime import datetime, timedelta
import random 
import os
import sys
from collections import Counter, defaultdict, deque


print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120
print(math.pi)             # 3.14159...
print(math.ceil(3.2))      # 4
print(math.floor(3.8))     # 3

now = datetime.now()
print("Current time:", now)

#Add 5 days 
future= now + timedelta(days=5)
print("5 days later:", future.strftime("%Y-%m-%d %H:%M:%S"))

print(random.randint(1, 10))        # Random integer between 1 and 10
print(random.choice(['A', 'B', 'C']))  # Random choice
random.shuffle([1, 2, 3, 4])         # Shuffle list in-place

print(os.getcwd())        # Current working directory
os.mkdir("new_folder")    # Create folder
os.remove("demo.txt")     # Delete file

print(sys.version)      # Python version
print(sys.argv)         # Command-line arguments
sys.exit()              # Exit the program

cnt = Counter("banana")
print(cnt)  # Counts each character

# defaultdict
d = defaultdict(int)
d['a'] += 1
print(d['a'], d['b'])  # 1 0

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # deque([0, 1, 2, 3, 4])


# Create a virtual environment
#python -m venv env

# Activate:
# Windows
# env\Scripts\activate

# Linux/Mac
# source env/bin/activate

# Deactivate
# deactivate

"""pip install requests
pip uninstall requests
pip list
"""

#example of using a library
"""import requests

response = requests.get("https://api.github.com")
print(response.status_code)
"""

