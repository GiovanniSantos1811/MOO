--INSERINDO DADOS NAS TABELAS

--INSERINDO NA TABELA PERFIL_JOGADOR
INSERT INTO PERFIL_JOGADOR VALUES (3770607060, 'Danete', 'Pedro Zenatte', TO_DATE('27/07/2002', 'DD/MM/YYYY'),
                                    'Masculino', 'Brasileiro'); 
INSERT INTO PERFIL_JOGADOR VALUES (4770607060, 'Pochete', 'Marcelo Eduardo', TO_DATE('19/08/2003', 'DD/MM/YYYY'),
                                    'Masculino', 'Brasileiro'); 
INSERT INTO PERFIL_JOGADOR VALUES (5770607060, 'Golias', 'Giovanni dos Santos', TO_DATE('18/11/2003', 'DD/MM/YYYY'),
                                    'Masculino', 'Brasileiro');
INSERT INTO PERFIL_JOGADOR VALUES (6770607060, 'Bomber', 'Guilherme Augusto', TO_DATE('11/09/2003', 'DD/MM/YYYY'),
                                    'Masculino', 'Brasileiro');


--INSERINDO NA TABELA JOGO
INSERT INTO JOGO VALUES ('The Legend of Zelda: Breath of the Wild', 'Aventura/RPG', 'Nintendo', 'Nintendo', TO_DATE('03/03/2017', 'DD/MM/YYYY'), 
                            10); 
INSERT INTO JOGO VALUES ('Call of Duty: Modern Warfare II', 'FPS', 'Infinity Ward', 'Activision', TO_DATE('28/10/2022', 'DD/MM/YYYY'), 
                            18);
INSERT INTO JOGO VALUES ('Minecraft', 'Sandbox', 'Mojang Studios', 'Mojang Studios', TO_DATE('18/11/2011', 'DD/MM/YYYY'),
                            0);
INSERT INTO JOGO VALUES ('GTA V', 'Ação/Mundo Aberto', 'Rockstar', 'Rockstar', TO_DATE('17/09/2013', 'DD/MM/YYYY'),
                            18);

--INSERINDO NA TABELA CONVITE
INSERT INTO CONVITE VALUES (3770607060, 4770607060, 'Minecraft', TO_DATE('11/12/2024', 'DD/MM/YYYY'), 
                            'Ow, bora joga mine com mods ai');
INSERT INTO CONVITE VALUES (3770607060, 5770607060, 'Minecraft', TO_DATE('11/12/2024', 'DD/MM/YYYY'), 
                            'Vamo joga mine com mods');
INSERT INTO CONVITE VALUES (5770607060, 6770607060, 'GTA V', TO_DATE('11/12/2024', 'DD/MM/YYYY'), 
                            'Bora rusha nas missões');
INSERT INTO CONVITE VALUES (4770607060, 5770607060, 'Call of Duty: Modern Warfare II', TO_DATE('11/12/2024', 'DD/MM/YYYY'), 
                            'Um fpszinho ai?');

--INSERINDO NA TABELA JOGOS_JOGADOR
INSERT INTO JOGOS_JOGADOR VALUES ('Minecraft', 3770607060);
INSERT INTO JOGOS_JOGADOR VALUES ('Minecraft', 5770607060);
INSERT INTO JOGOS_JOGADOR VALUES ('GTA V', 6770607060);
INSERT INTO JOGOS_JOGADOR VALUES ('GTA V', 4770607060);

COMMIT;

rollback;


