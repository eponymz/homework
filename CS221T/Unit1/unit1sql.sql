create database unit1_dbwithtables

create schema unit1_schema

create table unit1_dbwithtables.unit1_schema.sample_table
(
  sample int default null ,
  column_2 varchar(25) default null
)

INSERT INTO [unit1_dbwithtables].[unit1_schema].[sample_table]
  ([sample], [column_2])
VALUES
  (12, 'hello')

INSERT INTO [unit1_dbwithtables].[unit1_schema].[sample_table]
  ([sample], [column_2])
VALUES
  (12, 'sample entry #2')

select *
from unit1_schema.sample_table;
