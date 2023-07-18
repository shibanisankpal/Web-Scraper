import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def scrape_webpage(url, tag, class_name):
    soup = get_page_content(url)
    results = soup.find_all(tag, class_=class_name)
    return results

# Streamlit web app
def main():
    st.title("Web Scraping with Streamlit")

    # Input URL from the user
    url = st.text_input("Enter the URL of the webpage to scrape:")

    # Dropdown list for HTML tags
    tag_options = ['div', 'p', 'h1', 'a', 'img', 'table', 'ul', 'ol', 'li']
    tag = st.selectbox("Select the HTML tag to search for:", tag_options)

    class_name = st.text_input("Enter the class name to search for (optional):")

    if st.button("Scrape"):
        try:
            results = scrape_webpage(url, tag, class_name)

            if not results:
                st.write("No results found.")
            else:
                st.write("Scraped content:")
                for result in results:
                    st.write(result.text)
        except Exception as e:
            st.write("Error occurred:", e)

if __name__ == "__main__":
    main()
