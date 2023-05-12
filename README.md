<h1 align="center">Book Collections Project</h1>
This is a Book Collections Project built with Django Rest Framework (DRF). The project allows users to create an account and login. Once authenticated, users can see a list of all books and the details of each book, including the availability status.

To get this repository, run the following command inside your git enabled terminal.
https://github.com/Parassirohi/Book_Library.git

To install all of the Python modules and packages used in this project, run the following command inside your terminal.
```pip install -r requirements.txt```

<h3 align="left">API Endpoints</h3>
The following API endpoints are available:

POST /auth/users/: Register a new user account <br>
POST /auth/jwt/create/: Obtain a JWT token by providing a valid username and password <br>
GET /library/books/: List all books <br>
GET /library/books/pk/: Retrieve the details of a specific book by its primary key (pk) <br>

<h3 align="left">Technologies Used</h3>
Django <br>
Django Rest Framework (DRF) <br>
Sqlite3 db <br>
Postman (for API testing) <br>
HTML/CSS/JS (for frontend)

<h3 align="left">Getting Started</h3>
To get started with this project, follow these steps: <br>
Clone this repository to your local machine. <br>
Create a virtual environment and activate it. <br>
Install the project dependencies using ```pip install -r requirements.txt```. <br>
Apply database migrations using ```python manage.py migrate```.<br>
Generate fake data by running the generate_data.py script located in the books app.<br>
Start the development server using ```python manage.py runserver```.<br>
Use Postman or your preferred HTTP client to interact with the API endpoints<br>
