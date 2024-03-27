**Telegram Binance Smart Chain (BSC) Transaction Notifier**

This Telegram bot allows users to receive notifications for transactions on the Binance Smart Chain (BSC) that meet certain criteria. Users can set their BSC wallet addresses and receive notifications for transactions exceeding a specified threshold.

### Features

- **Set Address**: Users can set their BSC wallet address to receive notifications for transactions on that address.
- **Transaction Notifications**: Users receive notifications for transactions exceeding a specified threshold (currently set at 10,000 USDT).
- **Transaction Details**: Notifications include details such as transaction amount, date, time, sender and receiver addresses, transaction hash, and a link to the transaction on BscScan.

### Setup

1. **Telegram Bot Token**: Obtain a Telegram Bot Token by creating a new bot through BotFather on Telegram.
2. **BscScan API Key**: Obtain an API key from BscScan.
3. **Dependencies**: Install the required Python dependencies using pip:
   ```
   pip install python-telegram-bot requests
   ```
4. **Configuration**: Replace the placeholder tokens in the code with your Telegram Bot Token and BscScan API Key.
5. **Run**: Execute the script, and the bot will start checking for new transactions and sending notifications.

### Usage

- **Set Address**: Use the `/set <address>` command to set your BSC wallet address. Replace `<address>` with your actual BSC wallet address.
- **Receive Notifications**: Once the address is set, you will start receiving notifications for transactions exceeding the specified threshold.

### Contribution

Contributions to the project are welcome. Feel free to open issues, submit pull requests, or suggest improvements.


### Disclaimer

This project is for educational purposes only. Use it at your own risk. The developers are not responsible for any loss incurred due to the use of this bot.

### Acknowledgments

- This project utilizes the Telegram Bot API and BscScan API.
- Special thanks to the developers of python-telegram-bot and requests libraries.

### Authors

- [Your Name or Username](https://github.com/yourusername) - Initial work

### Contact

For any inquiries or feedback, please contact [Your Email Address].
