--employee

create table employee
(emp_id varchar2(20) primary key,
emp_name varchar2(30),
emp_dept varchar2(30),
emp_sal float,
emp_add varchar2(20),
emp_branch varchar2(20),
foreign key (emp_branch) references branch);

--branch

create table branch
(br_name varchar(20) primary key,
br_address varchar(20),
br_budget float);

--client_company

create table if not exists client_company
(Cli_id varchar2(20) primary key,
Cli_name varchar2(20),
Cli_add varchar2(30));

--transport

create table if not exists transport
(Trans_id varchar2(20) primary key,
Trans_mode varchar2(30),
Trans_cap float);

--shipment

create table if not exists shipment
(Ship_id varchar2(20) primary key,
Ship_date date,
Ship_from varchar2(20),
Ship_to varchar2(20),
Ship_status varchar2(30),
Ship_trans varchar2(20),
Inv_id varchar2(20),
foreign key (Ship_trans) references transport(Trans_id),
foreign key (Inv_id) references invoice),
foreign key (Ship_from) references warehouse),
foreign key (Ship_to) references warehouse);

--warehouse

create table if not exists warehouse
(Wh_id varchar2(20) primary key,
Wh_add varchar2(30));

--invoice

create table if not exists invoice
(Inv_no varchar2(20) primary key,
Inv_date date,
Inv_amt float,
Cli_id varchar2(20),
foreign key (Cli_id) references client_company(Cli_id)
Emp_no varchar2(20),
foreign key (Emp_no) references employee(Emp_no),
Doc_id varchar2(20),
foreign key (Doc_id) references Document);

--emp_hierarchy

create table if not exists emp_hierarchy
emp_no varchar2(20),
super_no varchar2(20),
primary key (emp_no, super_no),
foreign key (emp_no) references employee(emp_no),
foreign key (super_no) references employee(emp_no));

-- document

create table if not exists document
(doc_id varchar2(20) primary key,
doc_type varchar(50),
doc_add varchar(100));

---PLSQL

CREATE OR REPLACE TRIGGER Employee_Minimum_Wage
BEFORE INSERT OR UPDATE ON Employee
FOR EACH ROW
DECLARE 
	ex exception;
BEGIN
	if :NEW.emp_sal >= 30000 THEN
		insert into Employee values(:NEW.emp_id, :NEW.emp_name, :NEW.emp_dept, :NEW.emp_sal, :NEW.emp_add, :NEW.emp_branch);
	else 
		RAISE ex;
	end if;
END;
/

---
CREATE OR REPLACE PROCEDURE low_wage(x float) IS
BEGIN
	for i in (select emp_name from employee where emp_sal < x)
	LOOP
		dbms_output.put_line(i.emp_name);
	END LOOP;
END;
/

DECLARE
BEGIN
	low_wage(100000);
END;
/



select * from employee e where e.emp_sal >= all(select e2.emp_sal from employee e2);

select * from employee where emp_add = 'Delhi';

select * from branch where branch_add = 'Mumbai';

with b as
(select branch_id br from branch where branch_add = 'Delhi')
select * from employee, b where emp_branch = b.br and emp_sal > 50000;





