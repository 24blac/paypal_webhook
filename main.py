from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

# Endpoint for PayPal Webhook
@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    webhook_event = request.get_json()

    # Log the received event for debugging
    print(f"Received webhook event: {json.dumps(webhook_event, indent=4)}")

    # Check for payment events (like guest checkout)
    if webhook_event['event_type'] == 'CHECKOUT.ORDER.COMPLETED':
        order_id = webhook_event['resource']['id']
        payer_email = webhook_event['resource']['payer']['email_address']

        # Store this information (e.g., save to the database)
        print(f"Guest Checkout Payment Completed: Order ID {order_id}, Payer Email {payer_email}")

        # Handle post-payment logic here (e.g., mark payment as complete)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
