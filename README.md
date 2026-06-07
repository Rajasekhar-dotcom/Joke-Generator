# Joke Generator 🎭

A simple Python command-line application that fetches random jokes from the JokeAPI based on the user's preferred category.

## Features

* Fetches jokes from the JokeAPI.
* Supports multiple joke categories:

  * Programming
  * Misc
  * Pun
  * Spooky
  * Christmas
  * Any
  * Dark
* Handles invalid user input gracefully.
* Detects empty input and prompts the user accordingly.
* Includes basic network error handling.

## Technologies Used

* Python 3
* Requests Library
* JokeAPI

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/joke-generator.git
```

2. Navigate to the project directory:

```bash
cd joke-generator
```

3. Install the required dependency:

```bash
pip install requests
```

## Usage

Run the script:

```bash
python main.py
```

Example:

```text
Enter your preferred joke category(Programming/Misc/Pun/Spooky/Christmas/Any/Dark): Programming

Why do programmers prefer dark mode?
Because light attracts bugs.
```

## Project Structure

```text
joke-generator/
│
├── main.py
├── README.md
└── requirements.txt
```

## Error Handling

The application handles:

* Empty category input
* Invalid category names
* Network connection failures
* API request failures

## API Reference

This project uses the JokeAPI:

https://jokeapi.dev/

## Future Improvements

* Support for two-part jokes
* Random category selection
* Multiple jokes in a single request
* Graphical User Interface (GUI)
* Joke history feature

## License

This project is open source and available under the MIT License.

## Author

Rajasekhar

Built as a Python learning project to practice:

* API integration
* User input validation
* Exception handling
* Working with JSON responses
