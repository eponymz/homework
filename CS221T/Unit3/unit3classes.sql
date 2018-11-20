insert into classes (class_code, class_name, class_description)
	values ('ACCT306','Accounting 1','This course introduces accounting concepts and explores the accounting environment. It covers the basic structure of accounting, how to maintain accounts, use account balances to prepare financial statements, and complete the accounting cycle. It also introduces the concept of internal control and how to account for assets.');

insert into classes (class_code, class_name, class_description)
	values ('CS362','Structured Query Language for Data Management','This course gives complete coverage of SQL, with an emphasis on storage, retrieval, and manipulation of data.');

insert into classes (class_code, class_name, class_description)
	values ('ENG115','English Composition','In this course, students focus on developing writing skills through practice and revision. Students will examine expository, critical, and persuasive essay techniques.');

insert into classes (class_code, class_name, class_description)
	values ('FIN322','Investments','This course focuses on investments and investment strategies. Various investment vehicles such as stocks, bonds, and commodities are examined. Students will explore the principles of security analysis and valuation.');

select * from classes;

delete from classes where class_name='Investments';
