import sys
import webbrowser
import traceback
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    """Initialize a WebDriver session."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
    chrome_options.add_argument("--no-sandbox")  # Prevent sandbox issues
    chrome_options.add_argument("--disable-dev-shm-usage")  # Reduce memory usage
    chrome_options.add_argument("--log-level=3")  # Suppress warnings
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection as bot
    chrome_options.add_argument("--start-maximized")  # Ensure all elements are visible

    try:
        # Use Service instead of executable_path
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("WebDriver initialized successfully.")
        return driver
    except Exception as e:
        print("Error initializing WebDriver:", str(e))
        traceback.print_exc()
        sys.exit(1)

def open_website(search_term: str):
    """Perform a Bing search and open the first result in the web browser."""
    driver = initialize_driver()

    try:
        search_url = f"https://www.bing.com/search?q={search_term.replace(' ', '+')}"
        print(f"Searching: {search_url}")
        driver.get(search_url)

        # Wait for the first search result to be visible
        first_result = WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.b_algo a'))
        )

        first_link = first_result.get_attribute('href')
        print(f"First link found: {first_link}")  # Debugging line

        if first_link:
            # Open the link in the web browser only once
            webbrowser.open(first_link)
            print(f"Opened: {first_link}")
        else:
            print("No valid search result found.")

    except Exception as e:
        print("Error during search operation.")
        traceback.print_exc()

    finally:
        driver.quit()  # Ensure WebDriver is closed after each search

def start_search_thread(search_term: str):
    """Start a thread for each search term."""
    search_thread = threading.Thread(target=open_website, args=(search_term,))
    search_thread.start()
    return search_thread

if __name__ == "__main__":
    search_terms = []
    threads = []
    beta=""

    # Start threads for all search terms
    for term in search_terms:
        beta=beta+" "+term
        thread = start_search_thread(term)
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f"Got request from Main.py - Opened{beta}")
