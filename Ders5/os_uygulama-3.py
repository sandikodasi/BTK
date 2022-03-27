import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Aynı isimle dosyan var!")