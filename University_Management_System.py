#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
from pathlib import Path

CSV_DIR = Path(__file__).parent / 'csv'


# In[24]:


# Inspect the structure of each table
def load_data():

    students = pd.read_csv(CSV_DIR / 'Students.csv')
    courses = pd.read_csv(CSV_DIR / 'Courses.csv')
    enrollments = pd.read_csv(CSV_DIR / 'Enrollments.csv')
    professors = pd.read_csv(CSV_DIR / 'Professors.csv')
    semesters = pd.read_csv(CSV_DIR / 'Semesters.csv')
    departments = pd.read_csv(CSV_DIR / 'Departments.csv')
    
    print(students.info())
    print(courses.info())
    print(enrollments.info())
    print(professors.info())
    print(semesters.info())
    print(departments.info())

    return students, courses, enrollments, professors, semesters, departments


# In[17]:


# Check for duplicate primary keys
def duplicate(students, courses, professors, departments, semesters, enrollments):
    print('Student_ID duplicates: ', students['Student_ID'].duplicated().sum())
    print('Course_ID duplicates: ', courses['Course_ID'].duplicated().sum())
    print('Professor_ID duplicates: ', professors['Professor_ID'].duplicated().sum())
    print('Department_ID duplicates: ', departments['Department_ID'].duplicated().sum())
    print('Semester_ID duplicates: ', semesters['Semester_ID'].duplicated().sum())
    print('Enrollment_ID duplicates: ', enrollments['Enrollment_ID'].duplicated().sum())

# Check foreign key integrity
def orphan_count(child_df, child_col, parent_df, parent_col):
    return (~child_df[child_col].isin(parent_df[parent_col])).sum()

def check_foreign_keys(courses, departments, professors, students, semesters, enrollments):
    print('\nCourses -> Department (orphans):', orphan_count(courses, 'Department_ID', departments, 'Department_ID'))
    print('Courses -> Professor (orphans):', orphan_count(courses, 'Professor_ID', professors, 'Professor_ID'))
    print('Professors -> Department (orphans):', orphan_count(professors, 'Department_ID', departments, 'Department_ID'))
    print('Enrollments -> Student (orphans):', orphan_count(enrollments, 'Student_ID', students, 'Student_ID'))
    print('Enrollments -> Course (orphans):', orphan_count(enrollments, 'Course_ID', courses, 'Course_ID'))
    print('Enrollments -> Semester (orphans):', orphan_count(enrollments, 'Semester_ID', semesters, 'Semester_ID'))

# Inspect unique values in categorical columns for inconsistent naming
def unique_value(students, enrollments):
    print('\nGender values:', students['Gender'].unique())
    print('Grade values:', enrollments['Grade'].unique())


# In[18]:


#datetime
def check_date_and_range(students, semesters):
    students['Birth_Date'] = pd.to_datetime(students['Birth_Date'])
    semesters['Start_Date'] = pd.to_datetime(semesters['Start_Date'])
    semesters['End_Date'] = pd.to_datetime(semesters['End_Date'])
    
    # Check that End_Date is always after Start_Date
    bad_semesters = semesters[semesters['End_Date'] <= semesters['Start_Date']]
    print('Terms with invalid dates:', len(bad_semesters))
    
    # Validate student age at enrollment
    students['Age_At_Enrollment'] = students['Enrollment_Year'] - students['Birth_Date'].dt.year
    print(students['Age_At_Enrollment'].describe())
    
    # Check for student ages outside the expected range (15–40)
    wierd_age = students[(students['Age_At_Enrollment'] < 15) | (students['Age_At_Enrollment'] > 40)]
    print('Counts of suspicious ages:', len(wierd_age))


# In[20]:


def main():

    students, courses, enrollments, professors, semesters, departments = load_data()
    duplicate(students, courses, professors, departments, semesters, enrollments)
    check_foreign_keys(courses, departments, professors, students, semesters, enrollments)
    unique_value(students, enrollments)
    check_date_and_range(students, semesters)

if __name__ == '__main__':
    main()

