from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configure your OpenAI API credentials
openai.api_key = 'opena_api api(cannot be uploaded because it end when uploaded online) '

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get user's answers
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    gender = request.form['gender']
    exer = request.form['exer']
    answer6 = request.form['answer6']
    answer7 = request.form['answer7']

    # Create prompt using user's answers
    prompt = f"My age is {age} years. my weight is {weight} kg my height is {height} cm. calculate my bmi and state whether am i underweight, normal or obese and on the basis of my answers state me how can i improve it"

    # Call the OpenAI API and generate the result
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    generated_result = response.choices[0].text.strip()

    return render_template('result.html', generated_result=generated_result)

if __name__ == '__main__':
    app.run(debug=True)
