## The Book
This is a book-searching web app. Like the description, it can search books and give you some info about books for you.

**Main Features**
- Search books by its title, author or ISBN.
- Display information about the book like cover, title, author, ISBN, publisher, publication date, description.
- Add to shelf: users can add the book to their collection after login.
- Give ratings: users can add ratings to the books after login.

**Technologies**
- Flask framework.
- Sqlite database locally and postgres database on server.

**Defects**
- If you update the ratings you gave, the average ratings won't update.
- The books on the shelf cannot be deleted.
- Reset password part hasn't been implemented.
- The book detail page on deployed web app cannot hide excess text in the description.(While it works fine locally)

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


