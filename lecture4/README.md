# Lecture 4: SQL, Models, and Migrations

## SQL

* SQL stores relational data (using SQLite)
  * Data stored in a table
* Data types in SQLite:
	* Text
	* Numeric (numeric data, ex: boolean)
	* Integer
	* Real numbers
	* Blob (binary)
* Creating a table (of flights):
	* `CREATE TABLE flights (
		  id INTEGER PRIMARY KEY AUTOINCREMENT,
		  origin TEXT NOT NULL,
		  destination TEXT NOT NULL,
		  duration INTEGER NOT NULL
	  );`
* Adding data (to the flights table)
	* `INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);`
	* The first part tells it what data values to include
	* The `VALUES` part tells it what values to store for those values
* Retreiving data from table
	* `SELECT * FROM flights;`
	* Gets all data from the given table (flights)
* To retrieve a specific row from the table:
	* `SELECT * FROM flights WHERE id = id_name;`
* To retrieve a specific column:
	* SELECT column_name FROM flights;
* To find a certain row in a table
	* `SELECT * FROM flights WHERE origin = "New York";`
* Comments is SQL are started with `--`

### Working with SQLite Files

* Create a .sql file
* Interact with it using `sqlite3 filename.sql`
* Make displayed data look nice by running `.mode columns` and `.headers yes
`

### Other SQLite Queries

* Adding boolean selections: `SELECT * from flights WHERE duration > 500;`
* Combine boolean conditions with `AND` and `OR`
* Table values can be accessed with RegEx-like syntax

#### SQLite Functions

* `AVERAGE`, `COUNT`, `MAX`, `MIN`, `SUM`, etc.
* Updating data in a table:
`UPDATE flights
	SET duration = 430
	WHERE origin = "New York"
	AND destination = "London";`
	* Finds where the origin is "New York" and the destination is "London" and updates the duration
* Deleting data: `DELETE FROM flights WHERE destination = "Tokyo"`
	* deletes all data values where the destination is Tokyo

### Using Multiple Tables

* You can refer to other tables by referencing their IDs in the columns of other tables
* Use multiple tables to show relations between multiple items in multiple tables
	* These relational tables do not have any data values, they only store ids from different tables
* Use `JOIN` to join multiple tables (an inner join)
* Use `ON` to tell sql the relationship between the two tables

### Optimizations

* Create an index for a table to speed up queries: `CREATE INDEX name_index ON passengers (last_name);`
* Data can then be accessed using the indices

### Vulnerabilities with SQL

* **SQL Injection:** SQL syntax can be taken advantage of to bypass certain conditions
	* Ex: Using `--` to comment out the password condition check when logging into an account
* **Race Checking:** When a database is being accessed by multiple entities at the same time
  * Fixed by locking a database until each request is completed

## Django Models

* Uses models.py file; models are a python class
* **Migrations:** Updating database with changes
  * Run `python3 manage.py makemigrations` to tell Django to create the migrations
  * `python3 manage.py migrate` to tell Django to apply migrations
* Classes are created to represent the data tables that SQL stores
  * `class DATATABLE(models.Model):`
  * Values in the class are accessed with `DATATABLE.objects.all()`
  * Filter results with `DATATABLE.objects.filter()`

### Admin app

* An *admin app* is used to add/modify data with django
  * A *superuser* account is needed to be able to do this: `python3 manage.py createsuperuser`
* Models are loaded into the admin app before it can modify them (for each model): `admin.site.register(MODEL)`
* Admin page can be configured to display different things (look at Django documentation)
