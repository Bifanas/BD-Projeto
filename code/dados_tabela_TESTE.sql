delete from historico_a;
delete from album_genero;
delete from musica_album;
delete from artista_album;
delete from artista;
delete from genero;
delete from musica;
delete from c_entrada;
delete from notificacao;
delete from historico_c_album;
delete from historico_c;
delete from pedido;
delete from album;

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

INSERT INTO genero VALUES (1,'rap');
INSERT INTO genero VALUES (2,'rock');
INSERT INTO genero VALUES (3, 'pop');
INSERT INTO genero VALUES (4, 'classica');
INSERT INTO genero VALUES (5,'gospel');

INSERT INTO album_genero VALUES (1,1);
INSERT INTO album_genero VALUES (1,2);
INSERT INTO album_genero VALUES (2,2);
INSERT INTO album_genero VALUES (2,3);
INSERT INTO album_genero VALUES (3,3);
INSERT INTO album_genero VALUES (3,4);
INSERT INTO album_genero VALUES (4,4);
INSERT INTO album_genero VALUES (4,5);
INSERT INTO album_genero VALUES (5,5);

INSERT INTO artista VALUES (1, 'artista1');
INSERT INTO artista VALUES (2, 'artista2');
INSERT INTO artista VALUES (3, 'artista3');
INSERT INTO artistaVALUES  (4, 'artista4');
INSERT INTO artista VALUES (5, 'artista5');

INSERT INTO artista_album VALUES (1, 1);
INSERT INTO artista_album VALUES (2, 2);
INSERT INTO artista_album VALUES (3, 3);
INSERT INTO artista_album VALUES (4, 4);
INSERT INTO artista_album VALUES (5, 5);

INSERT INTO MUSICA VALUES (1, 'musica1');
INSERT INTO MUSICA VALUES (2, 'musica2');
INSERT INTO MUSICA VALUES (3, 'musica3');
INSERT INTO MUSICA VALUES (4, 'musica4');
INSERT INTO MUSICA VALUES (5, 'musica5');

INSERT INTO musica_Album VALUES (1,1);
INSERT INTO musica_Album VALUES (2,2);
INSERT INTO musica_Album VALUES (3,3);
INSERT INTO musica_Album VALUES (4,4);
INSERT INTO musica_Album VALUES (5,5);

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

delete from historico_a;
delete from album_genero;
delete from musica_album;
delete from artista_album;
delete from artista;
delete from genero;
delete from musica;
delete from c_entrada;
delete from notificacao;
delete from historico_c_album;
delete from historico_c;
delete from pedido;
delete from album;
