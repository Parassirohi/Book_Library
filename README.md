Book Collections Project
This is a Book Collections Project built with Django Rest Framework (DRF). The project allows users to create an account and login. Once authenticated, users can see a list of all books and the details of each book, including the availability status.

To get this repository, run the following command inside your git enabled terminal.
https://github.com/Parassirohi/Book_Library.git

To install all of the Python modules and packages used in this project, run the following command inside your terminal.
```pip install -r requirements.txt```

API Endpoints
The following API endpoints are available:

POST /auth/users/: Register a new user account
POST /auth/jwt/create/: Obtain a JWT token by providing a valid username and password
GET /library/books/: List all books
GET /library/books/pk/: Retrieve the details of a specific book by its primary key (pk)
Technologies Used
Django
Django Rest Framework (DRF)
PostgreSQL
Postman (for API testing)
HTML/CSS/JS (for frontend)
Getting Started
To get started with this project, follow these steps:

Clone this repository to your local machine.
Create a virtual environment and activate it.
Install the project dependencies using pip.
Apply database migrations using Django's manage.py command.
Generate fake data by running the generate_data.py script located in the books app.
Start the development server using Django's manage.py command.
Use Postman or your preferred HTTP client to interact with the API endpoints
