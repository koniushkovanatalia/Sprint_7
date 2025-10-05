import random
import string

def random_login():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

def random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def random_name():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

