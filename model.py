import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Read original dataset
df = pd.read_excel("D:/CopperProject/.venv/data/Copper_Set.xlsx", sheet_name=0)

indexAge = df[ (df['status'] != 'Won') & (df['status'] != 'Lost') ].index
df.drop(indexAge , inplace=True)

df.drop(['material_ref','id', 'item_date', 'delivery date'], axis= 1, inplace=True)

#drop the null values
df = df.dropna()

df = df[df['quantity tons'] != 'e']
df['quantity tons'] = df['quantity tons'].astype(float)

objList = df.select_dtypes(include = "object").columns

#Labelencoding 
le = LabelEncoder()

for feat in objList:
    df[feat] = le.fit_transform(df[feat].astype(str))

#Build the model
X = df.drop(['status','selling_price'], axis=1)
y = df['status']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = rf_classifier.predict(X_test)

# Evaluate the accuracy of the model
rf_accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", rf_accuracy)

#save the model to disk
joblib.dump(rf_classifier,"rfclass.sav")
# print(df.head(5))

#Price prediction model
#Build the regression model
X = df.drop(['status','selling_price'], axis=1)
y = df['selling_price']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting Random Forest Regression to the dataset
regressor = RandomForestRegressor(random_state=0, n_estimators=10)

# Fit the regressor with x and y data
regressor.fit(X_train, y_train)

# Making predictions on the same data or new data
predictions = regressor.predict(X_test)

joblib.dump(regressor, "regg_rf_model.sav")

