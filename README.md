# **Rememby Bot**

**Rememby Bot** is a Telegram bot designed to help you create, manage, and track reminders. It uses FastAPI as the backend framework and APScheduler for task scheduling.

---

## **Features**
- Create reminders with `/remind <message> <YYYY-MM-DD:HH:MM>` format.
- Automatically schedules reminders and notifies you via Telegram.
- Persistent data storage using SQLite.

---

## **Prerequisites**
To set up and run this project locally, ensure you have the following installed:
1. Python 3.8+ (compatible with `python-telegram-bot` and `FastAPI`).
2. Pipenv or virtualenv (recommended for virtual environment management).
3. `ngrok` or an alternative tunneling service for webhook testing.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/SaulEiros/Rememby.git
cd Rememby
```

### **Step 2: Create and Activate a Virtual Environment**
Using `venv`:
```bash
python3 -m venv rememby_env
source rememby_env/bin/activate  # On Windows, use `rememby_env\Scripts\activate`
```

### **Step 3: Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Environment Variables**
1. Open the `.env` file in the project root.
2. Add your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

In order to get a bot token, you need to follow this [guide](https://github.com/SaulEiros/Rememby.git). 

### **Step 5: Initialize the Database**
1. Ensure SQLite is installed (it comes pre-installed with Python).
2. Ensure you have the `data` folder in the project root. A file named `reminders.db` should be inside that folder.
3. Run the database initialization script:
   ```bash
   python app/database.py
   ```
   This script will create the necessary tables in the SQLite database.

For ensure the status of this step, you can run the script `database.py` for check that the tables are created.

### **Step 6: Run the Application**
Start the FastAPI server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 5001
```

### **Step 7: Expose Localhost for Webhooks**
Use Cloudflare Tunnel to expose your local server to the internet:
1. Install Cloudflare Tunnel:
   ```bash
   brew install cloudflared  # macOS
   sudo apt install cloudflared  # Ubuntu
   ```

2. Run the Cloudflare Tunnel command:
   ```bash
   cloudflared tunnel --url http://localhost:5001
   ```

3. Note the public URL provided by Cloudflare (e.g., `https://your-cloudflare-url`).

---

## **Configure Telegram Webhook**
In the `utils` folder, there is a script called `webhook.py` that automates setting up and verifying your Telegram bot's webhook.

#### **`utils/webhook.py`**
The script performs the following:
1. Sets your bot's webhook to the public URL provided by Cloudflare.
2. Verifies the webhook setup by fetching the current webhook info.

#### **Usage**
1. Replace `YOUR_TELEGRAM_TOKEN` in the script with your actual bot token.
2. Replace `YOUR_PUBLIC_URL` with the public URL from Cloudflare Tunnel.
3. Run the script:
   ```bash
   python utils/webhook.py
   ```
4. The script will output the result of the webhook setup and its current status.

---

## **Testing the Bot**
1. Open Telegram and search for your bot using its name or username.
2. Test the `/remind` command:
   ```plaintext
   /remind "Buy groceries" 2025-01-26:15:00
   ```
3. Confirm that the bot schedules the reminder and sends you a message at the specified time.

---

## **Project Structure**
```
rememby/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point for the FastAPI server
│   ├── database.py             # SQLite database initialization and connection
│   ├── scheduler.py            # APScheduler configuration
│   ├── handlers/               # Telegram command handlers
│       ├── __init__.py
│       ├── start_handler.py    # /start command
│       ├── remind_handler.py   # /remind command
│       ├── help_handler.py     # /help command
├── data/
│   ├── reminders.db            # SQLite folder
├── utils/
│   ├── database.py             # Script for checking database integrity
│   ├── webhook.py              # Script for setting up Telegram webhook
├── .env                        # Environment variables
├── .gitignore                  # Git exclusions file
├── requirements.txt            # Python dependencies
├── LICENSE                     # Project License
└── README.md                   # Project documentation
```

---

## **Contributing**
Feel free to contribute to this project! Please fork the repository, make your changes, and submit a pull request.

---

## **License**
This project is licensed under the APACHE 2.0 License. See the LICENSE file for details.

---

## **Support**
If you encounter any issues, please open an issue on the [GitHub repository](https://github.com/SaulEiros/Rememby/issues).
