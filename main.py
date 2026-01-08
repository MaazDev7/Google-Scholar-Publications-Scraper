import pandas as pd
import re
import time
from scholarly import scholarly

input_df = pd.read_excel("professors.xlsx")

all_data = []

for index, row in input_df.iterrows():
    name = row['Names']
    profile_id = row['Profile ID']

    print(f"Processing: {name} ({profile_id})")

    try:
        profile_url = f"https://scholar.google.com/citations?hl=en&user={profile_id}"
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
        df['Professor Name'] = name

        all_data.append(df)
        time.sleep(2)  # Delay to avoid throttling

    except Exception as e:
        print(f"Error processing {name}: {e}")
        all_data.append(pd.DataFrame([{
            'Professor Name': name,
            'Year': 'Error',
            'Publications': str(e)
        }]))

final_df = pd.concat(all_data, ignore_index=True)
final_df = final_df[['Professor Name', 'Year', 'Publications']]

final_df.to_excel("result.xlsx", index=False)
print("Output saved as 'result.xlsx'")
