# Discord Bot

A Discord bot built with Python using the discord.py library that provides various server management and entertainment features.

## Features

- **Music Playback**: Play music from URLs in voice channels
- **Message Management**: Clear messages from channels
- **Voice Channel Integration**: Join and interact with voice channels
- **User Moderation**: Kick members from the server
- **Help System**: Built-in help command to display all available commands

## Commands

| Command | Description |
|---------|-------------|
| `?` | Send a private message to the user |
| `!clear` | Clear all messages in the current channel |
| `!join` | Join the voice channel of the user who issued the command |
| `!play <url>` | Play music from the provided URL |
| `!kick <@member>` | Kick the mentioned member from the server |
| `!help` | Display all available commands |

## Requirements

- Python 3.8 or higher
- discord.py
- python-dotenv
- Flask (for keep_alive functionality)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Discord-Bot
   ```

2. Install dependencies:
   ```bash
   pip install discord.py python-dotenv flask
   ```

3. Create a `.env` file in the project root with your Discord bot token:
   ```
   TOKEN=your_discord_bot_token_here
   ```

## Usage

Run the bot with:
```bash
python main.py
```

## File Structure

- `main.py` - Main bot file containing all commands and event handlers
- `keep_alive.py` - Flask web server to keep the bot alive (for hosting on services like Replit)
- `README.md` - This file

## Configuration

Make sure to set the following in your Discord Developer Portal:
- Bot token (store in `.env` file)
- Required intents: Messages, Guilds, Voice States, Members
- Appropriate permissions for the server

## Author

MichaelChios
