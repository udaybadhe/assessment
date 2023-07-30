```markdown
# Flask CRUD with MongoDB REST API

This is a Flask application that provides REST API endpoints for performing CRUD (Create, Read, Update, Delete) operations on a User resource stored in a MongoDB database.

## Requirements

- Python 3.x
- Flask
- PyMongo
- dotenv

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-mongodb-crud.git
cd flask-mongodb-crud
```

2. Create a new Python virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and define the following environment variables:

```plaintext
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=your-database-name
```

Replace `your-database-name` with the name of your MongoDB database.

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. The API endpoints will be accessible at `http://localhost:5000/`.

## API Endpoints

### GET /users

Returns a list of all users.

### GET /users/<id>

Returns the user with the specified ID.

### POST /users

Creates a new user with the specified data.

### PUT /users/<id>

Updates the user with the specified ID with the new data.

### DELETE /users/<id>

Deletes the user with the specified ID.

## Examples (using cURL)

1. Get all users:

```bash
curl -X GET http://localhost:5000/users
```

2. Get a specific user (replace `<id>` with the user ID):

```bash
curl -X GET http://localhost:5000/users/<id>
```

3. Create a new user:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}' http://localhost:5000/users
```

4. Update a user (replace `<id>` with the user ID):

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "New Name"}' http://localhost:5000/users/<id>
```

5. Delete a user (replace `<id>` with the user ID):

```bash
curl -X DELETE http://localhost:5000/users/<id>
```