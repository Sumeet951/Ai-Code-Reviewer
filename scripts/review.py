from dotenv import load_dotenv
import subprocess
from google import genai
import os
import smtplib
from email.message import EmailMessage
# from mistralai import Mistral

# client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

load_dotenv()

def getDiff():
    diff=subprocess.check_output(["git","show"],text=True)
    return diff
print(getDiff())

client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("GOOGLE_API_KEY loaded:", os.getenv("GOOGLE_API_KEY") is not None)
def send_email(html_content):
    msg=EmailMessage()
    msg['Subject']="Code Review Feedback"
    msg['From']="sg297979@gmail.com"
    msg['To']="sumeet.ng@somaiya.edu"
    msg.set_content("Please find the code review feedback below")
    msg.add_alternative(html_content,subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login("sg297979@gmail.com",os.getenv("MAIL_APP_PASSWORD"))
        smtp.send_message(msg)
    return "Email sent successfully"
def main():
    diff=getDiff()
    prompt=f"Review the following code changes and provide feedback:\n\n Mandatory:provide the outpu in html that can use to send in mail \n\n{diff}"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt]
        
    )
    print("Code Review Feedback:")
    print(response.text)
    html=response.text
    send_email(html)


main()
