create table posts (
    post_id integer primary key autoincrement,
    from_user integer,
    to_user integer,
    title text not null,
    content text not null,
    foreign key(from_user) references professor_lecturer(pl_id) on delete cascade,
    foreign key(to_user) references professor_lecturer(pl_id) on delete cascade
);

create table professor_lecturer (
    pl_id integer primary key autoincrement,
    name varchar (255) not null,
    faculty varchar (50) not null
);
