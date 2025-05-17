---

# 🚀 Social Network Friend Graph API

## 📘 Overview

The **Social Network Friend Graph API** is a scalable backend service built with **FastAPI**, **Neo4j**, and **Docker Compose**. It models social relationships, allowing users to create friendships, list friends, and find mutual friends efficiently using graph database capabilities.

## 🧩 Tech Stack

* ⚡ **FastAPI** – Modern, fast Python web framework.
* 🌐 **Neo4j** – Graph database optimized for connected data.
* 🐳 **Docker Compose** – Simplifies local development and deployment.
* 🔐 **python-dotenv** – Securely manage environment variables.
* 🖋️ **Black & Flake8** – Code formatting and linting for code quality.
* ⚙️ **GitHub Actions** – Automated lint checks and Docker image deployment to DockerHub.

## 🎯 Features

### 👤 User Management

* Add new users with unique IDs.
* Create corresponding user nodes in Neo4j automatically.

### 🤝 Friendships

* Establish bi-directional friendships between users.
* Prevent duplicates and invalid relations.
* Support flexibility for future enhancements.

### 📜 Friends Listing

* Fetch a user’s complete list of friends.
* Provide structured responses for easy integration.

### 🧑‍🤝‍🧑 Mutual Friends

* Query mutual friends between any two users.
* Enables social recommendations and trust calculations.

## 🚀 Running the Application

1. Clone the repository.

2. Create a `.env` file with Neo4j credentials.

3. Run with:

   ```bash
   docker-compose up --build
   ```

4. Access the API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## ⚙️ Development & CI/CD

* Environment variables loaded securely using `python-dotenv`.
* Use Docker Compose for easy local development and testing.
* GitHub Actions workflow runs **Black** and **Flake8** on every push and pull request to ensure code quality.
* On successful CI checks, Docker images are automatically built and pushed to DockerHub repository  for seamless deployment.

## 📦 Project Structure

* `app/` – FastAPI source code and business logic.
* `Dockerfile` – Defines the API container image.
* `docker-compose.yml` – Orchestrates services including Neo4j and the API.
* `.env` – Contains sensitive environment variables (excluded from version control).
* `.github/workflows/ci.yml` – GitHub Actions workflow for linting and DockerHub image deployment.

## ✅ Production Considerations

* Securely store and manage secrets via Docker secrets or cloud vaults.
* Implement authentication, authorization, and rate limiting to protect the API.
* Backup Neo4j persistent volumes regularly for data durability.
* Add health checks, monitoring, and logging for operational visibility.

## 🧠 Ideal Use Cases

* Managing social network friend graphs.
* Graph-based friend recommendations and analytics.
* Trust scoring and social influence modeling.
* Rapid prototyping of social features for applications.

---
