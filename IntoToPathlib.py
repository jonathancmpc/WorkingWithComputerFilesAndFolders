from pathlib import Path

p1 = Path('files/abcd.txt')

if p1.exists():
  with open(p1, 'r') as file:
      print(file.read())
elif not p1.exists():
  with open(p1, 'w') as file:
      file.write('Content 3')

#get the name and suffix file
print(p1.name)
#get the name
print(p1.stem)
#get the suffix
print(p1.suffix)

#list the files in directory
p2 = Path('files')
print(p2.iterdir())
for item in p2.iterdir():
   print(item)

#or print at the list
print(list(p2.iterdir()))