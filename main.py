import openai
import os
import time
import pyperclip
import functions
import pyfiglet
from dotenv import load_dotenv
#import textwrap

# Fetch private API key from OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Importing a text version of my resume for openAI to use
resume = open('gpt_resume.txt', 'r')
text = resume.read()
resume.close()

def main():
  while True:
    # Main menu
    main_menu = pyfiglet.figlet_format("Cover Letter Writer", font = "digital", width = 50)
    print(main_menu)
    print("[1] Write a cover letter")
    print("[2] Re-write previous cover letter")
    print("[3] Quit")


    # Get option from the user
    option = input("What would you like to do?: ")


    # Option #1: Writing a cover letter.
    if option == "1":
    # Get necessary information from the user
    # With permission from Dice.com, this will be replaced with BeautifulSoup4 website scraping
      job_board = input("Which job board did you find this job on?: ")
      employer_name = input("What is the name of the company?: ")
      job_title = input("What is the advertised job title?: ")
      job_description = input("Paste job description here: ")

      # Create the prompt using function
      prompt = functions.prompt_creation(text, job_description)    


      # chatGPT generates a response with GPT-3.5-turbo into a class object
      cover_letter = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": 
                  prompt}]
      )


      # Turn the class object output into a string so that it is readable by the split function.
      output = cover_letter['choices'][0]['message']['content']


      #Formats the output to seperate the paragraphs, and replaces placeholder values, then prints the output
      output = output.replace("[Company Name]", "Hiring Manager")
      output = output.replace("[Employer's Name]", "Hiring Manager")
      output = output.replace("[Hiring Manager]", "Hiring Manager")

      output = output.replace("[Job Title]", job_title)
      output = output.replace("[Job Position]", job_title)

      output = output.replace("[Job Board]", job_board)
      output = output.replace("[Job Board/Company Website]", job_board)

      formatted_cover_letter = "\n\n".join(output.split('\n\n'))
      pyperclip.copy(formatted_cover_letter)
      print("Your cover letter has been copied to your clipboard.")
      time.sleep(2)
      print("Returning to main menu.")
      print("""

      """)
    # Option #2: Re-writing a cover letter using last entered data.
    if option == "2":
       #Only including one of the variables, because all of them should have a value other than none if one of them does. Proabably not best practice.
       if job_board != None:
        prompt = functions.prompt_creation(text, job_description)    


        #chatGPT generates a response with GPT-3.5-turbo into a class object
        cover_letter = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", 
          messages=[{"role": "user", "content": 
                    prompt}]
        )


        #Turn the class object output into a string so that it is readable by the split function.
        output = cover_letter['choices'][0]['message']['content']


        #Formats the output to seperate the paragraphs, and replaces placeholder values, then prints the output
        output = output.replace("[Company Name]", employer_name)

        output = output.replace("[Job Title]", job_title)
        output = output.replace("[Job Position]", job_title)

        output = output.replace("[Job Board]", job_board)
        output = output.replace("[Job Board/Company Website]", job_board)

        formatted_cover_letter = "\n\n".join(output.split('\n\n'))
        pyperclip.copy(formatted_cover_letter)
        print("Your cover letter has been copied to your clipboard.")
        time.sleep(2)
        print("Returning to main menu.")
        print("""

        """)
       else:
        print("No previous prompt could be found.")
    # Option #3: Quitting the program
    if option == "3":
      print("Goodbye!")
      time.sleep(2)
      break



if __name__ == "__main__":
   main()