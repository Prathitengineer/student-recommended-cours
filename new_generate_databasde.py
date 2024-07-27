import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for synthetic data
num_students = 300
num_courses = 200

# Generate student data
students = pd.DataFrame({
    'Student_ID': np.arange(1, num_students + 1),
    'Name': [f'Student_{i}' for i in range(1, num_students + 1)],
    'Age': np.random.randint(18, 30, size=num_students),
    'Gender': np.random.choice(['Male', 'Female'], size=num_students),
    'Major': np.random.choice(['Web Devlopment','Data Science','Mobile Development', 'Game Devlopment','DevOps'], size=num_students)
})
students.to_csv("Student.csv")
# Generate course data
courses = pd.DataFrame({
    'Course_ID': np.arange(1, num_courses + 1),
    'Course_Name': [f'Course_{i}' for i in range(1, num_courses + 1)],
    'Category': np.random.choice(['Js','html','css','python',"r",'sql','kotlin', 'swift','java','cpp''csharp','unity','go' ,'ruby'], size=num_courses),
    'Level': np.random.choice(['Beginner', 'Intermediate', 'Advanced'], size=num_courses),
    'Duration': np.random.randint(5, 25, size=num_courses),
    'Rating': np.round(np.random.uniform(3, 5, size=num_courses), 1),
    'Instructor': [f'Instructor_{i}' for i in range(1, num_courses + 1)],
    'Keywords': [f'Keyword_{i}' for i in range(1, num_courses + 1)]
})
courses.to_csv("courses.csv")
# Generate ratings with some randomness
ratings = pd.DataFrame({
    'Student_ID': np.random.choice(students['Student_ID'], size=num_students * 20, replace=True),
    'Course_ID': np.random.choice(courses['Course_ID'], size=num_students * 20, replace=True),
    'Rating': np.random.randint(1, 6, size=num_students * 20)
})

# Remove duplicate ratings
ratings = ratings.drop_duplicates(subset=['Student_ID', 'Course_ID'])

# Ensure all courses and students are represented
additional_ratings = pd.DataFrame({
    'Student_ID': np.random.choice(students['Student_ID'], size=num_courses),
    'Course_ID': courses['Course_ID'],
    'Rating': np.random.randint(1, 6, size=num_courses)
})
ratings = pd.concat([ratings, additional_ratings]).drop_duplicates(subset=['Student_ID', 'Course_ID'])
ratings.to_csv("ratings.csv")
# Print samples of the datasets
print("Students Data Sample:")
print(students.head())
print("\nCourses Data Sample:")
print(courses.head())
print("\nRatings Data Sample:")
print(ratings.head())
del students
del courses
del ratings
