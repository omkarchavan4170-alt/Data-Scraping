# NGO Lead Generation Automation

## Project Overview
This Python automation script collects data on Non-Governmental Organizations (NGOs) to build a lead database. It scrapes public directory information, cleans the data, and organizes it into an Excel file for easy access.

## Tools & Libraries Used
*   **Requests:** To securely fetch HTML content from the target website.
*   **BeautifulSoup (bs4):** To parse the HTML structure and extract specific table data (Name, Location, Category).
*   **Pandas:** To organize the data into a structured DataFrame, remove duplicates, and export to Excel.

## How It Works
1.  The script connects to a public NGO directory (Wikipedia List of NGOs).
2.  It iterates through the data table, extracting the Organization Name, Headquarters, Category, and Founder.
3.  It generates a probable contact email format based on the organization's name.
4.  The data is cleaned (duplicates removed) and saved automatically to `ngo_leads_final.xlsx`.

## Instructions
1.  Install dependencies: `pip install requests beautifulsoup4 pandas openpyxl`
2.  Run the script: `python main.py`
3.  Open the generated `ngo_leads_final.xlsx` file to view the results.
