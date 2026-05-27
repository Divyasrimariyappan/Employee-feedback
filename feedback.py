from flask import Flask, request, jsonify, send_from_directory, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_folder='.', static_url_path='')

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'


# FRONT PAGE
@app.route('/')
def portal():
    return send_from_directory(app.static_folder, 'portal.html')


# LOGIN PAGE
@app.route('/loginpage')
def loginpage():
    return send_from_directory(app.static_folder, 'index.html')


# FEEDBACK FORM PAGE
@app.route('/form')
def form():
    return send_from_directory(app.static_folder, 'form.html')


# LOGIN VALIDATION
@app.route('/login', methods=['POST'])
def login():

    data = request.get_json(silent=True) or {}

    username = data.get('username', '')
    password = data.get('password', '')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify(success=True)

    return jsonify(
        success=False,
        message='Invalid username or password'
    ), 401


# FEEDBACK SUBMIT
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():

    employee_name = request.form.get('employee_name')
    employee_email = request.form.get('employee_email')

    subject = 'Employee Feedback'

    body = f"""
Hello {employee_name},

Your feedback submitted successfully.
"""

    sender_email = 'divyasrimariyappan3@gmail.com'

    sender_password = 'nhfa fjvg zium habr'

    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = employee_email

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(
            sender_email,
            employee_email,
            msg.as_string()
        )

        server.quit()

        return send_from_directory(
            app.static_folder,
            'submit1.html'
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)