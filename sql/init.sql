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

-- CREATE FIELD "created_at" -----------------------------------
ALTER TABLE `matches` ADD COLUMN `created_at` DateTime NULL;
-- -------------------------------------------------------------

-- CREATE FIELD "updated_at" -----------------------------------
ALTER TABLE `matches` ADD COLUMN `updated_at` DateTime NULL;
-- -------------------------------------------------------------

-- CREATE TABLE "players" --------------------------------------
CREATE TABLE `players` ( 
	`id` BigInt( 20 ) AUTO_INCREMENT NOT NULL,
	`rank` Int( 255 ) NULL,
	`name` VarChar( 255 ) NULL,
	`player_id` Int( 11 ) NULL,
	`region` VarChar( 255 ) NULL,
	`matches` Int( 255 ) NULL,
	`win_rate` Double( 8, 2 ) NULL DEFAULT '0',
	`core` Double( 8, 2 ) NULL DEFAULT '0',
	`support` Double( 8, 2 ) NULL DEFAULT '0',
	`core_off` Double( 8, 2 ) NULL DEFAULT '0',
	`core_mid` Double( 8, 2 ) NULL DEFAULT '0',
	`core_safe` Double( 8, 2 ) NULL DEFAULT '0',
	`created_at` DateTime NULL,
	`updated_at` DateTime NULL,
	PRIMARY KEY ( `id` ) )
ENGINE = InnoDB;
-- -------------------------------------------------------------
