import os
from datetime import datetime
clear = lambda: os.system('cls') #on Linux System
date_string = datetime.now().isoformat().replace(":", "-")

f = open(f"concert{date_string}.yml", "w")
f.write("conversations:\n")
f.close()

response = input("Enter response: ")

while True:
    print(f"Predicted response: {response}")
    question = input("Expected question: ")
    f = open(f"concert{date_string}.yml", "a")

    f.write(f"- - {question}\n")
    f.write(f"  - {response}\n")
    clear()
    f.close()