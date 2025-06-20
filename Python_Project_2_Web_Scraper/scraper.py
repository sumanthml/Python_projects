import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.bbc.com/news"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

headlines = []
for tag in soup.find_all('h3'):
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)

# Save to CSV
df = pd.DataFrame(headlines, columns=["Headline"])
df.to_csv("sample_output.csv", index=False)
print("✅ Headlines scraped and saved to sample_output.csv")

