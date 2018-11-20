insert into advisors (first_name,last_name,email)
	values ('Fred', 'Stone', 'fred@college.edu');

insert into advisors (first_name,last_name,email)
	values ('Bob', 'Gordon', 'bob@college.edu');

insert into advisors (first_name,last_name,email)
	values ('Jack', 'Simpson', 'jack@college.edu');

select * from advisors;

delete from advisors where advisor_id in (2,3,4,5);

dbcc checkident (advisors, reseed, 0);
