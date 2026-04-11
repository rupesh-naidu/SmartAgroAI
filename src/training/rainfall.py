import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


df = pd.read_csv("data/processed/rainfall_clean.csv")

X = df[['JUN','JUL','AUG','SEP']]
y = df['ANNUAL']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {

"Linear Regression": LinearRegression(),

"Decision Tree": DecisionTreeRegressor(),

"Random Forest": RandomForestRegressor(n_estimators=200),

"Gradient Boosting": GradientBoostingRegressor()

}

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = r2_score(y_test, predictions)

    print(name, "R2 Score:", accuracy)