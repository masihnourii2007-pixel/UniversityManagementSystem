# University Management System

A relational dataset and Power BI dashboard modeling a university's academic operations departments, professors, courses, students, and enrollments.

## Data Model

The dataset (`University_Management_System.xlsx`) is structured as a relational schema across six tables, suitable for loading into a SQL database:

| Table           | Rows   | Key Columns                                                                            |
| --------------- | ------ | -------------------------------------------------------------------------------------- |
| **Departments** | 15     | `Department_ID` (PK), `Department_Name`, `Faculty`                                     |
| **Professors**  | 80     | `Professor_ID` (PK), `Professor_Name`, `Email`, `Department_ID` (FK), `Hire_Year`      |
| **Courses**     | 150    | `Course_ID` (PK), `Course_Name`, `Credits`, `Department_ID` (FK), `Professor_ID` (FK)  |
| **Semesters**   | 8      | `Semester_ID` (PK), `Semester_Name`, `Year`, `Start_Date`, `End_Date`                  |
| **Students**    | 1,000  | `Student_ID` (PK), `Student_Name`, `Gender`, `Birth_Date`, `Email`, `Enrollment_Year`  |
| **Enrollments** | 24,000 | `Enrollment_ID` (PK), `Student_ID` (FK), `Course_ID` (FK), `Semester_ID` (FK), `Grade` |

**Relationships:** each Professor and Course belongs to a Department; each Course is taught by a Professor; each Enrollment links a Student to a Course within a Semester. `Enrollments` is the fact table connecting all other dimensions.

## Power BI Dashboard

`UniversityManagementSystem.pbix` visualizes this data model across 5 report pages:

* **University Overview**  KPI cards (total students, professors, courses, enrollments), student trend over time, gender distribution
* **Academic Performance**  average grade, grade distribution, top 10 courses by enrollment
* **Student Analytics**  age distribution, gender vs. enrollment, student activity (scatter)
* **Department Analysis**  number of courses per department, faculty workload (treemap)
* **Semester Analysis**  enrollment trend, most popular semesters, top 10 popular courses

## Python Data Validation

`University_Management_System.py` provides data loading and quality checks for the CSV datasets. The script:

* Loads the six CSV tables using **Pandas**.
* Inspects the structure and data types of each table.
* Checks for duplicate primary keys across all six tables.
* Validates foreign key integrity and identifies orphan records.
* Checks unique values in categorical columns such as `Gender` and `Grade`.
* Converts date columns to datetime format.
* Validates semester date ranges by checking that `End_Date` occurs after `Start_Date`.
* Calculates student age at enrollment and identifies suspicious ages outside the expected range of 15–40.
* Runs all validation steps through a `main()` function.

## Files

* `University_Management_System.xlsx`  source data (6 tables)
* `UniversityManagementSystem.pbix`  Power BI report
* `UniversityManagementSystem.sql` SQL Database
* `University_Management_System.py`  Python data loading and validation script
* `csv/`  CSV datasets
