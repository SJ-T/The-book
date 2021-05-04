# from numpy import genfromtxt
from the_book import db
from the_book.models import Book
import pandas as pd



# def load_data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, filling_values="null" )
#     return data.tolist()

# try:
file_name = "goodreads_books.csv" 
# data = load_data(file_name) 

data = pd.read_csv(file_name).fillna('null')
data = data.values.tolist()

for i in data:
    record = Book(**{
        'id' : i[0], 
        'isbn' : i[20] ,
        'title' : i[1] ,
        'author' : i[5] ,
        'description' : i[30] ,
        'num_page' : i[15] ,
        'average_rating' : i[9] ,
        'ratings_count' : i[7] ,
        'publication_date' : i[16] ,
        'publisher' : i[17] 

    })
    db.session.add(record) #Add all the records
    
db.session.commit() #Attempt to commit all the records
# except:
#     db.session.rollback() #Rollback the changes on error