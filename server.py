from flask import Flask, render_template,url_for,request
import json
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)

def write_to_file(data):            
            with open('documentation.txt', 'a') as database:
                database.write(f'{data['email']}\n {data['subject']}\n{data['message']}'
               
                 )
def write_to_csv(data):            
            with open('documentation.csv', 'a', newline = '') as database2:
                email = data['email']
                subject = data['subject']
                message = data['message']
                csv_writer = csv.writer(database2, delimiter=',', quotechar='|',  quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([email,subject,message])
               
                 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        
        write_to_csv(data)
        return render_template('success.html')
    else:
        return 'omo we messed up'

