import os

path = "/mnt/c/Users/Max/MaxVault"
write_path = "/mnt/c/Users/Max/MaxVault/README.md"
tagCount = "/mnt/c/Users/Max/MaxVault/tagCount.txt"
os.chdir(path)

with open(write_path, 'w') as f:
  f.write("### Tag: Count\n")
  with open(tagCount, 'r') as g:
    tagCount_lines = g.readlines()
    for line in tagCount_lines:
      f.write("- " + line)
    g.close()
  f.write("\n### Blog Posts\n")
  for file in os.listdir():
    if file.endswith(".md"):
      if file != "README.md":
        split_name = file.split()
        rejoin_name = '%20'.join(split_name)
        github_link = "https://github.com/maxloosmu/MaxVault/blob/main/" + rejoin_name
        file_name = file[:-3]
        f.write(f"- [{file_name}]({github_link})\n")
  f.close()