# payments/views.py
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import uuid 

# === Initiate Payment View ===
def initiate_payment(request):
    if request.method == 'POST':
        # Payment Data to Send to aamarPay
        payload = {
            'store_id': settings.AAMARPAY_STORE_ID,
            'signature_key': settings.AAMARPAY_SIGNATURE_KEY,
            'cus_name': 'Customer Name',
            'cus_email': 'example@gmail.com',
            'cus_phone': '01870123456',  # Use real customer phone
            'amount': '100',              # BDT
            'currency': 'BDT',
            'tran_id': str(uuid.uuid4()),  # Must be unique every time!
            'desc': 'Test Transaction via aamarPay (Django)',
            'success_url': settings.AAMARPAY_SUCCESS_URL,
            'fail_url': settings.AAMARPAY_FAIL_URL,
            'cancel_url': settings.AAMARPAY_CANCEL_URL,
            'type': 'json'
        }

        try:
            # Send POST request to aamarPay API
            response = requests.post(settings.AAMARPAY_API_URL, data=payload)
            data = response.json()

            if data.get('result') == 'true':
                payment_url = data.get('payment_url')
                return redirect(payment_url)  # Redirect user to aamarPay
            else:
                error_message = data.get('message', 'Unknown error from aamarPay.')
                return render(request, 'payments/initiate_payment.html', {'error': error_message})

        except Exception as e:
            return render(request, 'payments/initiate_payment.html', {'error': f'Error: {str(e)}'})

    return render(request, 'payments/initiate_payment.html')

# === Callback Views (Basic Examples) ===

@csrf_exempt
def success(request):
    # TODO: Verify transaction details sent by aamarPay (via POST)
    return render(request, 'payments/result.html', {'status': 'success', 'message': 'Payment Successful!'})

@csrf_exempt
def fail(request):
    return render(request, 'payments/result.html', {'status': 'fail', 'message': 'Payment Failed.'})

@csrf_exempt
def cancel(request):
    return render(request, 'payments/result.html', {'status': 'cancel', 'message': 'Payment Cancelled.'})