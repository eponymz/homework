/* List all active male students assigned to Advisors 1 or 3 (Fred Stone or Jack Simpson). */
select * from students where advisor_id in (1, 3) AND is_active = 1 AND gender = 'm';

/* Provide a list of all students without a biography. */
select * from students where bio IS NULL;

/* What classes are in the English department? */
select * from classes where class_code LIKE '%ENG%';

/*
Create a list of all students and their advisors. 
Sort by the advisor’s name and then the student’s name. Include the student’s birth date, gender, and GPA.
*/
select a.first_name, a.last_name, s.first_name, s.last_name, s.dob, s.gender, s.gpa
	from students s
join advisors a on s.advisor_id = a.advisor_id
	ORDER BY a.first_name DESC, s.first_name;

/* How many students were born in the 1980s? */
select count(*) from students where dob like '%198%';

/* Write a query to show the average GPA by gender. */
select gender, avg(gpa) from students group by gender;

/*
Provide a list of all advisors and the number of active students assigned to each. 
Filter out any advisors with more than 1 student.
*/
select a.first_name, count(*)
	from advisors a
join students s on s.advisor_id = a.advisor_id
	where s.is_active = 1
	group by a.first_name
	having count(*) <= 1;
