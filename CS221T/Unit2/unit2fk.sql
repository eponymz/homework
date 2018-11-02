ALTER TABLE students
ADD CONSTRAINT FK_studentAdvisor
FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id)

ALTER TABLE student_classes
ADD CONSTRAINT FK_studentClasses
FOREIGN KEY (class_id) REFERENCES classes(class_id)

ALTER TABLE students
DROP COLUMN gender
GO

ALTER TABLE students
ADD gender char(1) NOT NULL
GO
