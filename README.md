# IMeals App

## Description

IMeal is an APP  that allows customers to make food orders and helps food vendors know what the customers' orders and manage them. This project was done during the Moringa School Bootcamp MC31.


#### By **Rootkit**

### Technologies Used

- HTML
- CSS
- Scripts
- Python/Flask
- Virtualenv
- Github
- Heroku

## Features

Customers can;
* Sign up
* Login
* View a daily menu of meal options
* Place an order by selecting meal options

Administrators/Caterers can;
* Login
* Create, retrieve, update and delete meal options
* Setup daily menu
* View customer orders

## Installation

Run the following commands to have your project setup

Clone the repository

```sh
git clone https://github.com/Jpkat92/Book-A-Meal-Api.git
```

Change to project directory

```sh
cd Book-A-Meal-Api
```

Create and launch the virtual environment

```sh
virtualenv venv
Run 'source venv/bin/activate' on Linux or macOS
Run 'venv\Scripts\activate' on Windows
```

Install dependencies

```sh
pip install -r requirements.txt
```

## How to  run tests

Navigate to the `tests` directory

```sh
cd tests
```
Run the tests

```sh
pytest
```

## Link to live site
(https://imeals.herokuapp.com/)


### Setting up environment variables

Create a 'start.sh' file and paste the following where appropriate:

- `export SECRET_KEY='<secret_key>'`
- `export MAIL_USERNAME='<username>'`
- `export MAIL_PASSWORD='<password>'`
- `python3.8 manage.py server`



### Make the file executable

- `chmod a+x start.sh`

### Open the file in the terminal

- `./start.sh`


### Support and contact details
For any queries contact us on Github at:
@Abdihakim
@AbugaAroni
@J-Okoto
@kahenya-anita
@Thanos-11
### License
License MIT License

Copyright (c) [2020] [Rootkit]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2020 **Rootkit**
