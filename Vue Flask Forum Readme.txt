Instructions

For this website, it is required that two local servers are running at the same time, one will be used for the Restful Flask API and the other will be used for Vue Js frontend. 

FLASK RESTFUL API INSTRUCTIONS:
To run the Flask API, it needs to run on a local server and it will be running the application from a virtual environment so that all packages will be already pre-installed within the whole folder itself.

To run the virtual environment do the following (instructions for windows OS only), start with going into command prompt:

1. Go to the 'flask_api_env' folder
2. Enter 'venv\Scripts\activate' to activate the virtual environment
3. Go to the following path: flask_api_env (folder) > flask_api (folder)
4. Enter 'python run.py' to run the local server

If you want to change the port number for the localhost, go to the following path: flask_api_env (folder) > flask_api (folder) > run.py . Look for the code 'app.run(debug=True, port=5000)' on line 14 and change the 'port' parameter 
(localhost uses port number 5000 by default)
WARNING: If you change the port number for the FLASK API port number, you will also need to change the api http request url with a different port number in order for the vue frontend to call the correct API server. To change this, go to the path:
vue_frontend (folder) > src (folder) > main.js. Look for the code 'domain_name_api: 'http://127.0.0.1:5000/api/' on line 13 and change the url's port to reflect the changes made in the port for the API server.


VUE JS FRONTEND INSTRUCTIONS:
To run the local server of the Vue js website do the following (instructions for windows OS only), start with going into command prompt:

1. Go to the 'vue_frontend' folder
2. Enter 'npm run serve -- --port 8080' to run the local server on port 8080 (you can change the port number to whatever you want)


