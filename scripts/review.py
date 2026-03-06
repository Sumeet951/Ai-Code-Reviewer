from dotenv import load_dotenv
import subprocess
from google import genai
import os
# from mistralai import Mistral

# client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

# load_dotenv()

def getDiff():
    diff=subprocess.check_output(["git","show"],text=True)
    return diff
print(getDiff())

client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("GOOGLE_API_KEY loaded:", os.getenv("GOOGLE_API_KEY") is not None)
def main():
    diff=getDiff()
    prompt=f"Review the following code changees and provide feedback:\n{diff}"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt]
        
    )
    print("Code Review Feedback:")
    print(response.text)


main()
