-- kl. 10.43 - 11.5.2019

DROP TABLE IF EXISTS Kingdom cascade;
DROP TABLE IF EXISTS RegionCode cascade;
DROP TABLE IF EXISTS Residence cascade;
DROP TABLE IF EXISTS CreditCard cascade;
DROP TABLE IF EXISTS Users cascade;
DROP TABLE IF EXISTS Buyer cascade;
DROP TABLE IF EXISTS Seller cascade;
DROP TABLE IF EXISTS Administrator cascade;
DROP TABLE IF EXISTS Estate cascade;
DROP TABLE IF EXISTS Buys cascade;


CREATE TABLE Kingdom(
    kID	serial,
    NAME VARCHAR(50),
    PRIMARY KEY(kID)
);
		
		
CREATE TABLE RegionCode(
    rID INT,	
    PRIMARY KEY(rID)
);
		
		
CREATE TABLE Residence(
    aID	SERIAL,
    Residence VARCHAR(50),
    rID	INT,
    kID	INT,
    PRIMARY KEY(aID),
    FOREIGN KEY (rID) REFERENCES RegionCode,
    FOREIGN KEY (kID) REFERENCES Kingdom
);
		
		
CREATE TABLE CreditCard(
    crID SERIAL,
    crNumber VARCHAR(19),
    PRIMARY KEY (crID)
);

CREATE TABLE Users(
    uID	serial,
    FirstName VARCHAR(30),
    Surname	VARCHAR(30),
    SSN	VARCHAR(11)	UNIQUE,
    email VARCHAR(50),
    pidgeonNo INT,
    PRIMARY KEY (uID)
);
		
		
CREATE TABLE Buyer(
    bID	SERIAL,
    uID INT,
	aID INT,
	crID INt,
    PRIMARY KEY(bID),
    FOREIGN KEY (uID) REFERENCES Users,
	FOREIGN KEY (crID) REFERENCES CreditCard,
    FOREIGN KEY (aID) REFERENCES Residence
);
		
		
CREATE TABLE Seller(
    sID	SERIAL,
    uID	INT,
	aID INT,
    crID INT,
    PRIMARY KEY(sID),
    FOREIGN KEY (uID) REFERENCES Users,
	FOREIGN KEY (crID) REFERENCES CreditCard,
    FOREIGN KEY (aID) REFERENCES Residence
);
		
		
CREATE TABLE Administrator(
    adID SERIAL,
    uID	INT,
    PRIMARY KEY(adID),
	FOREIGN KEY (uID) REFERENCES Users
);		

CREATE TABLE Estate(
    eID	SERIAL,
    type VARCHAR(30), --þarf að vera sér tafla
    squareMeters INT,
    rooms INT,
    dungeon	BOOL,
    moat BOOL,
    aID	INT,
    sID	INT,
	PRIMARY KEY (eID),
    FOREIGN KEY (aID) REFERENCES Residence,
    FOREIGN KEY (sID) REFERENCES Seller
);
		
CREATE TABLE Buys(
    buID SERIAL,
    Price INT,
    bID	INT,
    sID	INT,
    eID	INT,
    PRIMARY KEY (buID),
    FOREIGN KEY (bID) REFERENCES Buyer,
    FOREIGN KEY (sID) REFERENCES Seller,
    FOREIGN KEY (eID) REFERENCES Estate
);
