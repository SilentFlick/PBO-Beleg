create table if not exists posts (
    post_id integer primary key autoincrement,
    from_user integer,
    to_user integer,
    title text not null,
    content text not null,
    foreign key(from_user) references professor_lecturer(pl_id) on delete cascade,
    foreign key(to_user) references professor_lecturer(pl_id) on delete cascade
);

create table if not exists professor_lecturer (
    pl_id integer primary key autoincrement,
    name varchar (255) not null,
    faculty varchar (50) not null
);

insert into professor_lecturer values (null, 'Sebastian Aland', 'Informatik');
insert into professor_lecturer values (null, 'Jürgen Anke', 'Informatik');
insert into professor_lecturer values (null, 'Robert Baumgartl', 'Informatik');
insert into professor_lecturer values (null, 'Arnold Beck', 'Informatik');
insert into professor_lecturer values (null, 'Kai Bruns', 'Informatik');
insert into professor_lecturer values (null, 'Georg Freitag', 'Informatik');

insert into posts values (null,2,null,'Krankmeldung','Leider muss die LV für heute absagen');
