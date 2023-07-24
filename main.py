import sqlalchemy

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = sqlalchemy.create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:
    # # Run an SQL query with a condition for publication year after 2000 and use COUNT to get the number of results
    results = connection.execute('SELECT COUNT(*) FROM books WHERE publication_year >2000')
    num_results = results.scalar()

    # Print the number of results retrieved
    print(f"Returned {num_results} results")

    # Run as SQL query with condition for authors name
    results = '''SELECT books.title, authors.name
              FROM books
              JOIN authors ON books.author_id = authors.author_id
              ORDER BY books.title
    '''

    results = connection.execute(results)
    row = results.fetchall()

    # Print book names along with their authors' names in alphabetical order
    for row in row:
        book_title = row['title']
        author_name = row['name']

        print(f"{book_title} ({author_name})")

    # # Run the actual query to fetch the book details
    # results = 'SELECT * FROM simple_books WHERE publication_year > 2000'
    # results_books = connection.execute(results)
    # rows = results_books.fetchall()
    #
    # # Print values for each row using column names as keys
    # for row in rows:
    #     title = row['title']
    #     author = row['author']
    #     publication_year = row['publication_year']
    #     genre = row['genre']
    #
    #     print(f"Title: {title}, Author: {author}, Published Year: {publication_year}, Genre: {genre}")
