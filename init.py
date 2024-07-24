import oracledb
def createTables():
    try:
        con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
        cursor = con.cursor()
        try:
            val = cursor.execute('drop table emp_hierarchy')
        except:
            print('emp_hierarchy doesnt exist')
        try:
            val = cursor.execute('drop table shipment')
        except:
            print('shipment doesnt exist')
        try:
            val = cursor.execute('drop table transport')
        except:
            print('transport doesnt exist')
        try:
            val = cursor.execute('drop table warehouse')
        except:
            print('warehouse doesnt exist')
        try:
            val = cursor.execute('drop table invoice')
        except:
            print('invoice doesnt exist')
        try:
            val = cursor.execute('drop table document')
        except:
            print('document doesnt exist')
        try:
            val = cursor.execute('drop table client_company')
        except:
            print('client_company doesnt exist')
        try:
            val = cursor.execute('drop table employee')
        except:
            print('employee doesnt exist')
        try:
            val = cursor.execute('drop table branch')
        except:
            print('branch doesnt exist')

        cursor.execute(
            "create table branch(branch_id varchar2(20) primary key, branch_add varchar2(20), branch_budget float)")

        cursor.execute(
            "create table employee(emp_id varchar2(20) primary key, emp_name varchar2(20), emp_dept varchar2(20), emp_sal float, emp_add varchar2(20), emp_branch varchar2(20), foreign key(emp_branch) references branch)")

        cursor.execute(
            "create table client_company(cli_id varchar2(20) primary key, cli_name varchar2(20), cli_add varchar2(20))")

        cursor.execute(
            "create table transport(trans_id varchar2(20) primary key, trans_mode varchar2(20), trans_cap float)")

        cursor.execute(
            "create table warehouse(ware_id varchar2(20) primary key, ware_add varchar2(20))")

        cursor.execute(
            "create table document(doc_id varchar2(20) primary key, doc_add varchar2(20))")

        cursor.execute(
            "create table invoice(inv_id varchar2(20) primary key, inv_date date, inv_amount float, cli_id varchar2(20), emp_id varchar2(20), doc_id varchar2(20), foreign key(cli_id) references client_company,  foreign key(emp_id) references employee,  foreign key(doc_id) references document)")

        cursor.execute(
            "create table emp_hierarchy(emp_id varchar2(20), sup_id varchar2(20), foreign key(sup_id) references employee, foreign key(emp_id) references employee)")

        cursor.execute(
            "create table shipment(ship_id varchar2(20) primary key, ship_date date, ship_from varchar2(20), ship_to varchar2(20), trans_id varchar2(20), inv_id varchar2(20), foreign key(ship_from) references warehouse, foreign key(ship_to) references warehouse, foreign key(trans_id) references transport, foreign key(inv_id) references invoice)")

    except oracledb.DatabaseError as e:
        print("There is a problem with Oracle MAIN", e, e.args)

def insertRecords():
    try:
        con = oracledb.connect(user='system', password='jvdpLNS23510', host='localhost')
        cursor = con.cursor()

        cursor.execute("delete from emp_hierarchy")
        cursor.execute("delete from shipment")
        cursor.execute("delete from transport")
        cursor.execute("delete from warehouse")
        cursor.execute("delete from invoice")
        cursor.execute("delete from document")
        cursor.execute("delete from client_company")
        cursor.execute("delete from employee")
        cursor.execute("delete from branch")

        branch = ['Head','Branch']
        address = ['Mumbai', 'Delhi', 'Bangalore']

        cursor.execute(
            f"insert into branch values('MumbaiHead','Mumbai',10000000)")
        cursor.execute(
            f"insert into branch values('MumbaiBranch','Mumbai',500000)")
        cursor.execute(
            f"insert into branch values('DelhiHead','Delhi',20000000)")
        cursor.execute(
            f"insert into branch values('DelhiBranch','Delhi',1000000)")
        cursor.execute(
            f"insert into branch values('BangaloreHead','Bangalore',20000000)")
        cursor.execute(
            f"insert into branch values('BangaloreBranch','Bangalore',1000000)")

        cursor.execute(
            f"insert into employee values('10001','Ramesh','General', 100000, 'Mumbai', 'MumbaiHead')")
        cursor.execute(
            f"insert into employee values('10002','Mahesh','General', 100300, 'Mumbai', 'MumbaiBranch')")
        cursor.execute(
            f"insert into employee values('10003','Suhesh','Finance', 102000, 'Mumbai', 'MumbaiBranch')")
        cursor.execute(
            f"insert into employee values('10011','Rakesh','General', 90000, 'Delhi', 'DelhiHead')")
        cursor.execute(
            f"insert into employee values('10012','Darshan','Accounts', 80000, 'Delhi', 'DelhiHead')")
        cursor.execute(
            f"insert into employee values('10013','Raju','Finance', 77000, 'Delhi', 'DelhiBranch')")
        cursor.execute(
            f"insert into employee values('10021','John','General', 70000, 'Bangalore', 'BangaloreBranch')")
        cursor.execute(
            f"insert into employee values('10022','Jason','Accounts', 88000, 'Bangalore', 'BangaloreBranch')")
        cursor.execute(
            f"insert into employee values('10023','Blake','Finance', 99900, 'Bangalore', 'BangaloreHead')")

        con.commit()


    except oracledb.DatabaseError as e:
        print("There is a problem with Oracle MAIN", e, e.args)
    print('yeah')
