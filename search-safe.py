import sqlalchemy


# Ask the user for search term
search_input = input("Enter a search term for the books catalog: ")

# Create params dict
params = {"search": search_input}

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = sqlalchemy.create_engine('sqlite:///data/textbook.sqlite3')


with engine.connect() as connection:

  query = sqlalchemy.text('SELECT title FROM books WHERE title = :search')
  results = connection.execute(query, params)
  rows = results.fetchall()

  # Print num of results
  print(f"Returned {len(rows)} results")

  # Print results
  for row in rows:
    print(f'{row["title"]}')