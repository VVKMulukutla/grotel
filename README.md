# Telegram Groq Bot

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)

This project is a Telegram chatbot that integrates with Groq Inc's cloud API to provide inference results based on user inputs. The bot interacts with users, allowing them to choose from various models and input their data to get predictions or insights from the selected model.

## Features

- **Model Selection**: Users can choose from multiple models such as `Gemma-7b-it`, `Llama3-8b`, `Mixtral-8x7B`, and `Llama3-70B`.
- **Dynamic Inference**: After selecting a model, users can input their data, and the bot fetches the inference result from Groq Inc's API.
- **User-Friendly Interaction**: Simple and intuitive conversation flow with Telegram bot commands.


## Getting Started

Follow these instructions to set up and run the bot on your local machine.

### Prerequisites

- Python 3.8 or higher
- A Telegram bot token from BotFather
- A Groq API key

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/vvkmulukutla/grotel.git
   cd grotel
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create and configure the `.env` file:**

   ```plaintext
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GROQ_API_KEY=your_groq_api_key
   ```

### Running the Bot

Start the bot by running the following command:

```sh
python -m bot.main
```

### Usage

Once the bot is running, you can interact with it on Telegram:

- **/start**: Initiate the bot and choose a model.
- **Model Selection**: Choose from `Gemma-7b-it`, `Llama3-8b`, `Mixtral-8x7B`, and `Llama3-70B`.
- **Input Data**: Enter the data for which you need the inference.
- **Receive Results**: Get the inference result from the selected model.

## Contributing

We welcome contributions to enhance this project. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Python Telegram Bot](https://python-telegram-bot.org/)
- [Groq Inc](https://groq.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

Feel free to customize this `README.md` to better fit your project's specifics. This file aims to provide a clear and comprehensive guide to users and contributors.
```