-- Make sure we are using sakila database
USE sakila;

-- See all data from table actor in sakila database
SELECT * FROM actor;

/*	1a. Display the first and last names of all actors from the table `actor`
	1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name` */
SELECT A.first_name, 
		A.last_name,
		UPPER(CONCAT_WS('', first_name,' ', last_name)) AS 'Actor Name'
FROM actor as A
ORDER BY last_name
;
 
-- 2a. Search ID number, first name, and last name of an actor, of whom the only known information is the first name, "Joe." 
SELECT * FROM actor; 

SELECT actor_id, first_name, last_name 
FROM actor
WHERE first_name = "Joe";  

-- 2b. Actors whose last name contain the letters `GEN`
SELECT * FROM actor; 

SELECT actor_id, first_name, last_name 
FROM actor
WHERE last_name LIKE '%GEN%';

-- 2c. Actors whose last names contain the letters `LI`. Rows order by last name and first name, in that order
SELECT * FROM actor; 

SELECT actor_id, first_name, last_name 
FROM actor
WHERE last_name LIKE '%LI%' 
ORDER BY first_name ASC, last_name ASC;

-- 2d. Display `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China
SELECT * FROM country;

SELECT country_id, country
FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

/* 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
so create a column in the table `actor` named `description` and use the data type `BLOB` (Make sure to research the type `BLOB`, 
as the difference between it and `VARCHAR` are significant). */  
ALTER TABLE actor
ADD COLUMN description BLOB(100) after last_name; 

SELECT * FROM actor;
 
-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the `description` column.
ALTER TABLE actor 
DROP COLUMN description;

-- * 4a. List of the last names of actors, as well as how many actors have that last name.
SELECT 
	last_name as Last_Name, 
    COUNT(last_name) AS 'Last Name Count'
FROM 
	actor 
GROUP BY 
	last_name
    ;

-- 4b. List of last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT 
	last_name, 
    COUNT(last_name) AS Count_of_Last_Name
FROM 
	actor 
GROUP BY 
	last_name
HAVING 
 	Count_of_Last_Name > 1
ORDER BY
	Count_of_Last_Name ASC 
    ; 

-- 4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. Write a query to fix the record.
SELECT first_name, last_name
FROM actor
WHERE 
    first_name = 'GROUCHO'
    ;

UPDATE actor
SET first_name = 'HARPO' 
WHERE 
	last_name = 'WILLIAMS'
	AND 
    first_name = 'GROUCHO'
    ;
    
SELECT first_name, last_name
FROM actor
WHERE 
	last_name = 'WILLIAMS'
	AND 
    first_name = 'HARPO'
    ;

/* 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` 
was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.*/
UPDATE actor
SET first_name = 'GROUCHO' 
WHERE 
    first_name = 'HARPO'
    AND 
    last_name = 'WILLIAMS'
    ;

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
--  [https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html]
DESCRIBE sakila.address;

-- 6a. Display the first and last names, as well as the address, of each staff member using JOIN of tables `staff` and `address`.
SELECT S.first_name, S.last_name, A.address
FROM address as A
JOIN staff as S ON (S.address_id = A.address_id);

-- 6b. `JOIN` to display the total amount rung up by each staff member in August of 2005. Tables `staff` and `payment`.
SELECT S.staff_id, S.first_name, S.last_name, P.payment_date, SUM(P.amount) AS 'Total Amount ($)'
FROM 
	staff as S
    JOIN payment as P ON S.staff_id = P.staff_id
    WHERE P.payment_date LIKE '%2005-08%'
    GROUP BY S.staff_id
;

-- 6c. List of each film and the number of actors who are listed for that film. Tables `film_actor` and `film`. Inner join.
SELECT FI.title, COUNT(FA.actor_id) AS 'Number of Actors'
	FROM 
		film as FI
		JOIN film_actor as FA ON FI.film_id = FA.film_id
        GROUP BY FI.title
        ORDER BY FI.title ASC
;

-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT COUNT(film_id) AS Count
FROM inventory 
WHERE film_id IN
(
  SELECT film_id
  FROM film
  WHERE title = 'Hunchback Impossible'
);

/* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list of the total paid by each customer. 
Customers listed alphabetically by last name */
SELECT C.last_name, C.first_name, SUM(amount) AS 'Total Paid'
FROM 
	payment as P 
    JOIN customer as C ON P.customer_id = C.customer_id
    GROUP BY C.last_name
    ORDER BY C.last_name ASC
;

/* 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
films starting with the letters K and Q have also soared in popularity. Using subqueries, display the titles of movies starting
with the letters K and Q whose language is English.*/
SELECT * FROM film;

RENAME TABLE language TO language_table;

SELECT * FROM language_table;
 
SELECT title
FROM film WHERE title 
LIKE 'K%' OR title LIKE 'Q%'
AND title IN 
(
SELECT title 
FROM film 
WHERE language_id = 1
);

-- 7b. Use of subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
( 
	SELECT actor_id
	FROM film_actor
	WHERE film_id IN
	(
		SELECT film_id
		FROM film
		WHERE title = 'ALONE TRIP'
));

/* 7c. To run an email marketing campaign in Canada, for which you will need the names and email addresses 
of all Canadian customers. Use of joins to retrieve this information.*/
SELECT cu.first_name,cu.last_name, cu.email 
FROM customer AS cu
JOIN address AS a ON (a.address_id= cu.address_id)
JOIN city AS ci ON (ci.city_id= a.city_id)
JOIN country AS co ON (co.country_id= ci.country_id)
WHERE co.country = 'canada'
;

/* 7d. Sales have been lagging among young families. Identify all movies categorized as family films, 
to target all family movies for a promotion. */
SELECT title
FROM film
WHERE film_id IN
( 
	SELECT film_id
	FROM film_category
	WHERE category_id IN
	(
		SELECT category_id 
		FROM category
		WHERE name = 'Family'
));

-- 7e. Most frequently rented movies in descending order.
SELECT f.title, COUNT(rental_id) AS 'Times Rented'
FROM rental AS r
	JOIN inventory AS i ON (r.inventory_id = i.inventory_id)
	JOIN film AS f 	ON (i.film_id = f.film_id)
	GROUP BY f.title
	ORDER BY `Times Rented` DESC;

-- 7f. How much business, in dollars, each store brought in?
SELECT s.store_id, SUM(amount) AS Gross_Sales
FROM payment as p
	JOIN rental r ON (p.rental_id = r.rental_id)
    JOIN inventory i ON (i.inventory_id = r.inventory_id)
    JOIN store s ON (s.store_id = i.store_id)
    GROUP BY s.store_id
    ;

-- 7g. Check for each store its store ID, city, and country.
SELECT S.store_ID, CI.city, CO.country 
FROM 
	store as S 
	LEFT JOIN address AS A ON S.address_id = A.address_id
	LEFT JOIN city as CI ON A.city_id = CI.city_id
    LEFT JOIN country as CO ON CI.country_id = CO.country_id
;

-- 7h. Top five genres in gross revenue in descending order. 
SELECT CA.name, SUM(P.amount) AS 'Gross_Revenue ($)' 
FROM 
	category as CA
    LEFT JOIN film_category AS FC ON CA.category_id = FC.category_id
    LEFT JOIN inventory AS I ON FC.film_id = I.film_id
    LEFT JOIN rental AS R ON I.inventory_id = R.inventory_id
    LEFT JOIN payment as P ON R.rental_id = P.rental_id
GROUP BY CA.name ORDER BY SUM(P.amount) DESC LIMIT 5
;

/*8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
Using above solution, create a view */
CREATE VIEW top_five_genres AS 
(
SELECT CA.name, SUM(P.amount) AS 'Gross_Revenue ($)' 
FROM 
	category as CA
    LEFT JOIN film_category AS FC ON CA.category_id = FC.category_id
    LEFT JOIN inventory AS I ON FC.film_id = I.film_id
    LEFT JOIN rental AS R ON I.inventory_id = R.inventory_id
    LEFT JOIN payment as P ON R.rental_id = P.rental_id
GROUP BY CA.name
ORDER BY SUM(P.amount) DESC LIMIT 5
);

-- 8b. Display the view
SELECT * FROM top_five_genres;

-- 8c. No longer need the view top_five_genres. Delete it.
DROP VIEW top_five_genres; 