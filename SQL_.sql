#- my sql -#################################################################################################################
spark.sql("""
Create TABLE products    (
    id INTEGER PRIMARY KEY not null AUTO_INCREMENT ,    name_p VARCHAR(20) not null
    );
Create table categories    (
    id integer not null AUTO_INCREMENT primary key,    name_c varchar(45) not null
    );
create table connections    (
    p_id Integer not null,    c_id integer not null,
    foreign key (p_id) references products(id),    foreign key (c_id) references categories(id)
    );
Insert into products (name_p) VALUES("Клавиатура"),
("Принтер"),("Монитор");
Insert into categories (name_c) VALUES
("Периферия"),("Компьютерная техника");
Insert into connections VALUES
(1, 1),(3, 1),
(1, 2),(3, 2);
Select pr.name_p, ca.name_c from connections as co
join categories as ca on ca.id = co.c_idjoin products as pr on pr.id = co.p_id
UNION 
Select pro.name_p, 'no category' from products as pro
left outer join connections as c on c.p_id = pro.id
where  c.p_id is null
order by name_c, name_p
""")
.show()

#- pl sql -#################################################################################################################

spark.sql("""

Create TABLE products    
    (
    id INTEGER generated always as identity not null,    
    name_p VARCHAR(20) not null,
    CONSTRAINT products_pk PRIMARY KEY (id)
    );

Create table categories    
    (
    id integer generated always as identity not null,    
    name_c varchar(45) not null,
    CONSTRAINT categories_pk PRIMARY KEY (id)
    );

create table connections
    (
    p_id Integer not null,    
    c_id integer not null,
    foreign key (p_id) references products(id),    
    foreign key (c_id) references categories(id)
    );

Insert into products (name_p) VALUES ( 'Клавиатура');
Insert into products (name_p) VALUES ( 'Принтер');
Insert into products (name_p) VALUES ( 'Монитор');


Insert INTO categories (id, name_c) VALUES (DEFAULT,'Периферия');
Insert INTO categories (id, name_c) VALUES (DEFAULT,'Компьютерная техника');


Insert ALL 
INTO connections VALUES (1, 1)
INTO connections VALUES (3, 1)
INTO connections VALUES (1, 2)
INTO connections VALUES (3, 2)
SELECT 1 FROM DUAL;

SELECT pr.name_p, ca.name_c FROM connections co
inner join products pr on pr.id = co.p_id
Inner join categories ca on ca.id = co.c_id
UNION
Select pro.name_p, 'no category' from products  pro
left outer join connections  c on c.p_id = pro.id
where  c.p_id is null
""")
.show()