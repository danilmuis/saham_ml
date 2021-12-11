from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', output1='')

@app.route('/', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    a,b,c,d,e = [x for x in request.form.values()]

    data = [e,d,c,b,a]
    prediction = model.predict([data])
    output1 = round(prediction[0])
    
    data2 = [d,c,b,a,output1]
    prediction = model.predict([data2])
    output2 = round(prediction[0])
    
    
    data3 = [c,b,a,output1,output2]
    prediction = model.predict([data3])
    output3 = round(prediction[0])
    
    return render_template('index.html', output1=output1, output2=output2, output3=output3, e=e, d=d, c=c, b=b, a=a)


if __name__ == '__main__':
    app.run(debug=True)