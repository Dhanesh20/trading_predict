from flask import Flask, render_template, request
import pandas as pd  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    investment_amount = float(request.form.get('investmentAmount'))
    risk_level = request.form.get('riskLevel')
    selected_indicators = request.form.getlist('indicator')
    ma_period = request.form.get('maPeriod')

    
    recommendations = [
        {'Stock Symbol': 'AAPL', 'Predicted Returns': 0.05},
        {'Stock Symbol': 'GOOGL', 'Predicted Returns': 0.03},
        # Add more recommendations as needed
    ]

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
