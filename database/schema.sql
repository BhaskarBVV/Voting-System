create table if not exists User (
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

create table if not exists Role (
 UserId int not null,
 RoleId int not null,
 foreign key (UserId) references User(UserId)
);

 create table if not exists Approval (
 UserId int not null,
 IsApproved bool not null,
 foreign key (UserId) references user(UserId)
);

create table if not exists VoteRecord (
UserId int not null,
Vstatus bool not null,
VoteId int not null,
foreign key (UserId) references user(UserId)
);

create table if not exists Party (
 PartyID int not null primary key,
 PartyName varchar(50) not null
);

create table if not exists Result(
PartyId int not null,
ElectionYear int not null,
votes int not null,
primary key(PartyId,ElectionYear),
foreign key (PartyId) references Party(PartyId)
);
