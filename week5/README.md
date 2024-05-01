# Task 2
### Create a new database named website.
```sql
CREATE database website;
```
![alt text](image.png)
### Create a new table named member, in the website database.
```sql
CREATE TABLE website.member (
    id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    name VARCHAR(255) NOT NULL COMMENT 'Name',
    username VARCHAR(255) NOT NULL COMMENT 'Username',
    password VARCHAR(255) NOT NULL COMMENT 'Password',
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
);
```
![alt text](image-1.png)
# Task 3
### INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
```sql
INSERT INTO website.member (name, username, password, follower_count)
VALUES ('test', 'test', 'test',1);
INSERT INTO website.member (name, username, password, follower_count)
VALUES ('Apple', 'apple', '123',2),
       ('Banana', 'banana', '123',3),
       ('Kiwi', 'kiwi', '123',4),
       ('Grape', 'grape', '123',5);
```
![alt text](image-2.png)
![alt text](image-3.png)
### SELECT all rows from the member table.
```sql
SELECT * FROM website.member;
```
![alt text](image-4.png)
### SELECT all rows from the member table, in descending order of time.

```sql
SELECT * FROM website.member ORDER BY time DESC;
```
![alt text](image-5.png)
### SELECT total 3 rows, second to fourth, from the member table, in descending order of time.
```sql
SELECT * FROM website.member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![alt text](image-6.png)
### SELECT rows where username equals to test.
```sql
SELECT * FROM website.member WHERE username = 'test';
```
![alt text](image-7.png)
### SELECT rows where name includes the es keyword
```sql
SELECT * FROM website.member WHERE name LIKE '%es%';
```
![alt text](image-8.png)
### SELECT rows where both username and password equal to test.
```sql
SELECT * FROM website.member WHERE username = 'test' AND password = 'test';
```
![alt text](image-9.png)
### UPDATE data in name column to test2 where username equals to test.
```sql
UPDATE website.member
SET name = 'test2'
WHERE username = 'test';
```
![alt text](image-10.png)
# Task 4
### SELECT how many rows from the member table.
```sql
SELECT COUNT(*) FROM website.member;
```
![alt text](image-11.png)
### SELECT the sum of follower_count of all the rows from the member table.
```sql
SELECT SUM(follower_count) FROM website.member;
```
![alt text](image-12.png)
### SELECT the average of follower_count of all the rows from the member table.
```sql
SELECT AVG(follower_count) AS average_followers
FROM website.member;
```
![alt text](image-14.png)
### SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
SELECT AVG(follower_count) AS average_followers
FROM (SELECT follower_count
      FROM website.member
      ORDER BY follower_count DESC
      LIMIT 2) AS top2_followers;
```
![alt text](image-13.png)
# Task 5
### Create a new table named message, in the website database.
```sql
CREATE TABLE website.message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
    content VARCHAR(255) NOT NULL COMMENT 'Content',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
    FOREIGN KEY (member_id) REFERENCES website.member(id)
);
INSERT INTO website.message (member_id, content, like_count)
VALUES (1, 'hello', 10),
       (2, 'hello', 20),
       (3, 'hello', 30),
       (4, 'hello', 40),
       (5, 'hello', 50);
```
### SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
SELECT * 
FROM website.message 
JOIN website.member ON website.message.member_id = website.member.id
```
![alt text](image-15.png)
### SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```sql
SELECT * 
FROM website.message 
JOIN website.member ON website.message.member_id = website.member.id
WHERE website.member.username = 'test';
```
![alt text](image-16.png)
### Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql
SELECT website.member.username, AVG(website.message.like_count) AS average_likes
FROM website.message
JOIN website.member ON website.message.member_id = website.member.id
WHERE website.member.username = 'test';
```
![alt text](image-17.png)
### Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql
SELECT website.member.username, AVG(website.message.like_count) AS average_likes
FROM website.message
JOIN website.member ON website.message.member_id = website.member.id
GROUP BY website.member.username
```
![alt text](image-18.png)

