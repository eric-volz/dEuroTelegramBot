


![Frankencoin Telegram Bot Logo](/media/frankencoin_telegram_bot_logo.png)

A Telegram bot for querying data about the Frankencoin project. 
This bot enables users to retrieve and monitor important information about the Frankencoin protocol directly 
through Telegram.

## ✨ Features

- 💹 Query current rates and statistics
- 📊 Monitor Frankencoin positions
- 🔔 Get notifications about important events


## 📋 Prerequisites

- 🐳 Docker
- 🔄 Docker Compose
- 🎫 Telegram Bot Token (from [@BotFather](https://t.me/botfather))

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/eric-volz/FrankencoinTelegramBot.git
cd FrankencoinTelegramBot
```

2. Create a `.env` file in the root directory:
```
TELEGRAM_TOKEN=your_bot_token_here
```

3. Start the bot with Docker Compose:
```bash
docker-compose up -d
```

## 🎮 Bot Commands

- `/start` - Launches the bot and displays a welcome message
- `/help` - Shows all available commands

## 💻 Development

### 📁 Project Structure

```
FrankencoinTelegramBot/
├── bot/
│   ├── buttons/
│   ├── config/
│   ├── logger/
│   ├── methods/
│   ├── app.py
│   ├── config.ini
│   ├── Dockerfile
│   └── frankencoin_telegram_bot.py
├── media/
├── .env
├── docker-compose.yml
└── README.md
```

### 🔧 Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the bot in development mode:
```bash
python3 bot/app.py dev
```

## ❗ Troubleshooting

**Problem**: Bot won't start
- ✅ Verify that TELEGRAM_TOKEN is correctly set in the .env file
- 📝 Check Docker container logs: `docker-compose logs`

**Problem**: No blockchain connection
- ✅ Ensure required blockchain nodes are accessible
- 🔍 Check network settings in Docker Compose configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔐 Security

- Never share your TELEGRAM_TOKEN
- Keep your environment variables secure
- Regularly update dependencies
- Monitor bot activity for unusual behavior

## 📚 Additional Resources

- [Frankencoin](https://frankencoin.com)
- [Frankencoin App](https://app.frankencoin.com)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Docker Documentation](https://docs.docker.com/)
