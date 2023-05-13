create table Salesperson(Snum number, Sname varchar(20), City varchar(20), Comm number);

insert into Salesperson(Snum,Sname,City,Comm) values(1001,'Peel','London',.12);
insert into Salesperson(Snum,Sname,City,Comm) values(1002,'Serres','San Jose',.13);
insert into Salesperson(Snum,Sname,City,Comm) values(1004,'Motika','London',.11);
insert into Salesperson(Snum,Sname,City,Comm) values(1007,'Rafkin','Barcelona',.15);
insert into Salesperson(Snum,Sname,City,Comm) values(1003,'Axelrod','New_York',.1);

create table Cust(Cnum number, Cname varchar(20), City varchar(20), Rating number, SNUM number);

insert into Cust(Cnum,Cname,City,Rating,SNum) values(2001,'Hoffman','London',100,1001);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2002,'Giovanne','Rome',200,1003);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2003,'Liu','SanJose',300,1002);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2004,'Grass','Berlin',100,1002);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2006,'Clemens','London',300,1007);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2007,'Pereira','Rome',100,1004);
insert into Cust(Cnum,Cname,City,Rating,SNum) values(2008,’Smith’,'Rome',100,1004);


create table Orders(Onum number, AMt number, ODATe varchar(20), Cnum number,Snum number);

insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3001,18.69,'03-OCT-94',2008,1007);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3003,767.19,'03-OCT-94', 2001, 1001);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3002,1900.10,'03-OCT-94', 2007, 1004);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3005,5160.45,'03-OCT-94', 2003, 1002);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3006,1098.16,'04-OCT-94',2008,1007);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3009, 1713.23,'04-OCT-94', 2002, 1003);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3007,75.75,'05-OCT-94', 2004, 1002);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3008,4723.00,'05-OCT-94', 2006, 1001);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(1010,1309.95,'06-OCT-94', 2004, 1002);
insert into Orders(Onum,Amt,ODate,Cnum,Snum) values(3011,9891.88,'06-OCT-94', 2006, 1001);

select * from Cust where Rating>100;

select Sname from Salesperson where City='New_York';

select CName from Cust where City='Berlin';

select Onum from Orders where Amt>1000;

alter table Salesperson add constraint S_num primary key(Snum);
alter table Cust add constraint C_Num primary key(Cnum);
alter table Orders add constraint O_Num primary key(Onum);
alter table Cust add constraint S_Num_foreign foreign key(Snum) references Salesperson(Snum);
alter table Orders add constraint S_Num_foreign1 foreign key(Snum) references Salesperson(Snum);
alter table Orders add constraint C_Num_foreign1 foreign key(Cnum) references Cust(Cnum); 
select count(*) Onum, Snum from Orders group by Snum;
select count(*) Onum, ODate from Orders where ODate='05-OCT-94' group by ODate;
select min(Amt), ODate from Orders group by ODate;
select count(*) Onum, ODate from Orders where ODate='03-OCT-94' OR ODate='04-OCT-94' group by ODate;
select * from Salesperson order by Comm;
select min(Amt) from Orders group by Cnum;
select ODate, avg(Amt) from Orders group by ODate order by avg(Amt);
select min(rating),City from Cust group by City;
select Sname from Salesperson where Snum in (select Snum from Cust where Rating=300); 
select o.Onum, o.Amt, o.ODate, c.Cname as CustomerName, s.Sname as SalespersonName from Orders o join Cust c on o.Cnum=c.Cnum join Salesperson s on s.Snum=o.Snum;