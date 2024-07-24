DROP TABLE dept;
DROP TABLE person;

CREATE TABLE dept(
	id varchar2(5),
	name varchar2(10),
	PRIMARY KEY(id)
	);

CREATE TABLE person(
	id varchar2(5),
	name varchar2(10),
	dept varchar2(5),
	position varchar2(10) NOT NULL,
	marks float(1),
	password varchar2(10) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(dept) REFERENCES dept(id),
	CHECK (
		(position = 'Teacher' OR position = 'Student')
		AND
		((position = 'Teacher' AND (marks IS NULL))
		OR
		(position = 'Student' AND marks >= 0)))
	);
	

INSERT INTO dept VALUES(
	'CSE',
	'Computers'
	);
INSERT INTO dept VALUES(
	'PHY',
	'Physics'
	);
	
INSERT INTO person VALUES(
	'00003',
	'Boy2',
	'CSE',
	'Teacher',
	NULL,
	'iamaBOY2'
	);
INSERT INTO person VALUES(
	'00001',
	'Boy1',
	'CSE',
	'Student',
	10.5,
	'iamaBOY1'
	);
INSERT INTO person VALUES(
	'00002',
	'Someguy1',
	'PHY',
	'Student',
	99.25,
	'iamSOMEGUY'
	);
INSERT INTO person VALUES(
	'00004',
	'Boy2',
	'CSE',
	'Student',
	50.5,
	'iamaBOY2'
	);
	
--- Conditional

--- Login
--- 	get ID, password, select ID, password from db, 
---		not found -> tell to register
--- 	found -> matched -> Teacher -> Show some details of all students in their branch
---						 -> Student -> Show details of themselves ONLY
---			  -> not matching -> tell wrong password

--- register
---		Input details

SELECT 
	
--- Other queries

SELECT * from person;

SELECT id, name, position, marks FROM person;

SELECT id, name, marks FROM person;

