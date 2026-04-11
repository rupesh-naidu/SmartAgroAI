import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# Load dataset
df = pd.read_csv("data/processed/crop_clean.csv")


# Features
X = df.drop("label", axis=1)

# Target
y = df["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Define models
models = {

"KNN": KNeighborsClassifier(),

"SVM": SVC(),

"Decision Tree": DecisionTreeClassifier(),

"Random Forest": RandomForestClassifier()

}


print("\nModel Accuracy Comparison\n")


for name, model in models.items():

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    print(name, "Accuracy:", round(accuracy * 100, 2), "%")