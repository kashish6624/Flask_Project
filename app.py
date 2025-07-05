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

pickle_file_path = '"C:/Users/kashishpreet kaur/OneDrive/Desktop/Documents/Flask_Project/mlclassfier1.pkl"'

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























# from flask import Flask, render_template, request
# import pickle
# import pandas as pd
# import os

# app = Flask(__name__)

# # Mapping prediction output to crop names
# crop_code = {
#     0: 'Rice',
#     1: 'Wheat',
#     2: 'Maize',
#     3: 'Jute'
# }

# # Define the feature columns expected by the model
# columns = ['N', 'P', 'K', 'pH']

# # Use raw string for Windows path or better yet, use os.path.join for portability
# pickle_file_path = r'C:/Users/kashishpreet kaur/OneDrive/Desktop/Documents/DMA LAB/flask/mlclassfier1.pkl'

# # Load the trained model safely
# model = None
# if os.path.exists(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             model = pickle.load(file)
#     except Exception as e:
#         print(f"Error loading model: {e}")
# else:
#     print(f"Pickle file not found at: {pickle_file_path}")

# @app.route('/')
# def index():
#     return render_template('index.html', columns=columns)

# @app.route('/feature')
# def feature():
#     return render_template('feature.html')

# @app.route('/result', methods=['POST'])
# def result():
#     if model is None:
#         return "Model is not loaded. Please check server logs."

#     try:
#         user_input = {}
#         for col in columns:
#             value = request.form.get(col)
#             if value is None or value.strip() == '':
#                 return f"Error: Missing input for {col}"
#             try:
#                 user_input[col] = float(value)
#             except ValueError:
#                 return f"Error: Invalid input for {col}, must be a number"

#         input_df = pd.DataFrame([user_input], columns=columns)
#         prediction = model.predict(input_df)[0]
#         predicted_crop = crop_code.get(int(prediction), "Unknown")

#         return render_template('result.html', prediction=predicted_crop)

#     except Exception as e:
#         return f"An error occurred: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
