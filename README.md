# sjsu_library
CMPE132 Term Project

This project is a simplistic view of the SJSU library website to show role based access control model. 
The project was implemented using Python and the Flask framework. To run the program, clone the repo and run the following commands in the root of the project directory.

## MacOS Terminal
1. `pip install -e .`
2. `flask --app website init-db`
3. `sqlite3 < ./tests/prefill-db.sql`
4. Start website: `flask --app website run`
5. Website can be found on http://127.0.0.1:5000
