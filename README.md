# Project Setup Guide

Welcome to the project! Follow these steps to get everything set up and running smoothly.

---

## Prerequisites

Before starting, ensure that the following tools are installed on your system:

### 1. Pipenv

Pipenv is required to manage the virtual environment and dependencies.

**Installing Pipenv:**

```bash
pip install pipenv
```

Or, if you are using Python 3:

```bash
pip3 install pipenv
```

Verify the installation:

```bash
pipenv --version
```

---

### 2. Docker and Docker Desktop

Docker is required to set up the database. Ensure that Docker and Docker Desktop are installed and running.

Download Docker Desktop [here](https://www.docker.com/products/docker-desktop/).

Verify Docker installation:

```bash
docker --version
docker-compose --version
```

---

## Project Setup

Follow these steps to set up the project environment.

### 1. Create the Pipenv Environment

Once Pipenv is installed, create the virtual environment and install the dependencies:

```bash
pipenv install -r requirements.txt
```

*Note: If the above command doesn’t work, use the following alternative (this method works for me):*

```bash
pipenv lock
pipenv install
```

---

### 2. Activate the Pipenv Shell

After installing the dependencies, start the Pipenv shell:

```bash
pipenv shell
```

---

### 3. Set up the Database

Before starting the application, the database must be set up.

Navigate to the `Database` folder:

```bash
cd Database
```

Run the Docker Compose command to start the database container:

```bash
docker-compose up -d
```

---

### 4. Run the Application

Once the database is running, navigate back to the root directory and start the application:

```bash
python run.py
```

---

## Final Steps

The application should now be running smoothly. If you encounter any issues, please reach out for support.

---

