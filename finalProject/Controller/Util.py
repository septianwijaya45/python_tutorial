import random
import string

def generatePrimary(panjang:int) -> str:
    primary = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return primary
