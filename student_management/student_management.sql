create database student_management;
use student_management;
create table students(
    name varchar(50),
    student_id int primary key,
    course varchar(50),
    year int
);
INSERT INTO students (student_id, name, course, year)
VALUES
(1001, 'Kanupriya', 'CSE', 19),
(1002, 'Priya', 'AIDS', 19),
(1003, 'Sneha', 'CE', 20),
(1004, 'Luv', 'CSE', 21),
(1005, 'Ananya', 'AIDS', 20),
(1006, 'Riya', 'CE', 21),
(1007, 'Aarav', 'CSE', 19),
(1008, 'Ishaan', 'AIDS', 20),
(1009, 'Ananya', 'CE', 21),
(1010, 'Rohan', 'CSE', 19);
SELECT * FROM students;

SELECT name
FROM students
WHERE course= 'CSE';

SELECT name
FROM students
WHERE course = 'CSE' AND year = 21;

SELECT name
FROM students
WHERE course = 'CSE' OR course = 'AIDS';

SELECT name
FROM students
WHERE year > 19;


SELECT * From students
ORDER BY year DESC;

SELECT * From students
ORDER BY year ASC;

SELECT * from students
ORDER BY course, name asc;

SELECT name, course, year from students
ORDER BY year desc;
