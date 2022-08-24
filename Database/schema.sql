 create table User (
 UserId int primary key,
 Name Varchar (50) not null,
 Father_Name Varchar (50) not null,
 Aadhaar_number bigint not null unique,
 age int not null,
 contact bigint not null unique,
 Email varchar (50) not null unique,
 city varchar (20) not null,
 passwd varchar (40) not null,
 gender varchar(7) not null
);


create table Role (
 UserId int not null,
 RoleId int not null,
 foreign key (UserId) references User(UserId)
);

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
 PartyName varchar(50) not null
);

create table Result(
PartyId int not null,
ElectionYear int not null,
votes int not null,
primary key(PartyId,ElectionYear),
foreign key (PartyId) references Party(PartyId)
);
