#!/usr/bin/python3

import os

try:
  path = "/mnt/c/Users/Max/MaxVault"
  os.chdir(path)
  write_path = "/mnt/c/Users/Max/MaxVault/README.md"
  tagCount_file = "/mnt/c/Users/Max/MaxVault/tagCount.txt"
  dateCount_file = "/mnt/c/Users/Max/MaxVault/dateCount.txt"
except:
  path = "/Users/maxloo/MaxVault"
  os.chdir(path)
  write_path = path + "/README.md"
  tagCount_file = path + "/tagCount.txt"
  dateCount_file = path + "/dateCount.txt"
github_url_start = "https://github.com/maxloosmu/MaxVault/blob/main/"

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

def write_combined_posts(f, combined_posts):
  newdict1 = dict(sorted(combined_posts.items(), key=lambda item: item[0]))
  newdict2 = dict(sorted(newdict1.items(), key=lambda item: item[1][0], reverse=True))
  newdict3 = dict(sorted(newdict2.items(), key=lambda item: item[1][1]))
  folders = set()
  for github_link in newdict3:
    [date_tag, folder_name, write_sorted_tags] = newdict3[github_link]
    # print(newdict3[github_link])
    # print()
    if folder_name != '!NIL':
      if not folder_name in folders:
        folders.add(folder_name)
        f.write("\n#### " + folder_name + "\n")
    f.write(github_link)
    f.write(write_sorted_tags)
  return f

# folders = []
combined_posts = {}
with open(write_path, 'w') as f:
  f.write("## Notes building with some Obsidian help for self-improvement to simplify work and life, and be ready for an uncertain future.\n")
  f.write("### Date: Posts Count\n")
  with open(dateCount_file, 'r') as g:
    dateCount_lines = g.readlines()
    for line in dateCount_lines:
      f.write("- " + line)
    g.close()
  f.write("\n### Tag: Posts Count\n")
  with open(tagCount_file, 'r') as h:
    tagCount_lines = h.readlines()
    for line in tagCount_lines:
      f.write("- " + line)
    h.close()
  f.write("\n### Blog Posts\n")
  # for file in os.listdir():
  #   if file.endswith(".md"):
  for root, dirs, files in os.walk("."):
    files.sort()
    dirs.sort()
    for file in files:
      if file.endswith(".md"):
        if file != "README.md":
          folder_url = ''
          # write_folder = "NoFolderString"
          len_divided_filename = len(root.split('/'))
          divided_filename = root.split('/')
          if len_divided_filename == 2:
            folder_name = divided_filename[1]
            # if not (folder_name in folders):
            #   folders.append(folder_name)
            #   write_folder = "\n#### " + folder_name + "\n"
            folder_url = folder_name + '/'
            split_folder_url = folder_url.split()
            folder_url = '%20'.join(split_folder_url)
            # print(folder_url)
            # print(dirs)
          else:
            folder_name = '!NIL'
          split_filename_space = file.split()
          name_url = '%20'.join(split_filename_space)
          split_filename_comma = name_url.split(',')
          name_url = '%2C'.join(split_filename_comma)
          # split_filename_dot = name_url.split('.')
          # name_url = '%2E'.join(split_filename_dot)
          github_url = github_url_start + folder_url + name_url
          file_name = file[:-3]
          github_link = f"* [{file_name}]({github_url})\n"
          # file_path = f"{path}/{file}"
          file_path = os.path.join(root, file)
          # print(file_path)
          unjoined_sorted_tags = read_text_file(file_path)
          sorted_tags = ', '.join(unjoined_sorted_tags)
          write_sorted_tags = f"    + {sorted_tags}\n"
          date_tag = unjoined_sorted_tags[0]
          # folder_date_key = folder_name + "|||" + date_tag
          triple = [date_tag, folder_name, write_sorted_tags]
          if not github_link in combined_posts.keys():
            combined_posts[github_link] = triple
          # else:
          #   combined_posts[github_link].append(triple)
  f = write_combined_posts(f, combined_posts)
  f.close()
