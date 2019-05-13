API Employee

Access:
http://127.0.0.1:8000/department/
http://127.0.0.1:8000/employee/

Infos
- Create first a department (Post and Get only)
    {
        "id": 1,
        "name": "TI",
        "description": "Tecnology"
    }
- Create a employee
    {
        "first_name": "Bruno",
        "last_name": "Mzr",
        "email": "brunomzr@gmail.com",
        "department": 1
    }

Validation
    email -> Unique and valid
 
Tests - PyTest - 3 Tests (Create a department, employee and validate e-mail)
    magalu>python manage.py test

LOGs
 select * from easyaudit_crudevent;
 select * from easyaudit_requestevent;


# Teste_Python
API Employees

Django Coding Test
The purpose of this coding test is to evaluate your skills using Python and the Django web
framework.
The Problem
Company' team is growing every month and now we need to have some application to manage
employees' information, such as name, e-mail and department. As any application written at
Company, it must have an API to allow integrations.
Deliverables
"Company Employee Manager" app must have:
-> A Django Admin panel to manage employees' data
-> An API to list, add and remove employees.

API example (list)
Request
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
Response
JSON