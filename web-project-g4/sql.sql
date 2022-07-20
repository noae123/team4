create table customers
(
    id        int auto_increment
        primary key,
    user_name varchar(30) not null,
    nickname  varchar(30) not null,
    password  varchar(30) not null,
    email     varchar(50) not null,
    constraint customers_id_uindex
        unique (id),
    constraint ck_email
        check (`email` like '%@%.%'),
	constraint ck_min_password
		check (length(`password`) >= 6)
);

INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (2, 'EDEN', 'ED77E77', '4567890', 'E@LJDN.T');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (4, 'Aviv', 'Aviv123', 'E&T22/08/22', 'aviv12@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (5, 'Yarden', 'Yardi90', 'Aa123456', 'yar@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (6, 'Noa', 'Nuni66', 'Nn123456', 'Noa@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (7, 'Gal', 'Galim15/08', 'Gg123456', 'Gal@gmail.com');


create table videos
(
    id_video    int auto_increment,
    user_id     int           not null
        primary key,
    audio       varchar(200)  null,
    image       varchar(200)  null,
    sender_name varchar(30)   not null,
    card_banner varchar(2500) not null,
    color       varchar(20)   null,
    shape       varchar(20)   null,
    dir         tinyint(1)    null,
    video_name  varchar(250)  null,
    constraint videos_id_video_uindex
        unique (id_video),
    constraint fk_user_id
        foreign key (user_id) references customers (id),
    constraint ck_max_card
        check (length(`card_banner`) <= 2500),
    constraint ck_max_sender
        check (length(`sender_name`) <= 30)
);

INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (1, 2, null, null, 'eden', 'tami', 'red', 'triangle', 2, 'var');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (3, 4, null, null, 'Aviv', 'Tomi', 'green', 'squre', 5, 'songi');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (4, 5, null, null, 'Dan', 'Hili', 'yellow', 'circle', 8, 'stars');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (5, 6, null, null, 'Yotam', 'Roni', 'blue', 'rectangle', 9, 'moon');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (6, 7, null, null, 'Yossi', 'Avi', 'orange', 'star', 10, 'sunshine');

