/*Create a mobile phone database */
CREATE DATABASE MOBILE_PHONE_DB;

/*Use Mobile Phone database*/
USE MOBILE_PHONE_DB;

/*Create two tables 
	- Image_table: contains only image url links 
    - Label table: contains only labels
*/

-- Image dataset
CREATE TABLE IMAGE_DS (
	IMAGE_ID INT PRIMARY KEY AUTO_INCREMENT,
    IMAGE_URL VARCHAR(100)
	
);

-- Label dataset
CREATE TABLE LABEL_DS (
	LABEL_ID INT PRIMARY KEY AUTO_INCREMENT,
    LABELS VARCHAR(50)
); 
