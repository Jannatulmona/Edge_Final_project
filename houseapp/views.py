from django.shortcuts import render
import os
import pickle

# Load the trained ML model once when the server starts
model_path = os.path.join(os.path.dirname(__file__), 'ml', 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        try:
            area = float(request.POST.get('area'))
            bedrooms = int(request.POST.get('bedrooms'))
            age = int(request.POST.get('age'))

            input_data = [[area, bedrooms, age]]
            prediction = model.predict(input_data)[0]
        except Exception as e:
            prediction = f"Error: {e}"

    return render(request, 'predict.html', {'prediction': prediction})
