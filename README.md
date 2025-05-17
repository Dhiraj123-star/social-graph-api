
---

# 🚀 Social Network Friend Graph API

## 📘 Overview

The **Social Network Friend Graph API** is a scalable backend service built with **FastAPI**, **Neo4j**, and **Docker Compose**. It models social relationships, allowing users to create friendships, list friends, and find mutual friends efficiently using graph database capabilities.

## 🧩 Tech Stack

- ⚡ **FastAPI** – Modern, fast Python web framework.
- 🌐 **Neo4j** – Graph database optimized for connected data.
- 🐳 **Docker Compose** – Simplifies local development and deployment.
- 🔐 **python-dotenv** – Securely manage environment variables.
- 🖋️ **Black & Flake8** – Code formatting and linting for quality.
- ⚙️ **GitHub Actions** – Automated lint checks and Docker image deployment to DockerHub.

## 🎯 Features

### 👤 User Management

- Add new users with unique IDs.
- Create corresponding user nodes in Neo4j automatically.

### 🤝 Friendships

- Establish bi-directional friendships between users.
- Prevent duplicates and invalid relations.
- Support flexibility for future enhancements.

### 📜 Friends Listing

- Fetch a user’s complete list of friends.
- Provide structured responses for easy integration.

### 🧑‍🤝‍🧑 Mutual Friends

- Query mutual friends between any two users.
- Enables social recommendations and trust calculations.

## 🚀 Running the Application

1. Clone the repo.
2. Create a `.env` file with Neo4j credentials.
3. Run with:

   ```bash
   docker-compose up --build
````

4. Access API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## ⚙️ Development & CI/CD

* Environment variables are loaded via `python-dotenv`.
* Local development and testing with Docker Compose.
* GitHub Actions runs **Black** and **Flake8** on push/PR.
* Docker images are automatically built and pushed to DockerHub on successful CI.

## 📦 Project Layout

* `app/` – FastAPI app source code.
* `Dockerfile` – API container definition.
* `docker-compose.yml` – Service orchestration.
* `.env` – Environment variables (not committed).
* `.github/workflows/ci.yml` – CI workflow for linting and DockerHub deployment.

## ✅ Production Notes

* Store secrets securely with Docker secrets or cloud vaults.
* Implement authentication and rate limiting for API protection.
* Backup Neo4j data volumes regularly.
* Use health checks and logging for observability and maintenance.

## 🧠 Use Cases

* Social network friend management.
* Graph-based recommendations.
* Analytics on social connections.
* Prototyping social features for apps.

---

