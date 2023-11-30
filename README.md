# Athena API Spec Scraper

![Athena Scraper Logo](https://github.com/reedtechus/.github/assets/77644584/16fb5f87-ae8f-4956-8cea-490312c427d0)

This is a simple script that scrapes the Athena API specs and generates a JSON file with each API spec.

## Usage

```bash
python3 main.py
```

## Output

This script will generate JSON files in the `output` directory.

The JSON files will be named `'category'/'endpoint'.json`.

## Dependencies

-   Python 3.10.12+
-   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [Requests](https://requests.readthedocs.io/en/master/)
-   [Selenium](https://selenium-python.readthedocs.io/)
-   [ChromeDriver](https://chromedriver.chromium.org/) - Tested in Ubuntu with Chromium
