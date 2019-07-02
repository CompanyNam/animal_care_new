from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standart.forms import PayPalPaymentsForm
from home.models import Animal_need_help
from django.view.decorators.csrf import csrf_exempt




# Create your views here.
@csrf_exempt
def payment_done(request):
    return render(request,done.html)

@csrf_exempt
def payment_canceled(request):
    return render(request,canceled.html)







def payment_process(request):
    animal_id=request.session.get('animal_id')
    animal=get_object_or_404(Animal_need_help, id=animal_id)

    host=request.get_host()
    donation_amount=request.get('donation_amount')
    paypal_dict={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': donation_amount,
        'item_name': animal_id,
        'invoice': str(order),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal_ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.form(host, reverse('payment:canceled')),


    }
    form=PayPalPaymentsForm(initial=paypal_dict)

    return render(request, "process.html" , {"animal":animal,"form":form})




