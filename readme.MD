## Check out this project on Heroku.
https://desolate-shelf-39908.herokuapp.com/
- I use dataset of books as books' info stored in my database. This is the dataset source: https://www.kaggle.com/austinreese/goodreads-books .
Due to free postgres database limit on heroku, I only uploaded 7000 rows of book data. If you run it locally, it should contains around 50,000 rows of data. The only difference between the web app at local and heroku is number of search results. 

## Run it on your computer locally
### Get Started
##### Clone it to your computer
- Create a new folder, change directory into that new folder
- `git clone <repoURL>`
##### Run the web app using Flask, locally.
- Change directory to the repository just cloned.
- Point Flask to your application: 

    macOS/Linux:  `export FLASK_APP=main.py`
    
    Windows: `set FLASK_APP=main.py`
- Run the flask application: 

    `flask run`
- Open the web app
    Go http://localhost:5000 in your browser.
- Quit the web app
    Press CTRL+C in terminal


