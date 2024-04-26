from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

class PredictView(APIView):
    def get(self, request):
        return Response({'message': 'All ok'}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get input values from the request data
        Age = request.data.get('age')
        Sex = request.data.get('sex')
        Bmi = request.data.get('bmi')
        Smoker = request.data.get('smoker')

        # Check if any input value is missing
        if Age is None or Sex is None or Bmi is None or Smoker is None:
            return Response({'error': 'One or more input values are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert Age and StressLevel to float
        try:
            Age = float(Age)
            Bmi = float(Bmi)
        except ValueError:
            return Response({'error': 'One or more input values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert Gender to numeric
        Sex_numeric = 0 if Sex.lower() == 'male' else 1
        Smoker_numeric = 0 if Smoker.lower() == 'male' else 1

        # Use LabelEncoder to encode categorical variables
        data = pd.read_csv('./medical_cost.csv')
        le = LabelEncoder()
        data["sex"] = le.fit_transform(data["sex"])
        data["smoker"] = le.fit_transform(data["smoker"])

        # Prepare input features (assuming columns 1, 2, 3, and 7 are relevant)
        x = data.iloc[:, [1, 2, 3, 4]]
        y = data.iloc[:, -1]

        # Train a linear regression model
        rg = LinearRegression()
        rg.fit(x, y)

        # Predict the output based on input values
        out = rg.predict([[Age, Sex_numeric, Bmi, Smoker_numeric]])

        # Process the output
        output = round(float(out[0]), 2)  # Convert to float, round to 2 decimal places
        output_formatted = f'medical charge: {output} '  # Format output as "Quality of Sleep: [value] Hours"

        return Response({'output': output_formatted}, status=status.HTTP_200_OK)