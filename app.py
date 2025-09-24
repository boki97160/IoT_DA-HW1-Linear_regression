
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Business Understanding
st.title("Simple Linear Regression App")
st.markdown("""
This application demonstrates a simple linear regression problem following the CRISP-DM methodology.
""")

st.header("1. Business Understanding")
st.markdown("""
**Goal:** To understand the relationship between an independent variable (X) and a dependent variable (y) by fitting a linear model.
This application allows you to generate data based on a linear equation `y = ax + b`, add noise, and then fit a linear regression model to the data.
""")

# 2. Data Understanding
st.header("2. Data Understanding")
st.markdown("""
The data is generated based on the linear equation `y = ax + b` with some random noise.
You can control the parameters for generating the data.
""")

# Sidebar for user inputs
st.sidebar.header("Data Generation Parameters")
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.0, 0.1)
b = st.sidebar.slider("Intercept (b)", -10.0, 10.0, 1.0, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 1.0, 0.1)
num_points = st.sidebar.slider("Number of points", 10, 1000, 100, 10)

# 3. Data Preparation
st.header("3. Data Preparation")
st.markdown(f"""
Generating {num_points} data points with the equation `y = {a}x + {b}` and noise level of {noise}.
""")
X = np.linspace(-10, 10, num_points).reshape(-1, 1)
y = a * X + b + np.random.normal(0, noise, size=(num_points, 1))

# Display the generated data
st.subheader("Generated Data")
fig, ax = plt.subplots()
ax.scatter(X, y, label="Generated Data")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)


# 4. Modeling
st.header("4. Modeling")
st.markdown("""
We will use a simple linear regression model from scikit-learn to fit the generated data.
""")
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

st.subheader("Model Results")
st.write(f"The model found the following equation: `y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}`")


# 5. Evaluation
st.header("5. Evaluation")
st.markdown("""
We can evaluate the model by visualizing the fitted line against the original data.
""")
st.subheader("Fitted Line")
fig, ax = plt.subplots()
ax.scatter(X, y, label="Generated Data")
ax.plot(X, y_pred, color='red', label="Fitted Line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# 6. Deployment
st.header("6. Deployment")
st.markdown("""
This application is deployed as a Streamlit web app. To run it locally, you need to have Python and the required libraries installed.

1. **Install the required libraries:**
```bash
pip install -r requirements.txt
```

2. **Run the Streamlit app:**
```bash
streamlit run app.py
```
""")
