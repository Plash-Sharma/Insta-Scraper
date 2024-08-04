# Instagram Scraper

This Python project uses Selenium to scrape data from Instagram profiles. The scraper retrieves the specified number of recent posts from a target profile and collects information on the number of likes and post dates.

#### Video Demo: <>


## Features

- Login to Instagram using your credentials.
- Scrape a specified number of recent posts from any public profile.
- Extract the number of likes and the date of each post.
- Display the results in a formatted table in the terminal.
- Save the results to a CSV file for further analysis.
- Optionally open the CSV file in Excel after scraping.

## Requirements

- Python 3.x
- Selenium library
- Maskpass library
- Requests library
- Tabulate library

You can install the required libraries using pip:


```bash
pip install selenium maskpass requests tabulate
```

## Usage
- Open the terminal and navigate to the project directory.

- Run the script:
```bash
python project.py
```
- Follow the prompts to enter your Instagram username, password, the profile you want to scrape, and the number of posts to retrieve.

## Important Notes
- Download the appropriate ChromeDriver for your version of Chrome from ChromeDriver. Ensure that it is in your system PATH or specify its path in the script.
- Make sure your Instagram account is public or that you are logged in to access private profiles you follow.
- Ensure you handle your credentials securely; consider using environment variables or a secure credential storage method.

## CSV File
- The scraped data will be saved to a CSV file named I_SCRAPE.csv in the project directory. You will be prompted to open the file in Excel after the scraping is complete.

## Acknowledgements
- Selenium Documentation
- Instagram

