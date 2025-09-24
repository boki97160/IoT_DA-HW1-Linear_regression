# Simple Linear Regression Web App

This is a simple web application that demonstrates a linear regression problem. The application is built using Python and the Streamlit framework, and it follows the CRISP-DM methodology.

## Features

*   **Interactive Data Generation:** Users can generate their own data by specifying the slope (a), intercept (b), noise level, and the number of data points for a linear equation `y = ax + b`.
*   **Linear Regression Modeling:** The application fits a simple linear regression model to the generated data using the scikit-learn library.
*   **Model Evaluation:** The results of the model, including the calculated slope and intercept, are displayed. The fitted regression line is plotted against the original data for visual evaluation.
*   **CRISP-DM Framework:** The application is structured to follow the Cross-Industry Standard Process for Data Mining (CRISP-DM), with sections for Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.

## Technologies Used

*   Python
*   Streamlit
*   scikit-learn
*   NumPy
*   Matplotlib

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/boki97160/IoT_DA-HW1-Linear_regression.git
    cd IoT_DA-HW1-Linear_regression
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

    The application will be accessible at `http://localhost:8501` in your web browser.

## CRISP-DM Methodology

This project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology to structure the data mining process. The steps are outlined in the application itself:

1.  **Business Understanding:** Defining the project objectives and requirements.
2.  **Data Understanding:** Familiarizing with the data.
3.  **Data Preparation:** Covering all activities to construct the final dataset.
4.  **Modeling:** Selecting and applying various modeling techniques.
5.  **Evaluation:** Evaluating the model.
6.  **Deployment:** Deploying the model.
