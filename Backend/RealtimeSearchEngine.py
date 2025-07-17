import requests
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values
from bs4 import BeautifulSoup

# Load environment variables from the .env file.
env_vars = dotenv_values(".env")

# Retrieve environment variables.
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize Groq API client.
client = Groq(api_key=GroqAPIKey)

# Define system instructions for the AI.
System = f"""Hello, I am {Username}, You are an advanced AI chatbot named {Assistantname} with real-time internet access.
*** Provide concise, professional responses with proper grammar. ***
*** Just answer the question without unnecessary details. ***"""

# Load chat log or create a new one if unavailable.
try:
    with open("Data/ChatLog.json", "r") as f:
        messages = load(f)
except:
    messages = []

# Function to generate real-time date and time info.
def Information():
    now = datetime.datetime.now()
    return f"""Real-time Information:
Day: {now.strftime('%A')}
Date: {now.strftime('%d')} {now.strftime('%B')} {now.strftime('%Y')}
Time: {now.strftime('%H:%M:%S')}
"""

# Function to clean up AI responses and remove unwanted text.
def clean_response(response):
    lines = response.strip().split("\n")
    
    # Remove standalone first line if it's an entity name.
    if len(lines) > 1 and lines[0].strip().isupper():
        return "\n".join(lines[1:]).strip()
    
    return response.strip()

# Function to fetch stock price from Bing
def fetch_stock_price_bing(stock_symbol):
    search_url = f"https://www.bing.com/search?q={stock_symbol}+stock+price"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Send request to Bing
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Look for stock price in the page (this might change depending on Bing's page structure)
        price_div = soup.find("div", {"class": "b_vListPrice"})  # Example class name, check the real structure
        if price_div:
            price = price_div.get_text(strip=True)
            return f"The current stock price of {stock_symbol.upper()} is {price}."
        else:
            return f"Could not find the stock price for {stock_symbol.upper()} on Bing."

    except requests.exceptions.RequestException as e:
        return f"Error fetching stock price: {str(e)}"

# Function to handle AI-generated responses.
def RealtimeSearchEngine(prompt):
    global messages

    # Update chat log.
    messages.append({"role": "user", "content": prompt})

    # Handle stock price queries.
    if "share price" in prompt.lower() or "stock price" in prompt.lower():
        stock_query = prompt.split("of")[-1].strip().upper()
        return fetch_stock_price_bing(stock_query)

    # Generate AI response.
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "system", "content": System}, {"role": "system", "content": Information()}] + messages,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True
    )

    # Process AI response.
    Answer = "".join(chunk.choices[0].delta.content for chunk in completion if chunk.choices[0].delta.content)
    Answer = clean_response(Answer)  # Clean up response

    # Update chat log.
    messages.append({"role": "assistant", "content": Answer})
    with open("Data/ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    return Answer

# Main loop.
if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ").strip()
        if prompt.lower() in ["exit", "quit"]:
            break
        print(RealtimeSearchEngine(prompt))
