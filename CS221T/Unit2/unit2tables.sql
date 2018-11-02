create table students 
(
	student_id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	/*date of birth*/
	dob date NOT NULL,
	gender varchar(10) NOT NULL,
	student_start_dt date NOT NULL,
	gpa decimal(2),
	is_active bit,
	bio text, /*assuming this is student biography. assigning text type as that hold 2GB memory*/
	advisor_id int NOT NULL /*FOREIGN KEY references advisors(advisor_id)*/
);

create table advisors
(
	advisor_id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	email varchar(255) NOT NULL
);

create table classes
(
	class_id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	class_code varchar(25),
	class_name varchar(50),
	class_description text
);

create table student_classes
(
	student_class_id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	student_id int NOT NULL, /*FOREIGN KEY references students(student_id)*/
	class_id int NOT NULL, /*FOREIGN KEY references classes(class_id)*/
	class_start_dt date NOT NULL, /*start date of class != student start date. no reference made*/
	assignment_1 tinyint NOT NULL,
	assignment_2 tinyint NOT NULL,
	assignment_3 tinyint NOT NULL,
	assignment_4 tinyint NOT NULL,
	class_gpa decimal(2)
);
/*ALL FOREIGN KEYS WILL BE EXECUTED IN THE SECOND SCRIPT FILE TO CONSERVE SPACE
SECOND SCREENSHOT WILL CONTAIN EXPANDED VIEW OF STUDENTS TABLE*/
