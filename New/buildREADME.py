import os

path = "/mnt/c/Users/Max/MaxVault"
write_path = "/mnt/c/Users/Max/MaxVault/README.md"
os.chdir(path)

with open(write_path, 'w') as f:
  for file in os.listdir():
    if file.endswith(".md"):
      split_name = file.split()
      rejoin_name = '%20'.join(split_name)
      github_link = "https://github.com/maxloosmu/MaxVault/blob/main/" + rejoin_name
      file_name = file[:-3]
      f.write(f"[{file_name}]({github_link})\n")
  f.close()