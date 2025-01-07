# Flipkart Scraper

A web scraping project built using the [Scrapy](https://scrapy.org/) framework to extract product data from Flipkart. This scraper focuses on collecting details about phones, including their names, prices, ratings, images, and URLs.

## Features

- Extracts product data from Flipkart, including:
  - Product name
  - URL
  - Price
  - Rating
  - Image URL
- Handles pagination to scrape multiple pages of results.
- Stores the scraped data in a MongoDB database for easy access and analysis.
- Implements duplicate detection using hashed URLs to avoid redundant entries.

## Technologies Used

- Python
- Scrapy framework
- MongoDB for data storage
- XPath and CSS selectors for web scraping

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8+
- MongoDB
- Required Python packages (listed in `requirements.txt`)

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/josh1221wa/flipkart_scraper_mongodb
   cd flipkart-scraper
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your MongoDB connection in settings.py:

   ```python
   MONGO_URI = 'mongodb://localhost:27017'
   MONGO_DATABASE = 'flipkart_data'
   ```

4. Run the scraper:

   ```bash
   scrapy crawl flipkart_spider
   ```

## Configuration

You can modify the following settings in `settings.py`:

- **`MONGO_URI`**: URI for connecting to your MongoDB instance.
- **`MONGO_DATABASE`**: Name of the MongoDB database where data will be stored.
- **`DOWNLOAD_DELAY`**: Set a delay between requests to avoid being blocked.
- **`USER_AGENT`**: Customize the user agent to mimic a browser.

## Usage

- Start the scraper to extract product data:
  ```bash
  scrapy crawl flipkart_spider
  ```

## Usage

- Start the scraper to extract product data:
  ```bash
  scrapy crawl flipkart_spider
  ```
- Data will be stored in the specified MongoDB collection (phones by default).

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to submit a pull request or open an issue.
