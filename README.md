# 🧮 Microservices-Based Calculator

## 📌 Overview
This project is a **microservices-based calculator application** using **Docker and Docker Compose**. It features a **Flask-based web frontend**, a **Celery worker for asynchronous computations**, and a **PostgreSQL database** for storing calculations. The system is fully containerized for easy deployment and scalability.

## ✨ Features
✔️ **Interactive Calculator UI** with real-time results  
✔️ **Backend stores calculations** in PostgreSQL  
✔️ **Asynchronous computation** using Celery  
✔️ **Persistent database storage** with Docker volumes  
✔️ **Dockerized microservices** for efficient scalability  

## 🛠️ Tech Stack
- **Frontend:** Flask + HTML/CSS/JavaScript
- **Backend:** Flask (Python)
- **Worker Service:** Celery (Python) + Redis
- **Database:** PostgreSQL
- **Message Broker:** Redis
- **Containerization:** Docker, Docker Compose

## 📂 Project Structure
```
microservices-app/
│── web/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   ├── requirements.txt
│   ├── Dockerfile
│── worker/
│   ├── worker.py
│   ├── requirements.txt
│   ├── Dockerfile
│── docker-compose.yml
│── README.md
```

## 🚀 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Harshtherocking/calculator.git
cd calculator
```

### 2️⃣ Build and Start Services
```sh
docker-compose up --build -d
```

### 3️⃣ Verify Running Containers
```sh
docker ps
```

### 4️⃣ Access the Web Application
<!-- Open [http://localhost:8080](http://localhost:8080) in your browser. -->
Open [http://localhost:8080](http://172.19.0.5:8081/) in your browser.

### 5️⃣ Check Service Logs
```sh
docker logs 2022BCD0044-web
docker logs 2022BCD0044-worker
```

### 6️⃣ Run a Celery Task Manually
```sh
docker exec -it 2022BCD0044-worker python -c "from worker import add_task; print(add_task.delay('5+3*2').get())"
```

## 🔗 API Endpoints
### **📍 GET / (Homepage)**
Displays the calculator UI.

### **📍 POST /calculate**
Processes the given mathematical expression and returns the result.
#### Request Body (JSON):
```json
{
  "expression": "5+3*2"
}
```
#### Response (JSON):
```json
{
  "expression": "5+3*2",
  "result": 11
}
```

### **📍 GET /history**
Retrieves the last 10 stored calculations.
#### Response (JSON):
```json
[
  ["5+3*2", 11],
  ["10/2", 5]
]
```

## ⚠️ Important Notes
- The backend currently uses **Python's `eval()` function**, which is not secure for user input. In production, consider using a safer expression evaluation method.
- PostgreSQL ensures **data persistence** across container restarts.
- Redis is used as a **message broker** for Celery workers.

### 👨‍💻 Developed by **Harsh Chauhan** (Roll No: **2022BCD0044**)
![image](./Screenshot%20from%202025-02-24%2001-20-05.png)

