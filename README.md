# 🚀 Project Setup Guide

Welcome to the project! Follow these steps to get everything up and running smoothly. 

---

## 📋 Prerequisites

Before starting, make sure you have the following installed:

### 1️⃣ Pipenv

Pipenv is required to manage the virtual environment and dependencies.

✅ **Installing Pipenv:**

```bash
pip install pipenv
```

Or, if you are using Python 3:

```bash
pip3 install pipenv
```

👉 Verify the installation:

```bash
pipenv --version
```

---

### 2️⃣ Docker and Docker Desktop

Docker is required to set up the database. Ensure that Docker and Docker Desktop are installed and running.

🔗 [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

👉 Verify Docker installation:

```bash
docker --version
docker-compose --version
```

---

## ⚙️ Setting up the Project

### 1️⃣ Create the Pipenv Environment

Once Pipenv is installed, the first step is to create the virtual environment and install the dependencies.

```bash
pipenv install -r requirements.txt
```

⚠️ *Note: If the above command doesn’t work, use the following instead (this works for me):*

```bash
pipenv lock
pipenv install
```

---

### 2️⃣ Activate the Pipenv Shell

After installing the dependencies, start the Pipenv shell:

```bash
pipenv shell
```

---

### 3️⃣ Set up the Database

Before starting the app, the database must be set up.

📁 Navigate to the `Database` folder:

```bash
cd Database
```

▶️ Run the Docker Compose command to start the database container:

```bash
docker-compose up -d
```

---

### 4️⃣ Run the Application

Once the database is running, navigate back to the root directory and start the application:

```bash
python run.py
```

---

## 🎉 You're all set!

The application should now be running smoothly. Let me know if you encounter any issues!

---

