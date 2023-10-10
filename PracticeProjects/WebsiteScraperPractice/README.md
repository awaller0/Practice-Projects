# Web Scraping Practice Project

This is a simple Python practice project focused on web scraping using the `requests` library and the `BeautifulSoup` library. In this project, we scrape a web page from [GeeksforGeeks](https://www.geeksforgeeks.org/python-web-scraping-tutorial/) to extract various types of information.

## Project Overview

The project consists of several sections, each demonstrating different aspects of web scraping. Below is an overview of what each section accomplishes:

### 1. Importing Libraries

- The project begins by importing the necessary libraries: `requests` for making HTTP requests and `BeautifulSoup` for parsing HTML content.

### 2. Retrieving and Parsing HTML

- A GET request is made to fetch the HTML content of the web page.
- The HTML content is parsed using BeautifulSoup.

### 3. Extracting and Printing Title

- The project prints the title of the web page just for fun.

### 4. Scraping Paragraph Content

- The content inside a specific `<div>` element with the class name "text" is extracted.
- All the `<p>` (paragraph) elements within this `<div>` are extracted and printed.

### 5. Scraping Left Sidebar Content

- The project identifies a specific `<div>` element with the id "home-page" where the left sidebar content is located.
- The unordered list (`<ul>`) within this `<div>` is extracted.
- All the list items (`<li>`) within the unordered list are extracted and printed.

### 6. Scraping Images

- The project finds all `<img>` (image) elements on the web page.
- For each image, the source URL (`src`) and alt text (`alt`) attributes are extracted and stored in a list.
- The list of images with their source URLs and alt text is printed.

### 7. Scraping Multiple Pages

- The project demonstrates how to scrape multiple pages by iterating through a list of URLs.
- For each URL in the list, it fetches the content, parses it, and extracts titles with specific attributes. The titles are then printed.

## How to Use

To run this project, follow these steps:

pip install requests
pip install beautifulsoup4

## Note

This is a basic web scraping project for educational purposes. Make sure to respect website terms of service and applicable laws when scraping content from websites.

Feel free to modify and expand upon this project to suit your specific web scraping needs.
