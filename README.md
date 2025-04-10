# WA_Gov_Dep_API_Project
This is a RESTful API built using Flask to manage public services departments in Western Australia. 
It allows for the creation, retrieval, updating, and deletion of departments.

Project Structure

wa_public_services_api/
├── app/
│   ├── __init__.py         # Initialize the Flask app
│   ├── routes.py           # Define the API endpoints
│   ├── models.py           # Database models
│   ├── db.py               # Database setup and session management
├── run.py                  # Entry point to run the app
├── requirements.txt        # List of project dependencies
├── .gitignore              # Git ignore file for dependencies and virtual environment

Quick Start

1. Clone the Repository

To get started, clone this repository to your local machine:

git clone https://github.com/yourusername/wa_public_services_api.git
cd wa_public_services_api

2. Create a Virtual Environment (Optional but Recommended)

Create a Python virtual environment to manage dependencies:

python -m venv venv

Activate the virtual environment:
- Windows:
  venv\Scripts\activate
- macOS/Linux:
  source venv/bin/activate

3. Install Dependencies

Install the required Python packages using pip:

pip install -r requirements.txt

4. Run the Application

Once the dependencies are installed, you can start the Flask application:

python run.py

By default, the application will run at http://127.0.0.1:5000/.

API Endpoints

1. GET /departments

Retrieves a list of all departments.

- URL: /departments
- Method: GET
- Response:
  []

2. POST /departments

Creates a new department.

- URL: /departments
- Method: POST
- Body (JSON):
  {
    "name": "Department of Health",
    "location": "189 Royal St, Perth WA",
    "contact_email": "info@health.wa.gov.au"
  }
- Response:
  {
    "id": 1,
    "name": "Department of Health",
    "location": "189 Royal St, Perth WA",
    "contact_email": "info@health.wa.gov.au"
  }

3. GET /departments/{id}

Retrieves a specific department by its ID.

- URL: /departments/{id}
- Method: GET
- Response:
  {
    "id": 1,
    "name": "Department of Health",
    "location": "189 Royal St, Perth WA",
    "contact_email": "info@health.wa.gov.au"
  }

4. PUT /departments/{id}

Updates a specific department by its ID.

- URL: /departments/{id}
- Method: PUT
- Body (JSON):
  {
    "name": "Department of Health and Wellness",
    "location": "200 Royal St, Perth WA",
    "contact_email": "contact@health.wa.gov.au"
  }
- Response:
  {
    "id": 1,
    "name": "Department of Health and Wellness",
    "location": "200 Royal St, Perth WA",
    "contact_email": "contact@health.wa.gov.au"
  }

5. DELETE /departments/{id}

Deletes a department by its ID.

- URL: /departments/{id}
- Method: DELETE
- Response:
  - Status Code: 204 No Content
  - Response Body: Empty

Project Setup and Configuration

1. Database Configuration

This project uses SQLite as the database, and it is configured to use a file-based database called services.db. The database is created and tables are initialized automatically when you run the app.

Dependencies

The following libraries are used in this project:

- Flask: A lightweight web framework for building web applications.
- Flask-SQLAlchemy: Extension for Flask that adds support for SQLAlchemy.
- SQLAlchemy: ORM for interacting with the database.

To install the dependencies, you can use the following command:

pip install -r requirements.txt

requirements.txt contents:

Flask==2.2.3
Flask-SQLAlchemy==3.0.0

Running Tests (Optional)

You can use Postman or curl to test the endpoints mentioned in the API section. Below is an example of using curl for the GET request:

curl http://127.0.0.1:5000/departments

Running the App

To run the Flask app, use the following command:

python run.py

Future Enhancements

- Add authentication and authorization (JWT tokens or OAuth).
- Implement advanced filtering, sorting, and pagination for the GET endpoint.
- Integrate with a cloud-based database like AWS RDS or Azure SQL Database for production.

Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

