#!/usr/bin/python3

import os

path = "/mnt/c/Users/Max/MaxVault"
write_path = "/mnt/c/Users/Max/MaxVault/README.md"
tagCount_file = "/mnt/c/Users/Max/MaxVault/tagCount.txt"
os.chdir(path)

def read_text_file(file_path):
  file_tags = []
  sorted_tags = []
  with open(file_path, 'r') as f:
    for line in f:
      first_split = line.split()
      if len(first_split) > 0:
        first_in_line = line.split()[0]
        first_in_line_parts = len(first_in_line.split("#"))
        if first_in_line_parts > 1:
          tag = first_in_line.split("#")[1]
          if not not tag:
            file_tags.append(tag)
    file_tags.sort()
    f.close()
  return file_tags

with open(write_path, 'w') as f:
  f.write("### Tag: Count\n")
  with open(tagCount_file, 'r') as g:
    tagCount_lines = g.readlines()
    for line in tagCount_lines:
      f.write("- " + line)
    g.close()
  f.write("\n### Blog Posts\n")
  # for file in os.listdir():
  #   if file.endswith(".md"):
  for root, dirs, files in os.walk("."):
    for file in files:
      if file.endswith(".md"):
        if file != "README.md":
          split_name = file.split()
          url_name = '%20'.join(split_name)
          github_url = "https://github.com/maxloosmu/MaxVault/blob/main/" + url_name
          file_name = file[:-3]
          f.write(f"* [{file_name}]({github_url})\n")
          # file_path = f"{path}/{file}"
          file_path = os.path.join(root, file)
          sorted_tags = ', '.join(read_text_file(file_path))
          f.write(f"    + {sorted_tags}\n")
  f.close()