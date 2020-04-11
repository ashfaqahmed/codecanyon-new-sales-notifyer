# Codecanyon Sales Email Notifyer
Simple Python3 script to get notifications by email for any new sales made on author page at codecanyon

### Requirements

- Sendgrid API key (to send email)
- Python3

### Installation 

```
pip install requests 
pip install sendgrid 
pip install python-dotenv 
pip install beautifulsoup4
```

### Update .env config 

```
# your sendgrid API with permission send email
SENDGRID_API_KEY=''

# from email address, subject line and notification receiver email

FROM_EMAIL='info@ashfaqsolangi.com'
EMAIL_SUBJECT='Codecanyon Sales Notifcation'
SEND_EMAIL_TO='ashfaqsolangi@gmail.com'

# 0 to receive daily notifications (time is based on the cron-job you will set)
# 1 to receive only when there is new sale
NOTIFY_ONLY_NEW_SALE=1


# file name to store fetched sale number only
SALES_COUNT_FILE_NAME='sales_count.txt'

# Codecanyon Author page url (author username)
AUTHOR_PAGE = 'https://codecanyon.net/user/autho_user_name'
```

### Run script 

```
python notify.py 
```

#### Add to cron job 

Make the script executable by:
```
chmod u+x /path/to/notify.py 
```
