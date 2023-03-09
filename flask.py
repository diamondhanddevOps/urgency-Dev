from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        meeting_date = request.form['meeting_date']
        meeting_time = request.form['meeting_time']
        
        # Book the Zoom session
        join_url = book_session(name, email, meeting_date, meeting_time)
        
        # Send the confirmation email
        send_confirmation_email(email, join_url)
        
        # Show a confirmation message or redirect to a confirmation page
        return render_template('confirmation.html')
    else:
        # Show the booking form
        return render_template('booking_form.html')

if __name__ == '__main__':
    app.run(debug=True)
