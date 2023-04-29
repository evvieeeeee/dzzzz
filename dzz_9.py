from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

obmen = int(input("Введите количество гривен, которые нужно конвертировать, после нажмите Enter (ЦЕЛЬНЫЕ ЧИСЛА): "))
counter = 0
counter2 = 0

def run(playwright):
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://bank.gov.ua')

    soup = BeautifulSoup(page.content(), 'lxml')
    value = float(soup.select('.value-full')[1].text.strip().replace(",", "."))
    result = (obmen / value)
    print(round(result, 2))
    #for dollar in soup.select('.value-full '):
        #global counter
        #global counter2

        #if counter == 0:
            #print("1. Количество Евро (ОКРУГЛЕНО ДО СОТЫХ):")
        #if counter2 == 1:
            #print("2. Количество Долларов США (ОКРУГЛЕНО ДО СОТЫХ):")
        #value = dollar.select_one('small').text
        #value = value.replace(",", ".")
        #value2 = float(value)
        #result = (obmen / value2)
        #print(round(result, 2))
        #counter += 1
        #counter2 += 1

with sync_playwright() as playwright:
    run(playwright)