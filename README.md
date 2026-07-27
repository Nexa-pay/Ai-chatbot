# AAKASH AI Telegram Bot

A Telegram chatbot powered by **Ollama** and **Qwen 2.5 3B**.

## Features

- Telegram integration
- Local AI using Ollama
- Maximum 12-word replies
- Knowledge base support
- Easy deployment on a VPS

## Requirements

- Ubuntu VPS
- Python 3.10+
- Ollama
- qwen2.5:3b

## Install

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/telegram-ai-bot.git
cd telegram-ai-bot
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download the model:

```bash
ollama pull qwen2.5:3b
```

Set your Telegram bot token:

```bash
export BOT_TOKEN="YOUR_BOT_TOKEN"
```

Run the bot:

```bash
python3 bot.py
```

## Project Structure

```
telegram-ai-bot/
├── bot.py
├── ai.py
├── prompts.py
├── knowledge.txt
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## License

MIT
