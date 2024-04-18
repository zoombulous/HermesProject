import requests
from bs4 import BeautifulSoup

def get_job_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('h2', {'class': 'title'})
    return [job.text.strip() for job in jobs]

if __name__ == "__main__":
    url = "https://www.indeed.com/q-data-scientist-jobs.html"
    job_titles = get_job_titles(url)
    print("Job Titles:")
    print("\n".join(job_titles))
