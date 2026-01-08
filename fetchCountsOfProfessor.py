from scholarly import scholarly
import pandas as pd
import re

id="i7k_9SEAAAAJ"  # id example for Aamir wali (https://scholar.google.com/citations?user=i7k_9SEAAAAJ&hl=en)
profile_url = f"https://scholar.google.com/citations?hl=en&user={id}"
user_id_match = re.search(r'user=([\w-]+)', profile_url)
if not user_id_match:
    raise ValueError("Invalid Google Scholar URL")

user_id = user_id_match.group(1)

author = scholarly.search_author_id(user_id)
author_filled = scholarly.fill(author)

years = []
for pub in author_filled['publications']:
    year = pub.get("bib", {}).get("pub_year")
    if year and year.isdigit():
        years.append(int(year))

df = pd.Series(years).value_counts().sort_index().reset_index()
df.columns = ['Year', 'Publications']

print(df.to_string(index=False))
