# Docker Usage

## What is Docker?
Docker is a platform for developing, shipping, and running applications inside lightweight, portable containers. Containers bundle your application code with all dependencies, ensuring it runs the same everywhere.

## Key Docker Concepts
- **Image:** A snapshot of your application and its environment. Built from a Dockerfile.
- **Container:** A running instance of an image. Isolated from the host and other containers.
- **Dockerfile:** A script with instructions to build a Docker image.
- **Volume:** A persistent storage mechanism for containers, useful for saving data.
- **Network:** Allows containers to communicate with each other and the outside world.

## Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your OS.

## Step-by-Step: Building This Project from Scratch with Docker

### 1. Initialize a New Repository
- Create a new project folder and initialize git:
  ```sh
  mkdir my-flask-app && cd my-flask-app
  git init
  ```

### 2. Set Up the Python Environment
- Create `app.py` for your Flask app.
- Add a `requirements.txt` with dependencies (Flask, pandas, etc.).

### 3. Write the Main Application
- Implement your Flask routes and logic in `app.py`.
- Add HTML templates in a `templates/` folder.

### 4. Create a Dockerfile
- Example Dockerfile:
  ```Dockerfile
  FROM python:3.10-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```

### 5. Build the Docker Image
  ```sh
  docker build -t my-flask-app .
  ```

### 6. Run the App in Development Mode
  ```sh
  docker run -p 5000:5000 -v $(pwd):/app my-flask-app
  ```
  - The `-v` flag mounts your code for live editing.

### 7. Run the App in Production Mode
  ```sh
  docker run -p 5000:5000 my-flask-app
  ```

### 8. Access the App
- Open [http://localhost:5000](http://localhost:5000) in your browser.

### 9. Stopping the Container
- Press `Ctrl+C` in the terminal or stop the container via Docker Desktop.

## Why Use Docker Here?
- Ensures all dependencies are included.
- Makes deployment and sharing easier.
- Avoids "works on my machine" issues.
- Supports scaling and orchestration with Docker Compose or Kubernetes.

## Additional Tips
- Use Docker Compose for multi-container setups (e.g., Flask + MongoDB).
- Use volumes for persistent database storage.
- Refer to the official [Docker documentation](https://docs.docker.com/) for advanced usage.