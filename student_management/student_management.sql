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







create table marks(
mark_id int primary key,
student_id int,
subject varchar(50),
marks int,
FOREIGN KEY (student_id)
REFERENCES students(student_id)
 );
INSERT INTO marks (mark_id, student_id, subject, marks)
VALUES
(1, 1001, 'DBMS', 88),
(2, 1001, 'Python', 92),
(3, 1001, 'CS', 81),
(4, 1001, 'DSA', 62),
(5, 1002, 'DBMS', 81),
(6, 1002, 'Python', 85),
(7, 1002, 'CS', 45),
(8, 1002, 'DSA', 100),
(9, 1003, 'DBMS', 76),
(10, 1003, 'CS', 33),
(11, 1003, 'DSA', 71),
(12, 1003, 'Python', 100);
INSERT INTO marks (mark_id, student_id, subject, marks)
VALUES
(13, 1004, 'DBMS', 78),
(14, 1004, 'Python', 84),
(15, 1004, 'CS', 72),
(16, 1004, 'DSA', 69),

(17, 1005, 'DBMS', 91),
(18, 1005, 'Python', 87),
(19, 1005, 'CS', 79),
(20, 1005, 'DSA', 88),

(21, 1006, 'DBMS', 74),
(22, 1006, 'Python', 81),
(23, 1006, 'CS', 68),
(24, 1006, 'DSA', 77),

(25, 1007, 'DBMS', 85),
(26, 1007, 'Python', 90),
(27, 1007, 'CS', 82),
(28, 1007, 'DSA', 94),

(29, 1008, 'DBMS', 88),
(30, 1008, 'Python', 76),
(31, 1008, 'CS', 84),
(32, 1008, 'DSA', 80),

(33, 1009, 'DBMS', 71),
(34, 1009, 'Python', 79),
(35, 1009, 'CS', 73),
(36, 1009, 'DSA', 68),

(37, 1010, 'DBMS', 93),
(38, 1010, 'Python', 89),
(39, 1010, 'CS', 91),
(40, 1010, 'DSA', 95);




#-----------joins--------------------

select name, course,marks,subject from students
inner join marks
on marks.student_id= students.student_id;

#------------avg()marks-----------------------
select name ,avg( marks) from students  
inner join marks  on marks.student_id =students.student_id
group by name;

#---------------name of student with highest marks--------
select name , max(marks) as highest_marks from students 
inner join marks on marks.student_id=students.student_id
group by name;
#-----------avergae marks in course--------------
select course, avg(marks) from students 
inner join marks on marks.student_id=students.student_id
group by course;

#------------having query --------
select course, avg(marks) from students 
inner join marks on marks.student_id=students.student_id
group by course
having avg(marks)>80;

#--------------student performance report--------# 

select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students 
inner join marks on marks.student_id=students.student_id
group by name;
 #---------------top performing students-------------#
 select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students 
inner join marks on marks.student_id=students.student_id
group by name
having avg(marks)>80;
#--------------asec desc report ----------------------#
select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students 
inner join marks on marks.student_id=students.student_id
group by name
order by avg(marks) desc;

#-----------------subject-wise performance------------#
select   subject, avg(marks)as Avergae_marks from students
inner join marks on marks.student_id=students.student_id
group by subject;

#-----------students who failed in any subject------------
select name as student, subject ,marks from students 
inner join marks on marks.student_id=students.student_id
where marks <40;

#-----------student with highest avg report--------------#
select name as student, avg(marks) from students 
inner join marks on marks.student_id=students.student_id
group by name 
order by avg(marks) desc limit 1;

select * from students;

