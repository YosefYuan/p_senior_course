
# main.py
from utils import get_sum
from class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode("hello"))
print(decoder.decode("world"))