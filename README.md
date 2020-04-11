# Codecanyon Sales Email Notifyer
Simple Python3 script to get notifications by email for any new sales made on your codecanyon account.

I built this for personal use because i never got any new sales notification by codecanyon, i am not sure why but i have 3 accounts and i never received any sales email from them.

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

FROM_EMAIL='info@mydomain.com'
EMAIL_SUBJECT='Codecanyon Sales Notifcation'
SEND_EMAIL_TO='myemail@mydomain.com'

# 0 to receive daily notifications (time is based on the cron-job you will set)
# 1 to receive only when there is new sale
NOTIFY_ONLY_NEW_SALE=1


# file name to store fetched sale number only
SALES_COUNT_FILE_NAME='sales_count.txt'

# Codecanyon Author page url (author username)
AUTHOR_PAGE = 'https://codecanyon.net/user/author_user_name'
```

### Run script 

```
python notify.py 
```

### Add cron job on server

Make the script executable by:
```
chmod u+x /path/to/notify.py 
```
Open your cron table by:
```
crontab -e 
```
Add the following cron entry: (24 hours)
```
0 */24 * * * /path/to/notify.py 
```

That's it :)