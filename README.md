# Lead Generation Automation (Selenium + Pagination)

## Overview

This project automates lead data collection using Python and Selenium. It extracts structured data from a publicly available website and stores it in an organized Excel file.

The script navigates across multiple pages using pagination, collects relevant fields, performs basic data cleaning, and generates sample email formats for each entry.

---

## Features

* Automated web scraping using Selenium
* Pagination handling (multi-page data collection)
* Extraction of key fields:

  * Name
  * Email (generated)
  * Website
  * Location
* Data cleaning:

  * Duplicate removal
  * Handling missing values
* Export to Excel file
* Headless browser execution (runs in background)

---

## Technologies Used

* Python
* Selenium (browser automation)
* Pandas (data processing)
* WebDriver Manager (driver setup automation)

---

## How It Works

1. Launches a headless browser using Selenium
2. Loads the target website
3. Extracts data from each page
4. Navigates through pages using the "Next" button
5. Stores collected data in a structured format
6. Cleans the dataset
7. Exports the final data into an Excel file

---

## Installation

```bash
pip install selenium pandas webdriver-manager openpyxl
```

---

## Usage

```bash
python main.py
```

After execution, the output file will be saved as:

```
leads_selenium_pagination.xlsx
```

---

## Output

The generated Excel file contains:

* Name
* Email
* Website
* Location
* Sample Text (additional extracted field)

---

## Notes

* The email field is generated using a simple naming convention for demonstration purposes.
* The dataset is collected from a static website used for scraping practice.
* The script is designed to handle pagination dynamically.

---

## Future Improvements

* Integration with APIs (e.g., Google Sheets for cloud storage)
* Real-world company data scraping
* Email validation using external APIs
* Scheduled automation (cron jobs)
* Database integration for scalable storage

---

## Conclusion

This project demonstrates the use of Selenium for automated data extraction, pagination handling, and basic data processing. It can be extended into a full-scale lead generation system with API integrations and deployment.
