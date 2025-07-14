
# Python_CLI_TODO_APP

Python_CLI_TODO_APP is a command-line todo list application built with Python, [Typer](https://typer.tiangolo.com/), and [Rich](https://rich.readthedocs.io/). It allows you to add, update, complete, delete, and view tasks, with colored categories and persistent storage using SQLite. Perfect for managing your tasks directly from the terminal!

## Features
- Add tasks with categories
- Update existing tasks
- Mark tasks as complete
- Delete tasks
- View your todo list in a beautiful table with colored categories
- Persistent storage using SQLite

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Jayesh-Kamble/Python_CLI_TODO_APP.git
   cd Python_CLI_TODO_APP
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install typer rich
   ```

## Usage
Run the CLI app using Python:
```sh
python todocli.py [COMMAND] [OPTIONS]
```

### Example Commands
- Add a task:
  ```sh
  python todocli.py add "Read a book" "Reading"
  ```
- Show all tasks:
  ```sh
  python todocli.py show
  ```
- Mark a task as complete:
  ```sh
  python todocli.py complete 1
  ```
- Update a task:
  ```sh
  python todocli.py update 1 --task "Write notes" --category "Writing"
  ```
- Delete a task:
  ```sh
  python todocli.py delete 1
  ```

## Project Structure
```
Python_CLI_TODO_APP/
├── todocli.py      # Main CLI application
├── model.py        # Todo model class
├── database.py     # Database operations
├── todos.db        # SQLite database file
├── README.md       # Project documentation
└── ...
```

## License
This project is licensed under the MIT License.

---

Made with ❤️ using Python, Typer, and Rich.
