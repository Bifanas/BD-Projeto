INSERT INTO administrador VALUES (1,'adm1@email.com', 'senha1', 'adm1');
INSERT INTO administrador VALUES (2,'adm2@email.com', 'senha2', 'adm2');
INSERT INTO administrador VALUES (3,'adm3@email.com', 'senha3', 'adm3');

INSERT INTO cliente VALUES (1, 'cliente1','senha1','c1@email.com','02-05-1958',20);
INSERT INTO cliente VALUES (2, 'cliente2','senha2','c2@email.com','04-05-1985',20);
INSERT INTO cliente VALUES (3, 'cliente3','senha3', 'c3@email.com','15-04-1945',20);

INSERT INTO album VALUES (1, 'album1','1',2001,10,10);
INSERT INTO album VALUES (2, 'album2','2',2002,20,20);
INSERT INTO album VALUES (3, 'album3','3',2003,30,30);
INSERT INTO album VALUES (4, 'album4','4',2004,40,40);
INSERT INTO album VALUES (5, 'album5','5',2005,50,50);
INSERT INTO album VALUES (6, 'album6','6',2006,60,60);
INSERT INTO album VALUES (7, 'album7','7',2007,70,70);
INSERT INTO album VALUES (8, 'album8','8',2008,80,80);
INSERT INTO album VALUES (9, 'album9','9',2009,90,90);
INSERT INTO album VALUES (10, 'album10','10',2010, 100, 100);

INSERT INTO genero VALUES (1,'rap');
INSERT INTO genero VALUES (2,'rock');
INSERT INTO genero VALUES (3, 'pop');
INSERT INTO genero VALUES (4, 'classica');
INSERT INTO genero VALUES (5,'gospel');

INSERT INTO album_genero VALUES (1,1);
INSERT INTO album_genero VALUES (2,2);
INSERT INTO album_genero VALUES (3,3);
INSERT INTO album_genero VALUES (4,4);
INSERT INTO album_genero VALUES (5,5);
INSERT INTO album_genero VALUES (6,1);
INSERT INTO album_genero VALUES (7,2);
INSERT INTO album_genero VALUES (8,3);
INSERT INTO album_genero VALUES (9,4);
INSERT INTO album_genero VALUES (10,5);

INSERT INTO artista VALUES (1, 'artista1');
INSERT INTO artista VALUES (2, 'artista2');
INSERT INTO artista VALUES (3, 'artista3');INSERT INTO artistaVALUES (4, 'artista4');
INSERT INTO artista VALUES (5, 'artista5');

INSERT INTO artista_album VALUES (1, 1);
INSERT INTO artista_album VALUES (2, 2);
INSERT INTO artista_album VALUES (3, 3);
INSERT INTO artista_album VALUES (4, 4);
INSERT INTO artista_album VALUES (5, 5);
INSERT INTO artista_album VALUES (1, 6);
INSERT INTO artista_album VALUES (2, 7);
INSERT INTO artista_album VALUES (3, 8);
INSERT INTO artista_album VALUES (4, 9);
INSERT INTO artista_album VALUES (5, 10);

INSERT INTO MUSICA VALUES (1, 'musica1');
INSERT INTO MUSICA VALUES (2, 'musica2');
INSERT INTO MUSICA VALUES (3, 'musica3');
INSERT INTO MUSICA VALUES (4, 'musica4');
INSERT INTO MUSICA VALUES (5, 'musica5');
INSERT INTO MUSICA VALUES (6, 'musica6');
INSERT INTO MUSICA VALUES (7, 'musica7');
INSERT INTO MUSICA VALUES (8, 'musica8');
INSERT INTO MUSICA VALUES (9, 'musica9');
INSERT INTO MUSICA VALUES (10, 'musica10');
INSERT INTO MUSICA VALUES (11, 'musica11');
INSERT INTO MUSICA VALUES (12, 'musica12');
INSERT INTO MUSICA VALUES (13, 'musica13');
INSERT INTO MUSICA VALUES (14, 'musica14');
INSERT INTO MUSICA VALUES (15, 'musica15');
INSERT INTO MUSICA VALUES (16, 'musica16');
INSERT INTO MUSICA VALUES (17, 'musica17');
INSERT INTO MUSICA VALUES (18, 'musica18');
INSERT INTO MUSICA VALUES (19, 'musica19');
INSERT INTO MUSICA VALUES (20, 'musica20');

INSERT INTO musica_Album VALUES (1,1);
INSERT INTO musica_Album VALUES (2,1);
INSERT INTO musica_Album VALUES (3,2);
INSERT INTO musica_Album VALUES (4,2);
INSERT INTO musica_Album VALUES (5,3);
INSERT INTO musica_Album VALUES (6,3);
INSERT INTO musica_Album VALUES (7,4);
INSERT INTO musica_Album VALUES (8,4);
INSERT INTO musica_Album VALUES (9,5);
INSERT INTO musica_Album VALUES (10,5);
INSERT INTO musica_Album VALUES (11,6);
INSERT INTO musica_Album VALUES (12,6);
INSERT INTO musica_Album VALUES (13,7);
INSERT INTO musica_Album VALUES (14,7);
INSERT INTO musica_Album VALUES (15,8);
INSERT INTO musica_Album VALUES (16,8);
INSERT INTO musica_Album VALUES (17,9);
INSERT INTO musica_Album VALUES (18,9);
INSERT INTO musica_Album VALUES (19,10);
INSERT INTO musica_Album VALUES (20,10);

INSERT INTO historico_c
VALUES(1, '2010-02-02', 1);

INSERT INTO historico_c
VALUES(2, '2010-02-02', 1);

INSERT INTO historico_c
VALUES(3, '2010-02-02', 2);

INSERT INTO historico_c
VALUES(4, '2010-02-02', 3);

INSERT INTO historico_c
VALUES(5, '2010-02-02', 4);

INSERT INTO historico_c
VALUES(6, '2010-02-02', 5);

INSERT INTO historico_c_album
VALUES(1, 1);

INSERT INTO historico_c_album
VALUES(2, 1);

INSERT INTO historico_c_album
VALUES(3, 2);

INSERT INTO historico_c_album
VALUES(4, 3);

INSERT INTO historico_c_album
VALUES(5, 4);

INSERT INTO historico_c_album
VALUES(6, 5);