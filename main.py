import os
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from datetime import datetime

# Telegram Bot Token
TOKEN = "6463194081:AAGnNHX9S6Tlnc2sm4Prx9St-rZmOOsbTxk"

# BscScan API Key
API_KEY = "MINPWU6K928WSQI1HSVP7QPGMVC6C81FUQ"

# Dictionary to store user addresses
user_addresses = {}

# Function to set user address
def set_address(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.split()

    if len(text) < 2:
        update.message.reply_text("Please provide an address.")
        return

    address = text[1]

    user_addresses[chat_id] = address
    update.message.reply_text(f"Address {address} set successfully. You will receive notifications for transactions on this address.")

# Function to check for new transactions on all user's addresses
def check_transactions(context: CallbackContext):
    for chat_id, address in user_addresses.items():
        try:
            url = "https://api.bscscan.com/api"
            params = {
                "module": "account",
                "action": "txlist",
                "address": address,
                "apikey": API_KEY
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                transactions = data.get("result", [])

                for tx in transactions:
                    transaction_amount = int(tx["value"]) / 1e18  # Convert wei to BNB
                    if transaction_amount > 10000:  # Only notify for transactions above 10000 USDT
                        transaction_date = datetime.utcfromtimestamp(int(tx["timeStamp"])).strftime('%Y-%m-%d')
                        transaction_time = datetime.utcfromtimestamp(int(tx["timeStamp"])).strftime('%H:%M:%S')
                        sender_address = tx["from"]
                        receiver_address = tx["to"]
                        transaction_hash = tx["hash"]

                        transaction_link = f"https://bscscan.com/tx/{transaction_hash}"

                        message = f"Transaction amount: {transaction_amount} USDT\n"
                        message += f"Transaction date: {transaction_date}\n"
                        message += f"Transaction time: {transaction_time}\n"
                        message += f"Sender Address: {sender_address}\n"
                        message += f"Receiver Address: {receiver_address}\n"
                        message += f"Transaction Hash: {transaction_hash}\n"
                        message += f"Transaction Link: {transaction_link}"



                        context.bot.send_message(chat_id, message)
        except Exception as e:
            print(f"Error checking transactions: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("set", set_address))

    # Start checking for new transactions every 30 seconds
    updater.job_queue.run_repeating(check_transactions, interval=30, first=0)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
