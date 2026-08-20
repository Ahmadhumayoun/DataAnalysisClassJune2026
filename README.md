# Data Analysis Class — June 2026

A complete hands-on course for learning **Python for data analysis** — from the absolute basics to machine learning with scikit-learn. Every notebook is self-contained with rich explanations, examples, key takeaways, and practice exercises.

## Folder Structure

```
├── 01_Python_Fundamentals/          # Python basics: types, variables, loops, conditionals, strings, lists, dicts, functions
├── 02_NumPy_Fundamentals/           # NumPy arrays: creation, slicing, filtering, broadcasting, stats, random
├── 03_Pandas_Data_Analysis/         # Pandas: DataFrames, Excel/CSV I/O, filtering, grouping, vendor analysis
├── 04_File_Handling_and_IO/         # File I/O: read/write/append, JSON, CSV module, error handling, OS ops
├── 05_Web_Scraping/                 # Requests + BeautifulSoup: parsing, pagination, images, read_html
├── 06_Web_Automation/               # Selenium: browsers, waits, forms, a real game demo
├── 07_Scikit_Learn/                 # Machine learning: train/test split, linear regression, metrics
├── 08_Object_Oriented_Python/       # OOP: classes, constructors, inheritance, super(), a full Bank project
├── 09_Matplotlib_Visualization/     # Charts: line, bar, pie, subplots — plus common pitfalls
├── data/                            # Shared datasets used across exercises
└── README.md
```

## Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 1 | `01_Python_Fundamentals/01_Python_Fundamentals.ipynb` | Data types, variables, input, f-strings, operators, conditionals, string methods, loops, lists, dicts, tuples, sets, list comprehensions, functions |
| 2 | `02_NumPy_Fundamentals/02_NumPy_Fundamentals.ipynb` | Array creation, properties, reshape, slicing, broadcasting, filtering, statistics, random |
| 3 | `03_Pandas_Data_Analysis/01_Pandas_Fundamentals.ipynb` | Reading Excel/CSV, DataFrame exploration, filtering, missing data, sorting, grouping, price cleaning |
| 4 | `03_Pandas_Data_Analysis/02_Vendor_Products_Analysis.ipynb` | Real vendor analysis: 24,702 items, collection stats, top brands, price cleaning, export to Excel |
| 5 | `04_File_Handling_and_IO/04_File_Handling_and_IO.ipynb` | File read/write/append, JSON databases, CSV module, error handling, OS module, pathlib, user registration system |
| 6 | `05_Web_Scraping/01_Scraping_Fundamentals.ipynb` | HTTP + requests, BeautifulSoup parsing, countries table, pagination, `pd.read_html`, image scraping |
| 7 | `05_Web_Scraping/02_Scraping_Advanced.ipynb` | Guard-rails parsing, multi-page data combining, safe media downloads, error handling |
| 8 | `06_Web_Automation/01_Selenium_Automation.ipynb` | Browser automation: drivers, locating elements, forms, WebDriverWait, safe login, Cookie Clicker demo |
| 9 | `07_Scikit_Learn/01_ML_With_Scikit_Learn.ipynb` | ML workflow: split → train → predict → evaluate; linear regression, MSE/R², diabetes dataset |
| 10 | `08_Object_Oriented_Python/01_OOP_In_Python.ipynb` | Functions, classes, `__init__`, state, inheritance, multiple inheritance, overriding, `super()`, access modifiers, Bank project |
| 11 | `09_Matplotlib_Visualization/01_Matplotlib_Fundamentals.ipynb` | Line plots, bar charts, pie charts, subplot grids, legend/tight_layout pitfalls |

## Data Files

- `03_Pandas_Data_Analysis/` — VendorProducts.xlsx, AnalysedVendorProducts.xlsx, bank.csv, Questions.csv, StudentAgeData.xlsx/.csv, FetcheData.html
- `04_File_Handling_and_IO/` — introduction.txt, welcome.txt, UsersDatabase.txt, user.json, students.csv, pathlib_demo.txt
- `05_Web_Scraping/` — ScrapeThisSiteOffline.html, deskShopOffline.html, firstFile.html, htmlFiles/ (24 paginated pages), CountryData.xlsx, ScrappedImages/
- `data/` — industry.csv, Analysis.xlsx

## Scripts

- `01_Python_Fundamentals/If_Elif.py` — Conditionals: arithmetic calculator + coffee machine
- `01_Python_Fundamentals/StringFormatting.py` — f-string formatting with user input

## Getting Started

```bash
# 1. Install Python 3.10+
# 2. Install the libraries (some notebooks need a specific subset)
pip install numpy pandas matplotlib scikit-learn requests beautifulsoup4 selenium lxml openpyxl

# 3. Launch Jupyter
jupyter notebook
```

> **Tip:** notebooks 05 (Web Scraping) and 06 (Selenium) are designed to work offline too — fallback HTML files live inside their folders. Notebook 08's Bank project uses `03_Pandas_Data_Analysis/bank.csv`, so run notebooks in order.