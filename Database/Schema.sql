show databases;
create database voting; 
use voting;
show tables;

create table User (
 UserId int primary key,
 Name Varchar (25) not null,
 Father_Name Varchar (25) not null,
 Aadhaar_number int not null unique,
 age int not null check(age>=18),
 contact int not null unique,
 Email varchar (20) not null unique,
 city varchar (20) not null,
 passwd varchar (40) not null,
 gender varchar(7) not null
);

desc user;
insert into user values(1,"Bhaskar","Kanhiya Lal",432893,22,1234567890,"abc@gmail.com","Hathras", "1234","Male");
select * from User;

create table Role (
 UserId int not null,
 RoleId int not null,
 foreign key (UserId) references User(UserId)
);
desc Role;

 create table Approval (
 UserId int not null,
 IsApproved bool not null,
 foreign key (UserId) references user(UserId)
);

create table VoteRecord (
UserId int not null,
Vstatus bool not null,
VoteId int not null,
foreign key (UserId) references user(UserId)
);

 create table Party (
 PartyID int not null primary key,
 PartyName varchar(20) not null
);
