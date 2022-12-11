import os

path = "/mnt/c/Users/Max/MaxVault"
write_path = "/mnt/c/Users/Max/MaxVault/tagCount.txt"

os.chdir(path)

mylist = []
myset = set()
mydict = {}
newdict = {}

def read_text_file(file_path):
  with open(file_path, 'r') as f:
    # print(file_path)
    # print(f.read())
    for line in f:
      first_split = line.split()
      if len(first_split) > 0:
        first_in_line = line.split()[0]
        first_in_line_parts = len(first_in_line.split("#"))
        if first_in_line_parts > 1:
          tag = first_in_line.split("#")[1]
          mylist.append(tag)
          myset.add(tag)
    f.close()

for file in os.listdir():
  if file.endswith(".md"):
    file_path = f"{path}/{file}"
    read_text_file(file_path)

for val in myset:
  mydict[val] = mylist.count(val)
  newdict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))

print(newdict)
with open(write_path, 'w') as f:
  f.close()
with open(write_path, 'a') as f:
  for key in newdict:
    f.write(f"{key}: {newdict[key]}\n")
  f.close()