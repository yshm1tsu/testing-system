import random
import string

def random_code():
    letters_and_digits = string.ascii_letters + string.digits
    result = ''.join((random.choice(letters_and_digits) for i in range(5)))
    return result