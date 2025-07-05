from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/analysis')
def analysis():
    return render_template('result1.html')

@app.route('/feature')
def feature():
    return render_template('feature1.html')

crop_code  = {

    0: 'rice',
    1: 'wheat',
    2: 'jute',
    3: 'maize'
}

# Define the columns
columns = ['N', 'P', 'K', 'pH']

pickle_file_path = 'mlclassfier1.pkl'

# Open the file in binary read mode and load the data
with open(pickle_file_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        user_input = {}
        for column in columns:
            user_input[column] = float(request.form[column])

        # Create a DataFrame with the user input
        input_data = pd.DataFrame([user_input], columns=columns)

        print(model)


        prediction = model.predict(input_data)[0]
        predicted_crop = crop_code[int(prediction)]
        
        # Display the input data
        return render_template('result1.html', 
                               input_data=input_data.to_html(index=False), prediction=predicted_crop)

    return render_template('index1.html', columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
