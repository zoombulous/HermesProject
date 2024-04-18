# Import the scrape_job_listings function from job_scraper.py
from job_scraper import scrape_job_listings

# Define the sample URL from Remote.co
remote_co_url = 'https://remote.co/remote-jobs/'

# Call the scrape_job_listings function with the sample URL
job_titles, job_descriptions, application_details = scrape_job_listings(remote_co_url)

# Print the extracted information
print("Job Titles:", job_titles)
print("Job Descriptions:", job_descriptions)
print("Application Details:", application_details)
