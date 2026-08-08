create database UniversityManagementSystem;

use UniversityManagementSystem;

create table Departments (
	Department_ID varchar(10) primary key,
    Department_Name varchar(50) not null,
    Faculty varchar(30) not null
);

create table Professors (
	Professor_ID varchar(10) primary key,
    Professor_Name varchar(100) not null,
    Email varchar(100) unique,
    Department_ID varchar(10),
    Hire_Year smallint,
    
    constraint chck_hire_year check (hire_year between 1990 and 2026),
    
    foreign key (Department_ID)
		references Departments(Department_ID)
);

CREATE TABLE Courses (
	Course_ID varchar(10) primary key,
    Course_Name varchar(100) not null,
    Credits tinyint not null,
    Department_ID varchar(10),
    Professor_ID varchar(10),
    
    foreign key (Department_ID)
		references Departments(Department_ID),
	foreign key (Professor_ID)
		 references Professors(Professor_ID)
);

CREATE TABLE Semesters (
	Semester_ID varchar(10) primary key,
    Semester_Name varchar(20),
    Year smallint not null,
    Start_Date date not null,
    End_Date date not null,
    
    constraint chck_semester_name check (semester_name in ('Fall', 'Winter', 'Spring', 'Summer')),
    constraint chck_semester_year check (year between 2000 and 2035)
);

create table Students (
	Student_ID varchar(10) primary key,
    Student_Name varchar(100),
    Gender varchar(30),
    Birth_Date date,
    Email varchar(100) unique,
    Enrollment_Year smallint not null,
    
    constraint chck_gender check (gender in ('Male', 'Female', 'Non-Binary', 'Prefer not to say', 'Unknown', 'Unknown / Not Reported')),
    constraint chck_enrollment_year check (enrollment_year between 2000 and 2035)
);

create table Enrollments (
	Enrollment_ID varchar(12) primary key,
    Student_ID varchar(10),
    Course_ID VARCHAR(10),
    Semester_ID VARCHAR(10),
    Grade varchar(2),
    
    constraint chck_grade check (grade in ('A', 'A+', 'A-', 'B', 'B+', 'B-', 'C', 'C+', 'C-', 'D', 'D+', 'D-', 'F')),
    
    foreign key (Student_ID)
		references Students(Student_ID),
    foreign key (Course_ID)
		references Courses(Course_ID),
    foreign key (Semester_ID)
		references Semesters(Semester_ID)
);