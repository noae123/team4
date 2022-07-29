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


INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (1, 'Card4You', 'card4u', 'CD123456', 'card4u@c4u.io');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (2, 'EDEN', 'ED77E77', '4567890', 'E@LJDN.T');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (4, 'Aviv', 'Aviv123', 'E&T22/08/22', 'aviv12@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (5, 'Yarden', 'Yardi90', 'Aa123456', 'yar@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (6, 'Noa', 'Nuni66', 'Nn123456', 'Noa@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (7, 'Gal', 'Galim15/08', 'Gg123456', 'Gal@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (8, 'Don', 'dondon5', 'Don12345', 'don@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (9, 'Tali', 'Talic536', 'Tt12345', 'tal@gmail.com');
INSERT INTO `web-project-g4`.customers (id, user_name, nickname, password, email) VALUES (13, 'Roei', 'roei2107', 'Rr123456', 'Roei@gmail.com');

create table videos
(
    id_video    int auto_increment
        primary key,
    user_id     int           not null,
    audio       varchar(200)  null,
    image       varchar(200)  null,
    sender_name varchar(30)   null,
    card_banner varchar(2500) null,
    color       varchar(20)   null,
    shape       varchar(20)   null,
    video_name  varchar(250)  null,
    dir         bit           null,
    constraint videos_id_video_uindex
        unique (id_video),
    constraint fk_user_id
        foreign key (user_id) references customers (id),
    constraint ck_max_card
        check (octet_length(`card_banner`) <= 2500),
    constraint ck_max_sender
        check (octet_length(`sender_name`) <= 30)
);

INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (1, 1, '', 'happybdaycard.jpeg', 'card4u', 'Happy birthday, dear friend', 'pink', 'butterfly', 'Happy Birthday Card', false);
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (2, 1, 'wedding.mp3', 'wedding.jpeg', 'card4u', 'You are invited to our wedding', '', 'heart', 'Wedding Invitation', false);
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (3, 1, 'web.mp3', 'web.jpeg', 'team4', 'Thank you to all the web course teachers, for a great experience! we really enjoyed the course and we learnt a-lot! :)', 'brown', 'heart', 'Thank you web team', false);
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (4, 6, null, null, null, null, null, null, null, null);
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (5, 6, null, null, 'noa', 'team4check', 'green', 'heart', null, null);
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, video_name, dir) VALUES (6, 5, null, null, 'card4u', 'someblessinghere', null, null, null, null);