---

# 🚀 Social Network Friend Graph API

## 📘 Overview

Welcome to the **Social Network Friend Graph API**, a lightweight and efficient backend service built using **FastAPI**, **Neo4j**, and **Docker Compose**. This project models a social graph where users can connect with each other, manage friendships, and explore their social network dynamically.

## 🧩 Tech Stack

* ⚡ **FastAPI** – High-performance Python web framework for APIs.
* 🌐 **Neo4j** – Native graph database designed for connected data.
* 🐳 **Docker Compose** – Container orchestration to simplify local development.

## 🎯 Core Features

### 👤 User Management

* Add new users to the network with unique identifiers.
* Automatically initialize user nodes in the Neo4j graph.

### 🤝 Friendships

* Create bi-directional friendships between two users.
* Prevent duplicate or invalid connections.
* Support unidirectional/optional relationships for future scalability.

### 📜 Friends List

* Retrieve a complete list of a user's friends.
* Returns structured data to easily integrate with frontends or other services.

### 🧑‍🤝‍🧑 Mutual Friends

* Query mutual friends between two users.
* Useful for social recommendations, trust metrics, or gamification.

## 🚀 How to Run

1. Clone the repository 📁

2. Set up your environment variables in a `.env` file 🔐

3. Build and start the services with:

   ```bash
   docker-compose up --build
   ```

4. Access the API at: [http://localhost:8000/docs](http://localhost:8000/docs) 🌐

## 📦 Project Structure

* `app/` – FastAPI source code and logic
* `neo4j/` – Graph data and configurations
* `Dockerfile` – API container setup
* `docker-compose.yml` – Service orchestration
* `.env` – Environment configuration (excluded from version control)

## ✅ Production Considerations

* Secure environment variables using Docker secrets or cloud-based key stores 🔐
* Implement rate limiting and authentication for public APIs 🔐
* Add persistent volume backups for Neo4j data 💾
* Use health checks and logging for monitoring and observability 📈

## 🧠 Ideal Use Cases

* Friend suggestion systems
* Social graph analytics
* Trust and influence modeling
* Lightweight social networking prototypes

---
