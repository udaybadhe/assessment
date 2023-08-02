# Flask CRUD API with MongoDB

A Flask application that provides a RESTful API for performing CRUD operations on a User resource using a MongoDB database.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Technologies Used](#technologies-used)

## Description

This Flask application provides REST API endpoints to perform CRUD operations (Create, Read, Update, Delete) on a User resource. The application uses the PyMongo library to connect to a MongoDB database and interact with the User collection.

## Requirements

- Python 3.x
- Flask
- PyMongo
- python-dotenv

## Setup

1. Clone the repository:

```
git clone https://github.com/your-username/flask-mongodb-crud.git
cd flask-mongodb-crud
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a MongoDB database and collection for the application. Update the MongoDB URI and database name in the `.env` file (create one if not present):

```
MONGODB_URI=mongodb://your-mongodb-uri
DATABASE_NAME=your-database-name
```

5. Run the Flask application:

```
python app.py
```

## Usage

The Flask application will run locally at `http://localhost:5000/`. You can use tools like Postman or `curl` to interact with the REST API endpoints.

## Endpoints

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

## Technologies Used

- Flask
- PyMongo
- python-dotenv
