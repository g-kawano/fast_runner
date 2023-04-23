create table items(
    id int auto_increment,
    name text,
    age int,
    primary key (id)
) ;

insert into items(name, age)values('Alice', 25);
insert into items(name, age)values('Bob', 30);