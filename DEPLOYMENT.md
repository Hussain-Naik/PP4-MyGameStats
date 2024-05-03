# Deployment

- The app was deployed to [Render](https://render.com/).
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/).

- The app can be reached by the [link](https://pp4-mygamestats.onrender.com/).

## Local deployment

*Note:*
  - This project requires to install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/Hussain-Naik/PP4-MyGameStats).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/Hussain-Naik/PP4-MyGameStats`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Hussain-Naik/PP4-MyGameStats)

---

1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`

    *Advise setting up a virtual environment to install all app dependencies.*


1. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEVELOPMENT'] = 'True'
    ```

    *During the development stage DEBUG is set to True, but it is vital to change it to False.*

1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.

1. run the following command to import matchup data.
    - `python3 manage.py loaddata match_data.json`

## Render Deployment

### Create Database on ElephantSQL

1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account.

2. Create a new instance of the database.

3. Select a name for your database and select the free plan.

4. Click "Select Region"

5. Select a region close to you.

6. Click "Review"

7. Click "Create Instance"

8. Click on the name of your database to open the dashboard.

9. Copy the database URL and paste as a string for the os.environ['DATABASE_URL'] variable.

### Create a new app on Render

Link to the deployed application on Render: [My Game Stats](https://pp4-mygamestats.onrender.com/)

1. Create a new Render account if you don't already have one here [Render](https://render.com/).

2. Create a new application on the following page here [New Render App](https://dashboard.render.com/), choose **Web Service**:

3. Select Build and deploy from a Git repository

4. Search for the repository you created and click "Connect."

5. Create name for the application

6. Select the region where you want to deploy the application.

7. Select branch to deploy.

8. Select Python 3 as runtime option.

9. Render build command: `pip install -r requirements.txt`

10. Render start command: `gunicorn <NAME OF YOUR APP>.wsgi` 

11. Select Free plan.

12. Add the following environment variables:

    - Key: DATABASE_URL Value: *************
    - Key: SECRET_KEY Value: *************
    - Key: DEVELOPMENT Value: False

    *DATABASE_URL value is takes from ElephantSQL dashboard, SECRET_KEY value is takes from your local env.py file, DEBUG value is set to False.*

13. Create a superuser for your database from your local deployment.

    ```bash
        python manage.py createsuperuser
    ```

14. Commit and push the changes to GitHub.

15. Go back to Render and click "Create Web Service."

16. Wait for the completion of the deployment.

17. Start using the application

---