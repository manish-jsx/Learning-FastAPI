
# FastAPI Stripe Payment Gateway Integration

This project demonstrates the integration of a payment gateway (Stripe) with FastAPI. It includes endpoints for initiating payments, handling callbacks, and checking payment status.

## Prerequisites

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [Stripe Account](https://stripe.com/)
- [Stripe Python Library](https://stripe.com/docs/stripe-cli)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-stripe-payment.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the project root and add the following:

   ```env
   STRIPE_SECRET_KEY=your_stripe_secret_key
   STRIPE_ENDPOINT_SECRET=your_stripe_endpoint_secret
   ```

   Replace `your_stripe_secret_key` and `your_stripe_endpoint_secret` with your actual Stripe secret key and endpoint secret.

## Usage

1. Run the FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI development server.

2. Create a payment:

   Use the `/create-payment` endpoint to initiate a payment. Replace `your_amount` with the desired payment amount:

   ```bash
   curl -X POST "http://localhost:8000/create-payment" -H "Content-Type: application/json" -d '{"amount": your_amount}'
   ```

   The response will include a `client_secret`.

3. Configure Stripe Webhook:

   Set up a webhook endpoint in your [Stripe Dashboard](https://dashboard.stripe.com/webhooks) and obtain the endpoint secret.

4. Update Webhook Endpoint:

   Replace `"your_stripe_endpoint_secret"` in the `main.py` file with your actual Stripe endpoint secret.

5. Test Webhook:

   Simulate a payment success event using the [Stripe Dashboard](https://dashboard.stripe.com/test/payments), and check if the webhook endpoint receives the events.

## Webhook Events

The `/webhook` endpoint in the FastAPI app handles Stripe webhook events. Customize the handling of events based on your application requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
