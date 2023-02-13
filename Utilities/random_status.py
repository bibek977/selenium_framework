import string
import random

def status_gen(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))