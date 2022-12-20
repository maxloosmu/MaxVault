#!/usr/bin/python3
# ./test.py
import os

for root, dirs, files in os.walk(".", topdown=False):
  for name in files:
    print(os.path.join(root, name))
  for name in dirs:
    print(os.path.join(root, name))

combined_posts = {
	'cappuccino': [2022-11,
	'latte': [2022-11,
	'espresso': [2022-11,
	'americano': [2022-11,
	'cortado': [2022-11,
}
triple = [date_tag, github_link, write_sorted_tags]
          if not folder_name in combined_posts.keys():