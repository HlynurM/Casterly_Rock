
DROP TABLE IF EXISTS Kingdom cascade;
DROP TABLE IF EXISTS RegionCode cascade;
DROP TABLE IF EXISTS Castle cascade;
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
    rID	SERIAL,	
    PRIMARY KEY(Rid)
);
		
		
CREATE TABLE Castle(
    aID	SERIAL,
    CastleName	VARCHAR(50),
    PRIMARY KEY(aID),
    rID	INT,
    kID	INT,
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
    FOREIGN KEY (aID) REFERENCES Castle
);
		
		
CREATE TABLE Seller(
    sID	SERIAL,
    uID	INT,
	bID INT,
	aID INT,
    PRIMARY KEY(sID),
	FOREIGN KEY (bID) REFERENCES Buyer,
	FOREIGN KEY (aID) REFERENCES Castle,
    FOREIGN KEY (uID) REFERENCES Users
);
		
		
CREATE TABLE Administrator(
    adID SERIAL,
    uID	INT,
    PRIMARY KEY(adID),
	FOREIGN KEY (uID) REFERENCES Users
);		

CREATE TABLE Estate(
    eID	SERIAL,
    type VARCHAR(30),
    squareMeters INT,
    rooms INT,
    dungeon	BOOL,
    moat BOOL,
    aID	INT,
    sID	INT,
	PRIMARY KEY (eID),
    FOREIGN KEY (aID) REFERENCES Castle,
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
