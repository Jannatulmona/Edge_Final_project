# Edge_Final_project
# House Price Prediction Django App

This Django web application predicts house prices based on user inputs using a machine learning model trained on sample data.

---

## Features

- Input house details (area, bedrooms, age) via a web form  
- Predict house price using a trained Linear Regression model  
- Simple and user-friendly interface  

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

   
 Step 2:Create and activate a virtual environment:
 
ython -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Step 3:Install dependencies:
pip install -r requirements.txt

Step 4:Apply Django migrations:
python manage.py migrate

5.Run the development server:
python manage.py runserver
6.Open your web browser and visit:

http://127.0.0.1:8000/


Project Structure
core/ — Django project configuration files (settings, URLs)

houseapp/ — Django app with views, templates, ML scripts, and saved model

manage.py — Django project management script

requirements.txt — Python package dependencies
Retraining the Model
To retrain the ML model with updated data:

Modify or add data in houseapp/ml/data.csv

Run:
python houseapp/ml/create_csv.py
python houseapp/ml/train_model.py

This will generate a new model.pkl used for prediction.




