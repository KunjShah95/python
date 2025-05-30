import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier

class StudentData:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def clean_data(self):
        # Convert 'Yes'/'No' to 1/0
        self.df['Extracurricular'] = self.df['Extracurricular'].map({'Yes': 1, 'No': 0})
        print("✅ Data cleaned!")

    def visualize(self):
        sns.pairplot(self.df, hue='Passed')
        plt.show()

    def get_features_and_labels(self):
        X = self.df[['StudyHours', 'Attendance', 'PastScore', 'Extracurricular']]
        y = self.df['Passed']
        return X, y

class StudentPerformanceModel:
    def __init__(self, model_type='logistic'):
        if model_type == 'logistic':
            self.model = LogisticRegression()
        elif model_type == 'tree':
            self.model = DecisionTreeClassifier()
        else:
            raise ValueError("Choose 'logistic' or 'tree'")

    def train(self, X, y):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        print("📈 Model trained.")

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        print("🎯 Accuracy:", accuracy_score(self.y_test, y_pred))
        print("📊 Classification Report:\n", classification_report(self.y_test, y_pred))

    def predict(self, study, attendance, score, extra):
        input_data = [[study, attendance, score, 1 if extra == 'Yes' else 0]]
        prediction = self.model.predict(input_data)
        print("🧠 Prediction:", "Passed ✅" if prediction[0] == 1 else "Failed ❌")


def main():
    data = StudentData('student_data.csv')
    data.clean_data()
    data.visualize()

    X, y = data.get_features_and_labels()

    model = StudentPerformanceModel(model_type='logistic')
    model.train(X, y)
    model.evaluate()

    # Try prediction
    print("\n--- Predict New Student ---")
    model.predict(study=4.5, attendance=80, score=70, extra='Yes')

if __name__ == "__main__":
    main()
