import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#   # print(job_element, end="\n"*2)
#   title_element = job_element.find("h2", class_="title")
#   company_element = job_element.find("h3", class_="company")
#   location_element = job_element.find("p", class_="location")
#   print(title_element.text.strip())
#   print(company_element.text.strip())
#   print(location_element.text.strip())
#   print()
# python_jobs = results.find_all("h2", string="Python")
python_jobs = results.find_all(
  "h2", string=lambda text: "python" in text.lower()
)
# print(python_jobs)
# print(len(python_jobs))
python_job_elements = [
  h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
  title_element = job_element.find("h2", class_="title")
  company_element = job_element.find("h3", class_="company")
  location_element = job_element.find("p", class_="location")
  print(title_element.text.strip())
  print(company_element.text.strip())
  print(location_element.text.strip())
  print()
  links = job_element.find_all("a")
  link = links[1]
  link_url = link["href"]
  print(f"Apply here: {link_url}\n")

