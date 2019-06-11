import os

directory = os.fsencode('/home/paulina/Downloads/PSI-master/procedura')

for file in os.listdir(directory):
     filename = os.fsdecode(file)

     if filename.endswith("info.txt"):
         # print(os.path.join(directory, filename))
         continue
     else:
         os.rename("/home/paulina/Downloads/PSI-master/procedura/"+filename, "/home/paulina/Downloads/PSI-master/proceduraTXT/"+filename)
