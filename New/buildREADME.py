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

folders = []
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
          folder_url = ''
          len_divided_filename = len(root.split('/'))
          divided_filename = root.split('/')
          if len_divided_filename == 2:
            folder_name = divided_filename[1]
            if not (folder_name in folders):
              folders.append(folder_name)
              f.write("\n#### " + folder_name + "\n")
            folder_url = folder_name + '/'
            split_folder_url = folder_url.split()
            folder_url = '%20'.join(split_folder_url)
            print(folder_url)
          split_filename = file.split()
          name_url = '%20'.join(split_filename)
          github_url = "https://github.com/maxloosmu/MaxVault/blob/main/" + folder_url + name_url
          file_name = file[:-3]
          f.write(f"* [{file_name}]({github_url})\n")
          # file_path = f"{path}/{file}"
          file_path = os.path.join(root, file)
          # print(file_path)
          sorted_tags = ', '.join(read_text_file(file_path))
          f.write(f"    + {sorted_tags}\n")
  f.close()