# Pomodoro Bot

A simple Pomodoro timer bot to help you manage your work and break intervals efficiently. This project is designed for easy deployment and customization.

## Features
- Pomodoro timer with customizable work and break durations
- Docker support for containerized deployment
- Virtual environment support for Python dependencies
- Easy configuration via environment variables

## Getting Started

### Prerequisites
- Python 3.7+
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd pomodoro_bot
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
- Copy `.env.example` to `.env` and update the environment variables as needed.

### Usage
- Run the bot locally:
  ```bash
  python pomodoro_bot.py
  ```
- Or use Docker:
  ```bash
  docker build -t pomodoro-bot .
  docker run --env-file .env pomodoro-bot
  ```

## Project Structure
- `pomodoro_bot.py` - Main application file
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration
- `venv/` - Python virtual environment (should not be committed)
- `.env` - Environment variables (should not be committed)

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
