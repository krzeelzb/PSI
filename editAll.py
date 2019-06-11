import os

directory = os.fsencode('/home/paulina/Downloads/PSI-master/pocedura')

for file in os.listdir(directory):
     filename = os.fsdecode(file)

     # if filename.endswith("info.txt"):
     #     # print(os.path.join(directory, filename))
     #     continue
     # else:
     print(filename)
