#!/usr/bin/env python3

import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()

AUTHOR_PAGE_URL = os.environ.get('AUTHOR_PAGE')


def send_email(message):
    is_send = False
    message = Mail(
        from_email=os.environ.get('FROM_EMAIL'),
        to_emails=os.environ.get('SEND_EMAIL_TO'),
        subject=os.environ.get('EMAIL_SUBJECT'),
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        if response.status_code == 202:
            is_send = True
    except Exception as e:
        print(e.message)

    return is_send


def send_notification(sales_count):
    message = "<br/>Dear Admin<br/><br/>New Customer just purchased item, \
    Your sale increased to <strong>{}</strong>,\
    have a look at {} .<br/><br/><br/>Thank you" . format(sales_count, AUTHOR_PAGE_URL)
    send_email(message)


def update_sales_count(new_sale):
    sales_file = open(os.environ.get('SALES_COUNT_FILE_NAME'), "w")
    sales_file.write(str(new_sale))
    sales_file.close()


def get_previous_sale_count():
    sales_count=0
    if os.path.isfile(os.environ.get('SALES_COUNT_FILE_NAME')):
        sales_file = open(os.environ.get('SALES_COUNT_FILE_NAME'), "r")
        sales_count = sales_file.read()
    else:
        update_sales_count("0")
    return sales_count


def get_sales_count(html):
    previous_sale_count = get_previous_sale_count()
    soup = BeautifulSoup(html, 'html.parser')
    stats = soup.find_all("div", {"class": "user-info-header__stats-content"})[1].find("strong")
    if stats is not None:
        sales_number = stats.text.strip()
        if sales_number != '':
            if os.environ.get('NOTIFY_ONLY_NEW_SALE') == 0:
                send_notification(sales_number)
            else:
                if previous_sale_count != sales_number:
                    update_sales_count(sales_number)
                    send_notification(sales_number)
                else:
                    print("No new sales, will check again later.")
    else:
        print("Could not extract")


# start
def main():
    page = requests.get(AUTHOR_PAGE_URL)
    if page.status_code == 200:
        get_sales_count(page.text)


if __name__ == "__main__":
    main()

