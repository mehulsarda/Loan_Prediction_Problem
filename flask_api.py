from flask import Flask, request
import pandas as pd
import numpy as np
import joblib
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

model = joblib.load(open("rfc", 'rb'))


@app.route("/")
def welcome():
    return "Welcome All!"


@app.route("/predict")
def predict_loan_approval():
    """Let's Check the Bank note approval
    This is using docstring for specifications.
    ---
    parameters:
        - name: gender
          in: query
          type: number
          required: true
        - name: married
          in: query
          type: number
          required: true
        - name: dependents
          in: query
          type: number
          required: true
        - name: education
          in: query
          type: number
          required: true
        - name: self_employed
          in: query
          type: number
          required: true
        - name: applicant_income
          in: query
          type: number
          required: true
        - name: coapplicant_income
          in: query
          type: number
          required: true
        - name: loan_amount
          in: query
          type: number
          required: true
        - name: loan_amount_term
          in: query
          type: number
          required: true
        - name: credit_history
          in: query
          type: number
          required: true
        - name: property_area
          in: query
          type: number
          required: true

    responses:
          200:
              description: The output values

    """

    gender = request.args.get('gender')
    married = request.args.get('married')
    dependents = request.args.get('dependents')
    education = request.args.get('education')
    self_employed = request.args.get('self_employed')
    applicant_income = request.args.get('applicant_income')
    coapplicant_income = request.args.get('coapplicant_income')
    loan_amount = request.args.get('loan_amount')
    loan_amount_term = request.args.get('loan_amount_term')
    credit_history = request.args.get('credit_history')
    property_area = request.args.get('property_area')

    array = [gender, married, dependents, education, self_employed, applicant_income,
             coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]

    prediction = model.predict([array])

    if prediction == 1:
        return "Loan is granted"
    if prediction == 0:
        return "Loan is not granted"

    return "The predicted value is " + str(prediction)


if __name__ == "__main__":
    app.run()
