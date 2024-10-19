# Flask CRUD App

This is a Flask application that manages user data using a REST API. It provides CRUD (Create, Read, Update, Delete) operations for users.

## Project Structure

```
flask-crud-app
├── app
│   ├── __init__.py
│   ├── controllers
│   │   └── user_controller.py
│   ├── services
│   │   └── user_service.py
│   ├── repositories
│   │   └── user_repository.py
│   ├── models
│   │   └── user.py
│   ├── config.py
│   ├── database.py
│   └── blueprints
│       └── user_blueprint.py
├── run.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/flask-crud-app.git
```

2. Navigate to the project directory:

```
cd flask-crud-app
```

3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Run the application:

```
python run.py
```

The application will be accessible at `http://localhost:5000`.

## API Endpoints

The following API endpoints are available:

- `GET /users`: Get a list of all users.
- `GET /users/{id}`: Get a specific user by ID.
- `POST /users`: Create a new user.
- `PUT /users/{id}`: Update an existing user.
- `DELETE /users/{id}`: Delete a user.

Please refer to the controller, service, and repository files for more details on the implementation of these endpoints.

## Database

This application uses SQLite as the database. The database connection details can be configured in the `config.py` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.