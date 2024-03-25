# GitHub Copilot API Server

This project is a FastAPI server that interacts with the GitHub Copilot API. It authenticates with GitHub and uses the access token to get code completions from GitHub Copilot.

## Technologies Used

- Python
- FastAPI
- HTTPX

## Getting Started

1. Clone the repository.
2. Install the dependencies with `pip install poetry && poetry install && poetry shell`.
3. Run the server with `python main.py`.

## API Endpoints

- `POST /copilot/completion/`: Get code completions from GitHub Copilot. The request body should contain a `prompt` and an optional `language` (default is "python").

## Environment Variables

- `GITHUB_CLIENT_ID`: Your GitHub client ID.
- `GITHUB_CLIENT_SECRET`: Your GitHub client secret.
- `GITHUB_REDIRECT_URI`: Your GitHub redirect URI.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.