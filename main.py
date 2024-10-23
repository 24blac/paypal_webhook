import smtplib
from email.mime.text import MIMEText

def send_email(order_id, payer_email):
    # Email content
    body = f"Guest Checkout Payment Completed\nOrder ID: {order_id}\nPayer Email: {payer_email}"
    msg = MIMEText(body)
    msg['Subject'] = 'New PayPal Payment'
    msg['From'] = 'emkae0001@gmail.com'
    msg['To'] = 'jtsie98@gmail.com'

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'emkae0001@gmail.com'  # Your Gmail address
    smtp_password = 'zero17016175'  # Your Gmail password or app-specific password

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, ['jtsie98@gmail.com'], msg.as_string())
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f"Failed to send email: {e}")

# Call send_email() inside the webhook handler after processing the payment
@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    webhook_event = request.get_json()
    print(f"Received webhook event: {json.dumps(webhook_event, indent=4)}")

    if webhook_event['event_type'] == 'CHECKOUT.ORDER.COMPLETED':
        order_id = webhook_event['resource']['id']
        payer_email = webhook_event['resource']['payer']['email_address']
        print(f"Guest Checkout Payment Completed: Order ID {order_id}, Payer Email {payer_email}")

        # Send email with the order details
        send_email(order_id, payer_email)

    # return jsonify({'status': 'success'}), 200
    return jsonify(webhook_event)
