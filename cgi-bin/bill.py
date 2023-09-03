#!/usr/bin/python3
print("Content-type:text/html")
print()
import cgi
from sklearn.linear_model import LinearRegression
import pandas as pd

data=cgi.FieldStorage()
achrs=data.getvalue("achrs")
tvhrs=data.getvalue("tvhrs")
fridgehrs=data.getvalue("fridgehrs")

# Step 1: Read the CSV file
dataset = pd.read_csv("form.csv")
# Step 2: Extract features (x) and target (y)
y = dataset["electricity bill"]
x = dataset[["AC", "TV", "fridge"]]

# Step 3: Create and train the linear regression model
model = LinearRegression()
model.fit(x, y)

# Step 4: Create a function to take user input and predict the output
def predict_profit():

    rd_spend = achrs
    administration = tvhrs
    marketing_spend = fridgehrs

    # Create a dataframe with the input values
    input_data = pd.DataFrame({
        'AC': [rd_spend],
        'TV': [administration],
        'fridge': [marketing_spend]
    })

    # Use the model to predict the output
    predicted_profit = model.predict(input_data)

    print(f"<h2>Predicted bill: {predicted_profit[0]:.2f}</h2>")

# Step 5: Call the function to get predictions from user input
predict_profit()
