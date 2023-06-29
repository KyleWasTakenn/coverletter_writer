from bs4 import BeautifulSoup
import requests
# Small function to combine the job posting and qualifications into one prompt for chatGPT
def prompt_creation(qual: str, desc: str):
    # Generating a prompt for the chat bot with some formatting.
    prompt_gen = """
    Could you write me a cover letter?
    This is my resume: 

    """ + qual + """
     
    And this is the job posting:
    """ + desc

    return prompt_gen

# Function for webscraping data from a URL to automatically fetch data.
def get_job_data(url):
    raise NotImplementedError("This function is currently not being used. Awaiting permission from Dice to test.")
    # Make a request to the website
    r = requests.get(url)
    # Parse HTML text
    soup = BeautifulSoup(r.text, 'html.parser')

    # Identify the job title, job description, and company name. This particular set is using the data from Dice.com
    job_title = soup.find('h1', class_='jobTitle').text
    company_name = soup.find('div', class_='companyNameLink').text
    job_description = soup.find('div', class_='jobDescription').text

    return job_title, company_name, job_description