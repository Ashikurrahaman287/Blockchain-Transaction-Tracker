# Telegram Blockchain Transaction Tracker

This Telegram Bot notifies users about new transactions on the Binance Smart Chain (BSC) network for specified wallet addresses.

## Features

- Allows users to set their BSC wallet addresses to receive transaction notifications.
- Checks for new transactions on the specified wallet addresses periodically.
- Sends notifications to users via Telegram whenever a transaction above a certain threshold is detected.

## Usage

1. **Set Up Telegram Bot**:
   - Create a new Telegram bot using [BotFather](https://core.telegram.org/bots#6-botfather).
   - Copy the token provided by BotFather and replace the `TOKEN` variable in the code with your bot token.

2. **Set Up BscScan API Key**:
   - Obtain an API key from [BscScan](https://bscscan.com/myapikey).
   - Replace the `API_KEY` variable in the code with your API key.

3. **Deploy the Bot**:
   - Deploy the code to a server or any hosting platform where Python scripts can run.
   - Ensure Python and necessary dependencies are installed on the server.

4. **Start the Bot**:
   - Run the `main()` function in the code to start the bot.
   - The bot will start polling for messages and checking transactions periodically.

5. **Interact with the Bot**:
   - Use the `/set <address>` command to set your BSC wallet address for receiving notifications.
   - The bot will notify you via Telegram whenever a transaction above a certain threshold is detected on your specified wallet address.

## Configuration

- `TOKEN`: Replace with your Telegram bot token obtained from BotFather.
- `API_KEY`: Replace with your BscScan API key obtained from BscScan.

## Dependencies

- `python-telegram-bot`: Python library for interacting with the Telegram Bot API.
- `requests`: Python library for making HTTP requests.

## Disclaimer

This project is provided as-is without any warranty. Use it at your own risk. The developers are not responsible for any misuse or damages caused by this software.
For Help! Ashik@spudblocks.com
