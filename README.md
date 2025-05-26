# C964_TradingBot

Capstone Project for CompSci B.S. This project is a Flask-based web application designed to fetch, display, and visualize stock market data.

## Project Overview

The C964_TradingBot provides a user-friendly dashboard to view historical stock data. Users can input a stock ticker symbol, and the application will retrieve data for the past year, displaying it in a table and as a closing price chart. The application is containerized using Docker for ease of deployment and consistent environments.

## Features

*   Fetch historical stock data for a given ticker symbol.
*   Display recent stock data in a tabular format.
*   Visualize stock closing prices over the last year using a line chart.
*   Simple web interface built with Flask and HTML.
*   Support for Docker for easy setup and deployment.

## Technologies Used

*   **Python:** Core programming language.
*   **Flask:** A lightweight web framework for building the application and handling HTTP requests.
*   **yfinance:** Library to fetch historical market data from Yahoo Finance.
*   **pandas:** For data manipulation and analysis of stock data.
*   **Matplotlib:** For generating static plots and charts of stock prices.
*   **HTML/CSS:** For the front-end structure and styling (via templates).
*   **Docker:** For containerizing the application, ensuring consistent deployment across different environments.

## Setup and Usage

There are two primary ways to set up and run this application: locally using Python and pip, or using Docker.

### Local Setup (Python & Pip)

**Prerequisites:**

*   Python 3.10 or higher
*   pip (Python package installer)

**Installation & Running:**

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd C964_TradingBot-1
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    Open a terminal in the project root directory and run:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    In the terminal, start the Flask app:
    ```bash
    python app.py
    ```
5.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5000`.

### Docker Setup

**Prerequisites:**

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

**Building and Running with Docker:**

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd C964_TradingBot-1
    ```
2.  **Build the Docker image:**
    In the project root directory, run:
    ```bash
    docker build -t c964_tradingbot .
    ```
3.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 c964_tradingbot
    ```
    *   The `-p 5000:5000` flag maps port 5000 of the container to port 5000 on your host machine.
4.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5000`.

## How It Works

1.  The Flask application (`app.py`) defines routes for the web interface.
2.  When a user accesses the dashboard or submits a ticker symbol:
    *   The `yfinance` library fetches historical stock data for the specified ticker.
    *   `pandas` is used to process this data.
    *   `matplotlib` generates a plot of the closing prices.
3.  The data and the plot (encoded as a base64 string) are passed to an HTML template (`templates/index.html`).
4.  Flask renders the template, displaying the stock information and chart to the user.

## Project Structure
