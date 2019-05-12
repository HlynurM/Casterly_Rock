INSERT INTO Kingdom (kID, name) VALUES (1,'The North');
INSERT INTO Kingdom (kID, name) VALUES (2,'The Iron Islands');
INSERT INTO Kingdom (kID, name) VALUES (3,'The Riverlands');
INSERT INTO Kingdom (kID, name) VALUES (4,'The Vale of Arryn');
INSERT INTO Kingdom (kID, name) VALUES (5,'The Westerlands');
INSERT INTO Kingdom (kID, name) VALUES (6,'The Reach');
INSERT INTO Kingdom (kID, name) VALUES (7,'The Stormlands');
INSERT INTO Kingdom (kID, name) VALUES (8,'The Crownlands');
INSERT INTO Kingdom (kID, name) VALUES (9,'Dorne');


INSERT INTO RegionCode(rID) VALUES (101); -- the north
INSERT INTO RegionCode(rID) VALUES (102); -- the north
INSERT INTO RegionCode(rID) VALUES (103); -- the north
INSERT INTO RegionCode(rID) VALUES (104); -- the iron islands
INSERT INTO RegionCode(rID) VALUES (105); -- the riverlands
INSERT INTO RegionCode(rID) VALUES (106); -- the vale of arryn
INSERT INTO RegionCode(rID) VALUES (107); -- the westerlands
INSERT INTO RegionCode(rID) VALUES (108); -- the reach
INSERT INTO RegionCode(rID) VALUES (109); -- the reach
INSERT INTO RegionCode(rID) VALUES (110);-- the stormlands
INSERT INTO RegionCode(rID) VALUES (111);-- the stormlands
INSERT INTO RegionCode(rID) VALUES (112); -- the stormlands
INSERT INTO RegionCode(rID) VALUES (113); -- the stormlands
INSERT INTO RegionCode(rID) VALUES (170); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (200); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (201); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (202); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (203); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (210); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (211); -- the crownlands
INSERT INTO RegionCode(rID) VALUES (220); -- Dorne
INSERT INTO RegionCode(rID) VALUES (221); -- Dorne
INSERT INTO RegionCode(rID) VALUES (230); -- Dorne
INSERT INTO RegionCode(rID) VALUES (231); -- Dorne
INSERT INTO RegionCode(rID) VALUES (240); -- Dorne
INSERT INTO RegionCode(rID) VALUES (241); -- Dorne


INSERT INTO Residence (aID, Residence, rID, kId) VALUES (1,'Winterfell',101, 1); -- Eddard Stark (1)
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (2,'Moat Cailing',102, 1); -- Roose Bolton (2)
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (3,'Riverrun',105,3); -- Jane Doe
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (4,'Runestone',106,4); -- John door
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (5,'Casterly Rock',107,5); --  Tyrian Lannister
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (6,'Highgarden',108,6); --Andrea Andrésdóttir
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (7,'Storm´s_End',111,7); -- Andrés Magnússon
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (8,'Red Keep',170,8); --Tinni Tíbet
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (9,'Sunspear', 231,9); -- Tinna Tíbet
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (10,'Ten Towers',104,2); -- Jóna
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (11,'Placeholder 2',109,6); -- Jóhannes
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (12,'Placeholder 3',200,8); -- Birta
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (13,'Placeholder 4',210,8); -- Björn
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (14,'Placeholder 5',110,7); -- Magnea
INSERT INTO Residence (aID, Residence, rID, kId) VALUES (15,'Placeholder 6', 201,8); -- Magnús


INSERT INTO CreditCard (crID, crNumber) values (1,'1234-1234-1234-1234'); --Eddard Stark
INSERT INTO CreditCard (crID, crNumber) values (2,'2345-2345-2345-2345'); --Roose Bolton
INSERT INTO CreditCard (crID, crNumber) values (3,'3456-3456-3456-3456'); --Tyrion Lannister
INSERT INTO CreditCard (crID, crNumber) values (4,'4567-4567-4567-4567'); --Jane Doe
INSERT INTO CreditCard (crID, crNumber) values (5,'5678-5678-5678-5678'); --John Door
INSERT INTO CreditCard (crID, crNumber) values (6,'6789-6789-6789-6789'); --Jóna Jónsdóttir
INSERT INTO CreditCard (crID, crNumber) values (7,'7890-7890-7890-7890'); --Jóhannes Jónasson
INSERT INTO CreditCard (crID, crNumber) values (8,'9876-9876-9876-9876'); --Birta Bárudóttir
INSERT INTO CreditCard (crID, crNumber) values (9,'8765-8765-8765-8765'); --Björn Birtuson
INSERT INTO CreditCard (crID, crNumber) values (10,'7654-7654-7654-7654'); -- Andrea Andrésdóttir
INSERT INTO CreditCard (crID, crNumber) values (11,'6543-6543-6543-6543'); --Jóna Jónsdóttir
INSERT INTO CreditCard (crID, crNumber) values (12,'5432-5432-5432-5432'); --Jóhannes Jónasson
INSERT INTO CreditCard (crID, crNumber) values (13,'4321-4321-4321-4321'); --Birta Bárudóttir
INSERT INTO CreditCard (crID, crNumber) values (14,'1212-1212-1212-1212'); --Björn Birtuson
INSERT INTO CreditCard (crID, crNumber) values (15,'2323-2323-2323-2323'); -- Andrea Andrésdóttir

	
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (1, 'Eddard', 'Stark', '123456-7890', 'nedstark@winterfell.com', 555);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (2, 'Roose', 'Bolton', '654322-2342', 'bastard@bolton.com', 666);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (3, 'Tyrion', 'Lannister', '838383-3838', 'imp@lannisters.com', 111);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (4, 'Jane','Doe', '333333-3333', 'doe@jane.com', 123);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (5, 'John', 'Door', '123431-1212', 'doory@john.com', 124);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (6, 'Jóna', 'Jónsdóttir', '939393-2323', 'jona@jonsdottir.com', 125);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (7, 'Jóhannes', 'Jónasson', '444444-4444', 'jonasson@johannes.com', 126);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (8, 'Birta', 'Bárudóttir', '222222-2222','birta@barudottir.com', 127);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (9, 'Björn', 'Birtuson', '101010-8383', 'birtuson@bara.com', 128);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (10,'Magnús', 'Magnússon', '324342-2433', 'maggi@magg.com', 129);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (11, 'Magnea', 'Magnúsdóttir', '234232-3422', 'magnea@magg.com', 130);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (12, 'Andrea', 'Andrésdóttir', '757575-4747', 'andrea@andr.com', 131);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (13, 'Andrés', 'Magnússon', '234232-2322', 'andres@andr.com', 132);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (14, 'Tinni', 'Tíbet', '010101-1010', 'tinni@tinni.com', 133);
INSERT INTO Users(uID, Firstname, Surname, SSN, email, pidgeonNo) VALUES (15, 'Tinna', 'Tíbet', '939393-2322', 'tinna@tinni.com', 134);


INSERT INTO Buyer (bID, uID, aID, crID) VALUES (1,3,5,3); -- serial, user no, residence no, creditcard no
INSERT INTO Buyer (bID, uID, aID, crID) VALUES (2,2,2,2);
INSERT INTO Buyer (bID, uID, aID, crID) VALUES (3,4,3,4);
INSERT INTO Buyer (bID, uID, aID, crID) VALUES (4,5,4,5);
INSERT INTO Buyer (bID, uID, aID, crID) VALUES (5,12,7,10);
	
	
INSERT INTO Seller (sID, uID, aID, crID) VALUES (1,1,1,1); -- serial, user no, residence no, creditcard no
INSERT INTO Seller (sID, uID, aID, crID) VALUES (2,6,10,5); -- 
INSERT INTO Seller (sID, uID, aID, crID) VALUES (3,7,11,12);
INSERT INTO Seller (sID, uID, aID, crID) VALUES (4,8,12,8);
INSERT INTO Seller (sID, uID, aID, crID) VALUES (5,9,13,9);
		

INSERT INTO Administrator (adID, uID) VALUES (1,10);
INSERT INTO Administrator (adID, uID) VALUES (2,11);


-- motte and bailey castle, the stone keep castle, and the concentric castle. - búa til nýja töflu fyrir þessar upplýsingar

INSERT INTO Estate (eID, type, squareMeters, rooms, dungeon, moat, aID, sID) VALUES (1,'motte and bailey',10000,100,false,false,1,1); -- seria, type, m2, no. of rooms, bool, bool, castle for sale, seller no.
INSERT INTO Estate (eID, type, squareMeters, rooms, dungeon, moat, aID, sID) VALUES (2,'stone keep',9000, 90, false, true, 10,2);
INSERT INTO Estate (eID, type, squareMeters, rooms, dungeon, moat, aID, sID) VALUES (3,'concentric',13000, 85, true, false,11,3);
INSERT INTO Estate (eID, type, squareMeters, rooms, dungeon, moat, aID, sID) VALUES (4,'motte and bailey',11500, 115, true, true,12,4);
INSERT INTO Estate (eID, type, squareMeters, rooms, dungeon, moat, aID, sID) VALUES (5,'stone keep',8500, 77, false, false,13,5);


INSERT INTO Buys (buID, price, bID, sID, eID) VALUES (1,6500000,1,1,1); -- serial, price, buyer, selle, castle for sale
INSERT INTO Buys (buID, price, bID, sID, eID) VALUES (2,13000000,2,10,2);
INSERT INTO Buys (buID, price, bID, sID, eID) VALUES (3,2500000,3,11,3);
INSERT INTO Buys (buID, price, bID, sID, eID) VALUES (4,1999999,4,12,4);
INSERT INTO Buys (buID, price, bID, sID, eID) VALUES (5,4000000,5,13,5);
		