# Flipkart Web Scraper

The Flipkart Web Scraper is a Python script designed to extract product data from Flipkart's search results pages. It gathers information such as product title, price, rating, reviews, delivery details, and discounts.

## How It Works

The scraper operates in the following steps:

1. **User Input**: When executed, the script prompts the user to provide the base URL they want to scrape.

2. **Page Range**: Users specify the range of search result pages they want to scrape by entering the start and end pages.

3. **Data Extraction**: The script dynamically generates URLs for each page in the specified range. It then sends HTTP requests to retrieve the HTML content.

4. **Parsing HTML**: Using the `BeautifulSoup` library, the script parses the HTML content to extract relevant information.

5. **Data Storage**: Extracted data, including product title, price, rating, reviews, delivery information, and discounts, is organized into a structured format.

6. **Progress Updates**: The script provides progress updates, displaying the lengths of various data lists after processing each page.

7. **CSV Output**: The collected data is saved to a CSV file named `flipkart_data.csv`.

## How to Use

### Prerequisites

- Python 3.x
- Required Libraries: `requests`, `BeautifulSoup`, `pandas`

### Installation

1. Clone or download this repository to your local machine.

2. Install the necessary Python libraries:

```bash
pip install requests beautifulsoup4 pandas
```

### Usage

1. Run the `flipkart_scraper.py` script.

2. Follow the prompts to input the base URL and page range.

3. The scraper will initiate the data extraction process, providing progress updates.

4. Once complete, the data will be saved in `flipkart_data.csv`.

### Customization

- The script can be customized to extract additional information or adapted for other websites by modifying the code.

### Example

```bash
python3 scraper-main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides a detailed explanation of what the scraper does and how it operates. It also includes instructions on how to install and use the script. Feel free to customize it further based on your specific requirements.