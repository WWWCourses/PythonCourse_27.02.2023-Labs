/* --------------------------------- SELECT --------------------------------- */

SELECT * FROM employees.employees;

# Select all male employees who were hired after 1990-01-01:
SELECT *
FROM employees.employees
WHERE hire_date>'1990-01-01' AND gender='M';

# Select all male employees who were hired after 1990-01-01 and their first name starts with 'L':
SELECT *
FROM employees.employees
WHERE hire_date>'1990-01-01' AND gender='M' AND first_name LIKE 'L%';


# aliases
SELECT * FROM employees.employees as emp
WHERE emp.hire_date>'90-01-01';



-- INSERT INTO table_name [(column, ...)]
-- VALUES (value, ...)[, (...), ...];

use TEST;
INSERT INTO `Client` (fname,lname,town_id)
VALUES
	('Ivan', 'Ivanov',2),
	('Asen', 'Asenov',2),
	('Pesho', 'Peshoev', 1);


INSERT INTO `Client` (fname,lname,town_id)
VALUES ('Ivan','Petrov',3);

INSERT INTO `Client` (fname)
VALUES ('Maria');

SELECT * FROM `Client`
WHERE fname LIKE 'I%'
ORDER BY lname
LIMIT 1;


/* --------------------------------- DELETE --------------------------------- */
DELETE FROM `Client`
WHERE fname LIKE 'I%'
ORDER BY lname
LIMIT 1;

/* --------------------------------- UPDATE --------------------------------- */
-- Replace all null lname values with 'Anonymous'
-- TODO: fix error
UPDATE `Client`
SET lname='Anonymous'
FROM `Client`
WHERE lname IS NULL;

/* ----------------------------- ORDINARY INDEX ----------------------------- */

ALTER TABLE employees.employees
ADD INDEX(first_name);


/* --------------------------- Create Client Table -------------------------- */
DROP TABLE IF EXISTS Client ;
CREATE TABLE `Client` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`town_id` INT NOT NULL,
	`fname` varchar(5) DEFAULT NULL,
	`lname` varchar(10) NOT NULL,
	PRIMARY KEY(id),
	Foreign Key (town_id) REFERENCES Address (id)
);


/* --------------------------- Create Addres Table -------------------------- */
DROP TABLE IF EXISTS Address ;
CREATE TABLE `Address` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`town` varchar(20) NOT NULL UNIQUE,
	PRIMARY KEY(id)
);

INSERT INTO Address (town)
VALUES
	('Sofia'),
	('Plovdiv'),
	('Varna');




/* --------------------------- Create Order table --------------------------- */
CREATE Table order(
	'order_date' DATE NOT NULL,
	''
);



/* ------------------------------ SELECT DEMOS ------------------------------ */
# Select all clents, show 'fname', 'lname', 'town':
SELECT `fname`, `lname`, `town`
FROM Client as c,Address as a
WHERE c.town_id=a.id
ORDER BY c.fname;


# Select all clients which name starts with 'I'  and who lives in 'Sofia'


/* ------------------------ Many to Many Relationship ----------------------- */
/* -------------------- One Client can live in many towns ------------------- */
DROP TABLE IF EXISTS Client ;
CREATE TABLE `Client` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`fname` varchar(5) DEFAULT NULL,
	`lname` varchar(10) NOT NULL,
	PRIMARY KEY(id),
	Foreign Key (town_id) REFERENCES Address (id)
);

DROP TABLE IF EXISTS Address ;
CREATE TABLE `Address` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`town` varchar(20) NOT NULL UNIQUE,
	PRIMARY KEY(id)
);


CREATE TABLE ClientAddress(
	`id` INT NOT NULL AUTO_INCREMENT,
	client_id INT NOT NOT
	address_id INT NOT NOT
)