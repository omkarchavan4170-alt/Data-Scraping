import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_wikipedia_ngos():
    data = []
    url = "https://en.wikipedia.org/wiki/List_of_non-governmental_organisations_in_India"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        
        table = soup.find("table", class_="wikitable")
        rows = table.find_all("tr")
        
       
        for row in rows[1:]:
            cols = row.find_all(["td", "th"])
            if len(cols) >= 4:
                # Extract text and clean up references (like [1])
                name = cols[0].text.strip()
                category = cols[1].text.strip()
                location = cols[3].text.strip()
                founder = cols[4].text.strip() if len(cols) > 4 else "N/A"
                
                # Generate a placeholder email since Wikipedia doesn't list them
                email_guess = f"contact@{name.lower().split()[0].replace('.', '')}.org"

                data.append({
                    "Organization Name": name,
                    "Category": category,
                    "Location (HQ)": location,
                    "Founder": founder,
                    "Estimated Email": email_guess,
                    "Source URL": url
                })
                
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

    return pd.DataFrame(data)

def clean_and_save(df):
    if df.empty:
        print("No data found.")
        return

    df = df[df["Organization Name"] != ""] 
    df = df.drop_duplicates(subset=["Organization Name"]) 
    
    
    filename = "ngo_leads_final.xlsx"
    df.to_excel(filename, index=False)
    print(f"Successfully saved {len(df)} NGOs to {filename}")

if __name__ == "__main__":
    print("Starting scraper...")
    df_leads = scrape_wikipedia_ngos()
    clean_and_save(df_leads)
    print("Done.")
