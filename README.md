# aamarpay Payment Integration in Django

A Django project demonstrating seamless integration with aamarpay, a popular payment gateway in Bangladesh. This implementation provides a complete flow for initiating payments, handling callbacks, and displaying transaction results.

## Features

- Secure payment initiation using aamarpay API
- Responsive payment interface with Tailwind CSS
- Success/failure/cancellation handling
- Transaction status display
- Sandbox environment configuration

## Prerequisites

- Python 3.8+
- Django 5.2+
- aamarpay account (for store ID and signature key)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tanvir-yzu/aamarpay-payment-services-in-Django.git
   cd aamarpay
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure aamarpay credentials in `aamarpay/settings.py`:
   ```python
   AAMARPAY_STORE_ID = 'your_store_id'
   AAMARPAY_SIGNATURE_KEY = 'your_signature_key'
   AAMARPAY_API_URL = 'https://sandbox.aamarpay.com'  # Use production URL for live environment
   ```

5. Run migrations (if needed for future extensions):
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000/payments/`

## Project Structure

```
aamarpay-payment-services-in-Django/
├── aamarpay/                 # Main project folder
│   ├── settings.py           # Project settings including aamarpay config
│   ├── urls.py               # Main URL routing
│   └── ...
├── payments/                 # Payment app
│   ├── templates/payments/   # HTML templates
│   │   ├── initiate_payment.html  # Payment initiation form
│   │   └── result.html            # Payment status display
│   ├── views.py              # Payment logic and callback handlers
│   ├── urls.py               # Payment-related URL routing
│   └── ...
├── manage.py                 # Django management script
└── requirements.txt          # Project dependencies
```

## Payment Flow

1. User is directed to the payment initiation page
2. On clicking "Pay Now", a request is sent to aamarpay API
3. User is redirected to aamarpay's secure payment page
4. After completing/canceling the payment, user is redirected back to:
   - `success/` for successful payments
   - `fail/` for failed payments
   - `cancel/` if user cancels the payment

## Configuration

Key settings in `aamarpay/settings.py`:

- `AAMARPAY_STORE_ID`: Your aamarpay store ID
- `AAMARPAY_SIGNATURE_KEY`: Your aamarpay signature key
- `AAMARPAY_SUCCESS_URL`: URL for successful payments
- `AAMARPAY_FAIL_URL`: URL for failed payments
- `AAMARPAY_CANCEL_URL`: URL for canceled payments
- `AAMARPAY_API_URL`: aamarpay API endpoint (sandbox or production)

## Deployment Notes

- For production, set `DEBUG = False` in settings
- Update `ALLOWED_HOSTS` with your domain name
- Use the production aamarpay API URL
- Set up proper SSL/TLS (HTTPS)
- Consider using environment variables for sensitive information (store ID, signature key)
- In production, you may need to use a service like ngrok for local testing of webhooks

## Security Considerations

- Always verify transaction details in callback handlers
- Use HTTPS in production
- Keep your signature key secure and never expose it in client-side code
- Validate all input data before processing payments
- Implement proper error handling and logging

## Future Enhancements

- Add transaction record keeping in the database
- Implement proper transaction verification in callbacks
- Add user authentication
- Support for multiple payment amounts
- Email notifications for payment status
- Admin interface for transaction management

## Troubleshooting

- If payments aren't processing, check your aamarpay credentials
- Ensure your callback URLs are accessible from the internet (use ngrok for local testing)
- Check the aamarpay API documentation for error codes and troubleshooting

## Resources

- [aamarpay Documentation](https://aamarpay.com/docs)
- [Django Documentation](https://docs.djangoproject.com/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.