# BRANDI Candidate Service

# What is it?

The candidate service is an API designed to manage candidate profile information and also exposes APIs for lookup
tables that will be used for candidates.

# What is required to use it?

## Tools that will be used

* Git
* Python 3.6
* OpenShift oc client
* Pipenv

The application is written in Python using Flask.  By default, when the application starts it will use a SQLite
database as a persistent storage.  Using environment variables, the application can be configured to connect to a
PostgreSQL database.

# How do I deploy or run it?

The application can be run locally or deployed into OpenShift.

First clone this repository.

```
git clone git@gitlab.agilesof.com:brandi-dev/brandi-candidate-service.git
```

## Deploy to OpenShift

Deployment to OpenShift can be performed using the infrastructure as code (IAC) configured in the .openshift-applier
in this repository.

Login to OpenShift using the oc client.  You can copy the login command from the OpenShift web console.  There is not a
way to login into OpenShift from the oc client as the cluster is currently configured.

Using the login command from the console, log in using the oc client.

```
oc login https://console.ocp-dev.agilesof.com:8443 --token=<your_token>
```

Enter the .openshift-applier directory

```
cd .openshift-applier
```

Install the Ansible Roles

```
ansible-galaxy install -r requirements.yml --roles-path=roles
```

Run the Ansible inventory

```
ansible-playbook apply.yml -i inventory/
```

This inventory will create all the OpenShift objects for the service and along with the PostgreSQL instance(s).

## Run Locally

The application can be run locally using SQLite or PostgreSQL.

First, create a virtual environment and install all dependencies.

```
# create virtual environment
pipenv shell
# install dependencies
pipenv sync
# install dev dependencies if you are running tests
pipenv install --dev
```

### Using SQLite

To run the application locally, run start in the root directory where you cloned the repository.  The one with the
Pipfile.

### Using PostgreSQL

In order for a PostgreSQL instance to be used, the following set of environment variables configured.

```
export DATABASE_SERVICE_NAME=BRANDI_CANDIDATE_SERVICE_POSTGRESQL
export DATABASE_ENGINE=postgresql
export DATABASE_NAME=brandidb
export DATABASE_USER=brandiuser
export DATABASE_PASSWORD=brandipassword
export BRANDI_CANDIDATE_SERVICE_POSTGRESQL_HOST=127.0.0.1
export BRANDI_CANDIDATE_SERVICE_POSTGRESQL_PORT_POSTGRESQL=5432
```
Then, run the application as you would for the SW

### Start the application

Start the application.

```
python wsgi.py
```

# How do I know it is working?

First, check the output on the console.  You should see something like the following:

```
 * Serving Flask app "app.server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## Test using Swagger UI

The Swagger UI is available as a web based interface that allows users to interact with the available endpoints.

You can access the Swagger UI, by entering the host of the application into your browser.

###  Locally

```
http://localhost:5000
```

### OpenShift Dev

```
http://brandi-candidate-service-brandi-dev.apps.ocp-dev.agilesof.com/
```

### OpenShift Test

```
http://brandi-candidate-service-brandi-test.apps.ocp-dev.agilesof.com/
```

### Available Endpoints

The current set of endpoints expose the CRUD operations for candidate, education_level, rank, and mos resources.

#### Candidate API

```
# Retrieve all candidate resources
GET    /candidates
# Create a new Candidate resource
POST   /candidates

# Retrieve the specified candidate resource by DOD ID
GET    /candidates/{dod_id}

# Update the specified candidate resource by DOD ID
PUT    /candidates/{dod_id}

# Remove the specified candidate resource by DOD ID
DELETE /candidates/{dod_id}
```

#### Education Level API

```
# Retrieve all education level resources
GET    /education_level
# Create a new education level resource
POST   /education_level

# Retrieve the specified education level resource by code
GET    /education_level/{code}

# Update the specified education level resource by code
PUT    /education_level/{code}

# Remove the specified education level resource by code
DELETE /education_level/{code}
```

#### Rank API

```
# Retrieve all rank resources
GET    /rank
# Create a new rank resource
POST   /rank

# Retrieve the specified rank resource by code
GET    /rank/{code}

# Update the specified rank resource by code
PUT    /rank/{code}

# Remove the specified rank resource by code
DELETE /rank/{code}
```

#### MOS API

```
# Retrieve all mos resources
GET    /mos
# Create a new mos resource
POST   /mos

# Retrieve the specified mos resource by code
GET    /mos/{code}

# Update the specified mos resource by code
PUT    /mos/{code}

# Remove the specified mos resource by code
DELETE /mos/{code}
```
