# Web-Scraper

This is a simple web scraping project built using Python and Streamlit. The project allows users to input a URL and retrieve specific information from that webpage using web scraping techniques.



## Introduction
Web scraping is a technique used to extract data from websites. This project leverages the BeautifulSoup library to parse HTML content and the requests library to fetch webpages. Streamlit, a powerful Python library, is used to create a web application that allows users to interactively perform web scraping.

This project aims to demonstrate how web scraping can be implemented using Python and Streamlit. It provides a simple interface for users to input a URL and retrieve content based on their selected HTML tag and class name.

## Features
-User-friendly web interface powered by Streamlit.
-Ability to input any URL for web scraping.
-Dropdown list for selecting the HTML tag, making it easier to choose the correct tag.
-Option to specify a class name to target specific elements.
-Display of scraped content on the web page.

Link to application deployed on Streamlit Community Cloud: 

## Installation
To run this project locally, follow these steps:

-Clone this repository to your local machine:

git clone https://github.com/shibanisankpal/Web-Scraper.git
cd Web-Scraper

-Install the required Python libraries using pip:

pip install streamlit beautifulsoup4 requests

-Usage
Start the Streamlit app by running the following command in your terminal:

streamlit run app.py

Once the app is running, open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

Enter the URL of the webpage you want to scrape in the input box.

Select the HTML tag you want to extract from the webpage using the dropdown list.

Optionally, enter a class name to further refine the search.

Click the "Scrape" button to retrieve and display the content on the web page.
