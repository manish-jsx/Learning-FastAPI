from fastapi import FastAPI, HTTPException
import stripe

app = FastAPI()

# Configure Stripe
stripe.api_key = "your_stripe_secret_key"

@app.post("/create-payment")
async def create_payment(amount: int):
    try:
        # Create a PaymentIntent on Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
        )
        return {"client_secret": payment_intent.client_secret}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook")
async def stripe_webhook(payload: dict):
    # Handle Stripe webhook events here
    try:
        event = stripe.Webhook.construct_event(
            payload, stripe.api_key, "your_stripe_endpoint_secret"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Handle different webhook events as needed
    if event["type"] == "payment_intent.succeeded":
        # Payment succeeded, update your database or perform other actions
        pass

    return {"status": "success"}
