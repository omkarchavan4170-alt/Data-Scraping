import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def generate_email(name):
    if not name or name == "N/A":
        return "N/A"
    return name.lower().replace(" ", ".") + "@example.com"


def safe_text(element, selector):
    try:
        return element.find(selector).text.strip()
    except:
        return "N/A"


def safe_attr(element, tag, attr):
    try:
        return element.find(tag)[attr].strip()
    except:
        return "N/A"


def scrape_books():
    data = []
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"

    for page in range(1, 3):
        try:
            res = requests.get(base_url.format(page), timeout=10)
            res.raise_for_status()
        except:
            continue

        soup = BeautifulSoup(res.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            name = safe_attr(book.h3, "a", "title") if book.h3 else "N/A"
            price = safe_text(book, "p")
            availability = safe_text(book, "p")

            if name == "N/A":
                continue

            data.append({
                "Name": name,
                "Email": generate_email(name),
                "Website": "http://books.toscrape.com",
                "Location": "N/A",
                "Info": f"{price} | {availability}"
            })

    return data


def scrape_quotes():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("http://quotes.toscrape.com/")
    time.sleep(2)

    data = []

    while len(data) < 20:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for q in quotes:
            if len(data) >= 20:
                break

            try:
                author = q.find_element(By.CLASS_NAME, "author").text.strip()
            except:
                author = "N/A"

            try:
                text = q.find_element(By.CLASS_NAME, "text").text.strip()
            except:
                text = "N/A"

            if author == "N/A" and text == "N/A":
                continue

            data.append({
                "Name": author,
                "Email": generate_email(author),
                "Website": "http://quotes.toscrape.com",
                "Location": "N/A",
                "Info": text
            })

        try:
            driver.find_element(By.LINK_TEXT, "Next").click()
            time.sleep(2)
        except:
            break

    driver.quit()
    return data


def process_and_save(data):
    df = pd.DataFrame(data)
    df.replace("", "N/A", inplace=True)
    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)
    df = df[df["Name"] != "N/A"]
    df.to_excel("final_leads.xlsx", index=False)


def main():
    books = scrape_books()
    quotes = scrape_quotes()
    process_and_save(books + quotes)


if __name__ == "__main__":
    main()
