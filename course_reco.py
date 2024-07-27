from course_recommender import CourseRecommender

# Create an instance of the recommender
recommender = CourseRecommender('students.csv', 'courses.csv', 'ratings.csv')

# Get course categories recommendations for a specific student
student_id = 1
recommendations = recommender.get_recommendations(student_id)
print(recommendations)
