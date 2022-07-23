123

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

INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (1, 2, null, null, 'eden', 'tami', 'red', 'triangle', null, 'var');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (3, 4, null, null, 'Aviv', 'Tomi', 'green', 'squre', null, 'songi');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (4, 5, null, null, 'Dan', 'Hili', 'yellow', 'circle', null, 'stars');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (5, 6, null, null, 'Yotam', 'Roni', 'blue', 'rectangle', null, 'moon');
INSERT INTO `web-project-g4`.videos (id_video, user_id, audio, image, sender_name, card_banner, color, shape, dir, video_name) VALUES (6, 7, null, null, 'Yossi', 'Avi', 'orange', 'star', null, 'sunshine');