
# generowanie hasła zrobione za pomoca biblioteki :D

import random
import string

password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(10)])
print(password)