app.config['STRIPE_PUBLIC_KEY'] = 'your-stripe-public-key'
app.config['STRIPE_SECRET_KEY'] = 'your-stripe-secret-key'

from flask_stripe import Stripe
stripe = Stripe()

@app.route('/book_meeting', methods=['POST'])
def book_meeting():
    # get form data
    name = 'request.form'['name']
    email = 'request.form'['email']
    date = 'request.form'['date']
    time = 'request.form'['time']
    additional_info = 'request.form.get'('additional_info')
    # create Stripe charge
    charge = 'stripe.Charge.create'(
        amount=10000,
        currency='usd',
        source='request.form['stripeToken'],
        description='Meeting booking fee'
    )
    # store payment information in database
    payment = 'Payment'(
        amount=100,
        currency='usd',
        stripe_charge_id=charge.id,
        status='paid'
    )
    'db.session.add'(payment)
    'db.session.commit'()
