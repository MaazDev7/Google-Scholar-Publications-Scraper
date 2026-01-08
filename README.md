# Google-Scholar-Publications-Scraper

This project scrapes publication metadata from **Google Scholar** profiles of university faculty members and generates a **year-wise publication dataset** that can be used for analytics and visualizations such as **bar chart race animations** (e.g., using Flourish).

---

## 📊 Project Overview

- Scrapes **publication years** from Google Scholar profiles
- Aggregates **year-wise publication counts**
- Supports **multiple professors** via an input Excel file
- Outputs a clean dataset ready for visualization tools
- Final data used to create **bar chart race animations**

---

## 📁 Repository Structure
```
├── main.py # Scrapes data for multiple professors
├── fetchCountsOfProfessors.py # Single-professor publication analysis
├── professors.xlsx # Input file (Professor Name, Scholar Profile ID)
├── professor_jounal_pubs.csv.csv # Generated output having analytics for all professors
├── README.md # docs ( you are watching me )
```

---

## 🧠 How It Works

### Input
- `professors.xlsx`
  - Contains:
    - **Prof. Name**
    - **Google Scholar Profile ID**

### Processing
- Uses the `scholarly` Python library to fetch publication metadata
- Extracts publication years from each profile
- Aggregates yearly publication counts
- Handles throttling using request delays

### Output
- A structured dataset with:
  - Professor Name
  - Year
  - Number of Publications

This dataset is directly compatible with tools like **Flourish**, **Tableau**, or **Power BI**.

---

## 🛠️ Technologies Used

- **Python**
- **pandas**
- **scholarly**
- **Regex**
- **Excel / CSV**
- **Flourish ( optional for visualization)**

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install pandas scholarly openpyxl
```

### 2. Add professor data

Update professors.xlsx with:
- Professor Name
- Google Scholar Profile ID

### 3. Run the script
```bash
python main.py
```

### 4. Use output
- The generated Excel/CSV file can be used for visualization (e.g Use Flourish for bar chart race animation across professors of some institution.)

## ⚠️ Notes & Limitations
- Google Scholar may rate-limit or block excessive requests
- A delay is intentionally added to reduce throttling
- Scraping Google Scholar should be done responsibly and ethically



