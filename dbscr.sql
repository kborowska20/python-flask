BEGIN TRANSACTION;

DROP TABLE if EXISTS todolist;

CREATE TABLE "todolist" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
  `done` TEXT,
);

INSERT INTO `todolist` (id,name,done) VALUES (1, 'BUY MILK', 'True'),
(2, 'GO TO SHOP', 'FALSE');
COMMIT;