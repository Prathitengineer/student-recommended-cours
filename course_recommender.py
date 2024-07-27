import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

class CourseRecommender:
    def __init__(self, students_file, courses_file, ratings_file):
        self.students_file = students_file
        self.courses_file = courses_file
        self.ratings_file = ratings_file
        self.students = None
        self.courses = None
        self.ratings = None
        self.similarity_df = None
        
        self.load_data()
        self.prepare_data()
        
    def load_data(self):
        self.students = pd.read_csv(self.students_file)
        self.courses = pd.read_csv(self.courses_file)
        self.ratings = pd.read_csv(self.ratings_file)
        
    def prepare_data(self):
        # Create a pivot table with student IDs as rows and course IDs as columns
        rating_matrix = self.ratings.pivot(index='Student_ID', columns='Course_ID', values='Rating').fillna(0)
        
        # Convert the pivot table to a sparse matrix format
        sparse_matrix = csr_matrix(rating_matrix.values)
        
        # Apply SVD
        svd = TruncatedSVD(n_components=20)
        matrix_svd = svd.fit_transform(sparse_matrix)
        
        # Compute the cosine similarity matrix
        similarity_matrix = cosine_similarity(matrix_svd)
        
        # Create a DataFrame for the similarity matrix
        self.similarity_df = pd.DataFrame(similarity_matrix, index=rating_matrix.index, columns=rating_matrix.index)
        
    def get_recommendations(self, student_id, num_recommendations=20):
        # Get the similarity scores for the student
        similarity_scores = self.similarity_df[student_id]
        
        # Find the most similar students
        similar_students = similarity_scores.sort_values(ascending=False).index[1:num_recommendations + 1]
        
        # Get the courses rated by these similar students
        similar_students_ratings = self.ratings[self.ratings['Student_ID'].isin(similar_students)]
        
        # Calculate the average rating for each course
        course_recommendations = similar_students_ratings.groupby('Course_ID')['Rating'].mean().sort_values(ascending=False).head(num_recommendations)
        
        # Merge with course details
        recommended_courses = pd.merge(course_recommendations.reset_index(), self.courses, on='Course_ID')

        # Extract unique course categories
        recommended_categories = recommended_courses['Category'].unique()

        return recommended_categories

# Example usage: Get recommendations for student with ID 1
if __name__ == "__main__":
    recommender = CourseRecommender('students.csv', 'courses.csv', 'ratings.csv')
    student_id = 1
    recommendations = recommender.get_recommendations(student_id)
    print(recommendations) 