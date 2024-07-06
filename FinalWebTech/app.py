from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['firstn']
        last_name = request.form['lastn']
        email = request.form['email']
        job_role = request.form['jobr']
        address = request.form['add']
        city = request.form['city']
        pincode = request.form['pc']
        date = request.form['date']
        plan = request.form['plan']

        # Save data to CSV file
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, email, job_role, address, city, pincode, date, plan])

        return redirect('/index2.html')  # Corrected redirect path

@app.route('/index2.html')
def practice4():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
