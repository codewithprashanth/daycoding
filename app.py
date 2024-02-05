from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

members = []

@app.route('/')
def index():
    return render_template('index.html', members=members)

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form.get('name')
    hall_ticket_number = request.form.get('hall_ticket_number')
    dob = request.form.get('dob')
    gender = request.form.get('gender')

    member = {
        'name': name,
        'hall_ticket_number': hall_ticket_number,
        'dob': dob,
        'gender': gender
    }

    members.append(member)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

