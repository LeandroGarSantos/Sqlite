import sqlalchemy


# Ask the user for search term
search_input = input("Enter a the year to search at catalog: ")

# Create params dict
params = {"search": search_input}

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = sqlalchemy.create_engine('sqlite:///data/textbook.sqlite3')


with engine.connect() as connection:
    query = sqlalchemy.text('SELECT * FROM books WHERE publication_year = :search')
    result = connection.execute(query, params)
    rows = result.fetchall()

    # Print num of results
    print(f"Returned {len(rows)} results")

    # Print results
    for row in rows:
        print(f'{row["title"]}')