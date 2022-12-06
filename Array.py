# with open("WordFile.txt") as f:
#     for line in file
import random

with open("WordFile.txt") as file:
    lines = [line.rstrip() for line in file]
    # print(lines);
    print(random.choices(lines));

op = str(lines);

file = open("Op.txt","w")
file.write(op);
file.close();
