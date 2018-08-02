-- CREATE TABLE "matches" --------------------------------------
CREATE TABLE `matches` ( 
	`id` BigInt( 20 ) UNSIGNED AUTO_INCREMENT NOT NULL,
	`mode` VarChar( 255 ) NULL COMMENT 'All Random, Single Draft',
	`range_type` VarChar( 255 ) NULL COMMENT 'Normal matchmaking',
	`match_id` BigInt( 20 ) NOT NULL,
	`winner_type` VarChar( 255 ) NULL COMMENT 'dire, radiant',
	`winner_region` VarChar( 255 ) NULL COMMENT 'russia, china',
	`duration` Int( 11 ) NOT NULL DEFAULT '0' COMMENT 'seconds',
	`duration_string` VarChar( 255 ) NULL,
	`radiant_heroes` JSON NULL,
	`dire_heroes` JSON NULL,
	`date` DateTime NULL,
	`league_id` Int( 11 ) NULL,
	`league_name` Int( 255 ) NULL,
	PRIMARY KEY ( `id` ) )
ENGINE = InnoDB;
-- -------------------------------------------------------------
