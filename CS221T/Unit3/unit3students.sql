insert into students (first_name,last_name,dob,gender,student_start_dt,gpa,is_active,advisor_id)
	values ('Craig', 'Franklin', '1970-03-15', 'm', '2010-05-30', 3.10, 1, 3);

insert into students (first_name,last_name,dob,gender,student_start_dt,gpa,is_active,advisor_id)
	values ('Harriet', 'Smith', '1982-04-15', 'f', '2010-05-30', 3.22, 1, 1);

insert into students (first_name,last_name,dob,gender,student_start_dt,gpa,is_active,advisor_id)
	values ('George', 'David', '1984-11-05', 'm', '2010-10-01', 0.00, 1, 3);

insert into students (first_name,last_name,dob,gender,student_start_dt,gpa,is_active,advisor_id, bio)
	values ('Ben', 'Jefferson', '1976-09-25', 'm', '2009-02-21', 1.80, 0, 3, 'The student has gone on temporary leave to pursue other opportunities but plans on returning in 1 year.');

select * from students;

ALTER TABLE students
ALTER COLUMN gpa decimal(3,2);

update students set gpa = 3.25 where student_id = 3;

update students set dob = '1982-04-25' where student_id = 3;

delete from students where student_id in (2,3,4,5);

dbcc checkident (students, reseed, 0);
