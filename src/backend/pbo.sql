create table if not exists posts (
    post_id integer primary key autoincrement,
    from_user integer,
    to_user integer,
    faculty varchar(50),
    title text not null,
    content text not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key(from_user) references professor_lecturer(pl_id) on delete cascade,
    foreign key(to_user) references professor_lecturer(pl_id) on delete cascade
);

create table if not exists comments (
    comment_id integer primary key autoincrement,
    post_id integer not null,
    from_user integer ,
    comment text not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key(post_id) references posts(post_id) on delete cascade,
    foreign key(from_user) references professor_lecturer(pl_id) on delete cascade
);

create table if not exists professor_lecturer (
    pl_id integer primary key autoincrement,
    name varchar (255) not null,
    faculty varchar (50) not null
);



insert into professor_lecturer values (null, 'Sebastian Aland', 'Informatik/Mathematik');
insert into professor_lecturer values (null, 'Jürgen Anke', 'Informatik/Mathematik');
insert into professor_lecturer values (null, 'Robert Baumgartl', 'Informatik/Mathematik');
insert into professor_lecturer values (null, 'Arnold Beck', 'Informatik/Mathematik');
insert into professor_lecturer values (null, 'Kai Bruns', 'Informatik/Mathematik');
insert into professor_lecturer values (null, 'Georg Freitag', 'Informatik/Mathematik');

INSERT INTO posts(post_id, from_user, to_user, faculty, title, content) VALUES(null, 2, null,'Informatik/Mathematik' , 'Krankmeldung', 'Leider muss die LV für heute absagen');
INSERT INTO posts(post_id, from_user, to_user, faculty, title, content) VALUES(null, null, null,'Informatik/Mathematik' , 'Funny story in today class', 'Laughter is infectious. It lightens the weights we carry in life, uplifts our moods, and bonds us to those we share in it with. So why would not we embrace any chance we have to giggle at a joke? That is why we have rounded up that set of (clean) jokes for adults and kids alike that will have the whole family laughing.
But that is not all. In addition to the 70 jokes below, we have also got dad jokes, jokes for kiddos, mom jokes, and jokes for holidays that you can share them with the youngest person in the room.
Get ready: Some of what is to come is quite punny. Some might even make your eyes roll. But, deep down, if we are honest, who does not smile at corny jokes? Others might even make you laugh so hard you cry, so do not say we did not warn you. Many are one-liners so you can remember them to share and share again, and your kids can retell them to their friends too, maybe even years later. Now get ready to make some memories filled with laughter with these 70 hilariously funny jokes!');
INSERT INTO posts(post_id, from_user, to_user, faculty, title, content) VALUES(null, 3, null,'Informatik/Mathematik', 'Hausaufgaben für Weihnachten', 'Randomly creates a first and last name, using an array of common first and last names. GenerateName() returns a string[2] (2 element array) containing the randomly chosen first and last name. This is written as a class so it can be instantiated and called numerous times when creating large datasets.');
INSERT INTO posts(post_id, from_user, to_user, faculty, title, content) VALUES(null, null, null, 'Informatik/Mathematik', 'Why do we have assaignments?', 'Because we are lazy and we want to make you lazy too');

INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 1, 1, 'I hope you get well soon');
INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 1, null, 'How long will you be out?');
INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 1, null, 'How about homeworks?');
INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 2, null, 'I love this joke');
INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 2, null, 'This is hilarious');
INSERT INTO comments(comment_id, post_id, from_user, comment) VALUES(null, 2, null, 'I am crying');


