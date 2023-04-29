from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import lxml

obmen = int(input("Введите количество гривен для конвертации и нажмите ENTER: "))
counter = 0

def run(playwright):
    global obmen
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://bank.gov.ua/')
    soup = BeautifulSoup(page.content(),'lxml')
    value = float(soup.select('.value-full')[1].text.strip().replace(",", "."))
    result = (obmen / value)
    print(round(result, 2), 'долларов')

with sync_playwright() as playwright:
    run(playwright)