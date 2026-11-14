# playing-with-data - Data Manipulation with Python

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://playing-with-data.streamlit.app/)
[![CI](https://github.com/arunangshu01/playing-with-data/actions/workflows/ci.yml/badge.svg)](https://github.com/arunangshu01/playing-with-data/actions/workflows/ci.yml)

**Live demo:** https://playing-with-data.streamlit.app/

This repository contains code samples for playing with data from JSON files, CSV files, and Excel files using **NumPy** and **Pandas** in Python. The provided scripts demonstrate various techniques for loading, processing, and analyzing data using these powerful libraries.

## Contents

- **JSON Data Handling**: Examples of reading, writing, and manipulating JSON files.
- **CSV Data Handling**: Examples of working with CSV files, including reading, writing, and processing data.
- **Excel Data Handling**: Examples of reading, writing, and manipulating Excel files.

## Requirements

To run the code samples in this repository, you need to have Python installed along with the following libraries:

- NumPy
- Pandas 
- openpyxl (for reading Excel files)
- Streamlit (for the interactive demo)

1. You can install the required packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/arunangshu01/playing-with-data.git
   ```

2. **Navigate to the cloned repository:**
   ```sh
   cd playing-with-data
   ```

3. **Run any of the scripts** (they can be run from any directory):
   ```sh
   python source/data_playing/csv_to_dataframe.py
   ```

4. **Explore the folders and files to find the tutorials and solutions you are interested in.**

## Interactive Demo

`streamlit_app.py` walks through each pipeline step by step, showing the pandas code next to the resulting DataFrame, plus an explorer for custom group-by aggregations.

Try it online at **https://playing-with-data.streamlit.app/**, or run it locally:

```sh
streamlit run streamlit_app.py
```

## Testing

```sh
pip install -r requirements-dev.txt
pytest
```

GitHub Actions (`.github/workflows/ci.yml`) runs the tests and a boot check of the Streamlit app on every push and pull request to `main`. The app is hosted on Streamlit Community Cloud, which redeploys automatically whenever `main` changes.

### Contributing

If you would like to contribute to this repository, feel free to fork the repository and submit a pull request. Your contributions are always welcome!

### Let's Connect

If you have any questions or suggestions, feel free to reach out!

- 📧 **Email:** arunangshu01@gmail.com
- 🔗 [**LinkedIn**](https://www.linkedin.com/in/arunangshu-pramanik-1896168b/)

---

Thank you for visiting my GitHub profile. Happy coding! 🚀

---

_Arunangshu Pramanik_
