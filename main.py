from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# In-memory storage for received webhook events
webhook_events = []

# Endpoint for PayPal Webhook
@app.route('/webhook', methods=['POST'])
def paypal_webhook():
    # webhook_event = request.get_json()

    if request.headers["Content-Type"] == "application/json":
        return json.dumps(request.json)

    # # Log the received event for debugging
    # print(f"Received webhook event: {json.dumps(webhook_event, indent=4)}")

    # # Store the event in memory (you can save this in a database if needed)
    # webhook_events.append(webhook_event)

    # # Optionally handle specific events like 'CHECKOUT.ORDER.COMPLETED'
    # if webhook_event['event_type'] == 'CHECKOUT.ORDER.COMPLETED':
    #     order_id = webhook_event['resource']['id']
    #     payer_email = webhook_event['resource']['payer']['email_address']
    #     print(f"Order Completed: {order_id}, Payer Email: {payer_email}")

    # return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
