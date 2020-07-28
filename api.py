import numpy as np
import pandas as pd
from flask import  Flask, request, jsonify, render_template, url_for
from sklearn import metrics

app = Flask(__name__)

df_test = pd.read_csv('C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/test2.csv')
df_test = df_test.dropna()
df_pred = pd.read_csv('C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/test2-predictions.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submission():
    '''
    For rendering results on HTML GUI
    '''
    y = np.array(df_test['SeriousDlqin2yrs'])
    pred = np.array(df_pred['Predictions'])
    fpr, tpr, thresholds = metrics.roc_curve(y, pred)
    AUC = metrics.auc(fpr, tpr)

    output = round(AUC, 2)

    return render_template('index.html', submission_text="L'AUC est de {}".format(output))

@app.route('/submit_api', methods=['POST'])
def submission_api():
    '''
    For direct API calls through request
    '''
    y = np.array(df_test['SeriousDlqin2yrs'])
    pred = np.array(df_pred['Predictions'])
    fpr, tpr, thresholds = metrics.roc_curve(y, pred)
    AUC = metrics.auc(fpr, tpr)

    output = round(AUC, 2)

    return jsonify("L'AUC est de {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)