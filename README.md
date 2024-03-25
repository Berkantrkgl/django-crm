# Django CRM Project

I created this Django project in line with the tasks given to me during my time at Loggma. Here, I first created a server with Classic Django and used Django Template Language for the UI. 
* Here I designed a customer tracking application. Admin users can open customer records, view these records and perform pagination. Here, input validations such as Regex are made during customer registration.
* The listing process of the entered customer records was done with Django pagination.
* A Django-rest-framework version of the application was later made. You can find this under the API directory.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, make sure you have the following prerequisites:

- [Python](https://www.python.org/downloads/) (version X.X)
- [Pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   $ git clone https://github.com/Berkantrkgl/django-crm.git
   $ cd django-crm
   $ python manage.py runserver
