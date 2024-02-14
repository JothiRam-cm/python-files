#####################################################################################################################
#To retrieve content from a webpage in Python, you can use libraries like requests to fetch the HTML 
# content and BeautifulSoup to parse and navigate the HTML. 
# Here's an example of a program that fetches and extracts content from a webpage:
# In this example, replace https://example.com with the URL of the webpage you want to retrieve content from.' 
#The program uses the requests library to send a GET request and fetch the HTML content.'
#Then, it uses BeautifulSoup to parse the HTML and extract specific elements like the title and paragraphs'"
''''import requests
from bs4 import BeautifulSoup
class content:
# URL of the webpage you want to fetch content from
 url = "https://trends.google.com/trends/trendingsearches/realtime?geo=IN&hl=en-US&category=all"

# Send a GET request to the URL
 response = requests.get(url)
 # Check if the request was successful
 if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find elements by their HTML tags and attributes
    title_element = soup.find("title")
    paragraph_elements = soup.find_all("p")
    header_text=soup.find("head")
    # Extract text content from the elements
    title = title_element.text if title_element else "No title found"
    paragraphs = [p.text for p in paragraph_elements]
    header=[h.text for h in header_text]
    # Print the extracted content
    print("Title:", title)
    print("header",header)
    print("Paragraphs:")
    for idx, paragraph in enumerate(paragraphs, start=1):
        print(f"{idx}. {paragraph}")
 else:
    print("Failed to fetch the webpage. Status code:", response.status_code)



#**************************************************************************************************************#

def generate_webpage(title, header_text, paragraph_text):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <header>
            <h1>{header_text}</h1>
        </header>
        <main>
            <p>{paragraph_text}</p>
        </main>
    </body>
    </html>
    """
    return html_code

# Input data
title = content.title
header_text = content.header
paragraph_text = content.paragraphs
# Generate the HTML code
webpage_code = generate_webpage(title, header_text, paragraph_text)

# Save the HTML code to a file
with open("index.html", "w") as file:
    file.write(webpage_code)

print("Webpage generated successfully!")'''

#######################################################################################################################
import spacy
import random
import openai
from flask import Flask, render_template, request

# Set up Flask
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load Jinja2 template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")

# Process user input using NLP
def process_user_input(user_input):
    doc = nlp(user_input)
    keywords = [token.text for token in doc if token.pos_ == "NOUN"]
    purpose = " ".join([token.text for token in doc if token.pos_ == "VERB"])
    return keywords, purpose

# Generate color scheme
def generate_color_scheme():
    colors = ["#FF5733", "#FFC300", "#C70039", "#900C3F", "#581845"]
    return random.choice(colors)

# Generate content using GPT-3
def generate_content(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=200
    )
    return response.choices[0].text.strip()

# Render website using Jinja2
def render_website(content, color_scheme):
    return template.render(content=content, color_scheme=color_scheme)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form["user_input"]
    keywords, purpose = process_user_input(user_input)
    content = generate_content(user_input)
    color_scheme = generate_color_scheme()
    website = render_website(content, color_scheme)
    return website

# Run the app
if __name__ == "__main__":
    app.run()