# Challenge Banza

This is the repository where the solution to the Banza challenge is hosted.

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋

What things you need to install the bot and how to install them
1. Download and install Python 3. You can download from https://www.python.org/downloads/

2. Create an enviorment to run the script properly

    ```
    python -m venv /path/to/new/virtual/environment
    ```
    Then, activate it:
    ```
    path_env\venv\Scripts\activate
    ```    
3. You have to install dependencies that ```requirements.txt``` contains.

    ```
    pip install -r requirements.txt
    ```

4. Create a copy of your .env file

    ```
    cp .default.env .env
    ```
5. Config your .env 
    ```
    USER=user
    PASSWORD=pwd
    HOSTNAME=localhost
    PORT=5432
    DB_NAME=instituciones
    ```

## Setting up database 🛠️
In this project I used PostgreSQL, you can download it from here: https://www.postgresql.org/download/

You don't have to create the tables from scratch, you will create it automatically in the script service.py using SQLService.

```
python service.py
```

### Running API ⚙️
You have to run in your terminal:
```
uvicorn app:app --reload
```
And then the API is available


## Running tests ⚙️

This project use pytest and unnitest library.

```
pytest
```

## ToDo 📖

- Add corresponding tests for missing endpoints
- Improve folder structure
- Refactor routes.py and separate logic
- Better understand, study and review the concept of testing and the use of mocks.
- Use of database in memory for tests.
- Add get_total method.

## Built With 🛠️

- [requests](https://docs.python-requests.org/en/latest/) - Requests is a simple, yet elegant, HTTP library.
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper.
- [FastAPI](https://github.com/tiangolo/fastapi) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [python-decouple](https://github.com/henriquebastos/python-decouple/) - Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.
## Author ✒️

- **Nicolás Liendro** - _Initial work_ - [GitLab](https://gitlab.com/NicoLiendro14),
  [GitHub](https://github.com/NicoLiendro14), and
  [LinkedIn](https://www.linkedin.com/in/nicolas-liendro/)