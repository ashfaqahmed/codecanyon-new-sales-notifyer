# Codecanyon Sales Email Notifier

A lightweight Python script that automatically notifies you via email when you make new sales on your Codecanyon account. This tool solves the common issue of not receiving timely sales notifications from Codecanyon.

## ✨ Features

- Real-time email notifications for new sales
- Configurable notification settings
- Daily sales summary option
- Simple setup and configuration
- Lightweight and efficient
- Works with any Codecanyon author account

## 🛠️ Requirements

- Python 3.x
- SendGrid API key (for sending emails)
- Codecanyon author account

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/codecanyon-new-sales-notifyer.git
cd codecanyon-new-sales-notifyer
```

2. Install required dependencies:
```bash
pip install requests sendgrid python-dotenv beautifulsoup4
```

## ⚙️ Configuration

Create a `.env` file in the project root with the following configuration:

```env
# SendGrid API key (with email sending permissions)
SENDGRID_API_KEY='your_sendgrid_api_key'

# Email configuration
FROM_EMAIL='your@email.com'
EMAIL_SUBJECT='Codecanyon Sales Notification'
SEND_EMAIL_TO='recipient@email.com'

# Notification settings
# 0 = Daily notifications (based on cron job timing)
# 1 = Only when new sales occur
NOTIFY_ONLY_NEW_SALE=1

# Storage configuration
SALES_COUNT_FILE_NAME='sales_count.txt'

# Your Codecanyon author page URL
AUTHOR_PAGE='https://codecanyon.net/user/your_username'
```

## 🚀 Usage

1. Test the script:
```bash
python notify.py
```

2. Set up automated checking using cron:
```bash
# Make the script executable
chmod u+x /path/to/notify.py

# Add to crontab (check every 24 hours)
0 */24 * * * /path/to/notify.py
```

## 🔧 How It Works

1. The script checks your Codecanyon author page for the current sales count
2. Compares it with the previously recorded count
3. Sends an email notification if new sales are detected
4. Updates the local sales count file

## 📝 Notes

- The script uses SendGrid for email delivery
- Sales count is stored locally in a text file
- You can configure the notification frequency through cron
- The script is lightweight and can run on any server

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ☕ Support My Work

If this tool saved you time or effort, consider buying me a coffee.  
Your support helps me keep building and maintaining open-source projects like this!

You can either scan the QR code below or click the link to tip me:

👉 [**buymeacoffee.com/ashfaqueali**](https://buymeacoffee.com/ashfaqueali)

<img src="https://ashfaqsolangi.com/images/bmc_qr.png" alt="Buy Me a Coffee QR" width="220" height="220" />