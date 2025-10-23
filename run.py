"""Simple runner for the Flask application."""
import os
from src.app import create_app

# Ensure environment variable is set
if not os.getenv("MAIN_DB_URI"):
    os.environ["MAIN_DB_URI"] = "sqlite:///H:/TUM-PC/TUM_CEM_PhD/REMS_ACC/REMS-For-ACC/acc_rems.db"

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
