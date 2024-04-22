
# Todos

A basic todos app for backend cohort 1


## Run Locally

Clone the project

```bash
  git clone https://github.com/backendtechwitclan/todos.git
```

Go to the project directory

```bash
  cd todos
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## URL Routes

#### Get all todos

```http
  GET /
```
Get all todos in the application

#### Login

```http
  POST /auth/login/
```
Login user to the application

#### Register

```http
  POST /auth/register/
```
Register a user to the application

#### Get user todos

```http
  GET /todos/
```
Get the todos belonging to the logged in user

#### Mark Todo as read

```http
  GET /todos/${id}/mark/
```
Mark a todo as read

#### Create Todo

```http
  POST /todos/create/
```
Create a todo for a user account


### The Demo Routes

#### Create Teacher
```http
  POST /create-teacher/
```
Create a teacher entry

#### View all Teacher
```http
  POST /view-teachers/
```
View all the teachers in the application


## Features

- Creating Todos
- Adding Todo
- Marking Todos as read
- View Todos
- Login User
- Register User

