# Local Development Setup

## Prerequisites
- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/)

## Install Dependencies
1. Open a terminal in the project root directory.
2. Run:
   ```sh
   pip install -r requirements.txt
   ```

## Run the Application
1. In the terminal, start the Flask app:
   ```sh
   python app.py
   ```
2. Open your browser and go to [http://localhost:5000](http://localhost:5000) to access the app.

## Development Tips
- Edit `app.py` to add features or fix bugs.
- Restart the app after making changes.
- Use a virtual environment for dependency management (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Troubleshooting
- If you have issues with dependencies, ensure your Python version matches the requirements.
- For port conflicts, change the port in `app.py` and access the app at the new port.