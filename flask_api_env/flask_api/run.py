from flaskforum import app, manager

# use 'venv\Scripts\activate' within flask_api_venv directory to activate virtual environment
# use 'deactivate' to deactivate virutal environment
# use 'pip list' to check all installed packages
# use 'python run.py' within flask_api directory

# use 'python run.py db init' to initalize migration
# use 'python run.py db revision --rev-id {filename}' to make new file with blank configs
# use 'python run.py db migrate' perform database migration
# use 'python run.py db upgrade' to commit migration
if __name__ == '__main__':
    # manager.run() #run to migrate database
    app.run(debug=True, port=5000)
