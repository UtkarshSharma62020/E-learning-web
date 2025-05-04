import json
import stripe # type: ignore
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Contact.models import Instructor_Contact, User_Contact, Payment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
@login_required
def create_checkout_session(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    course_name = request.POST.get('course_name', 'Course Enrollment')
    amount_cents = int(request.POST.get('amount', 0))

    try:
        # 1) create the Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': course_name},
                    'unit_amount': amount_cents,
                },
                'quantity': 1,
            }],
            mode='payment',
            customer_email=request.user.email,
            success_url=request.build_absolute_uri(
                f"/payment-success/?session_id={{CHECKOUT_SESSION_ID}}"
            ),
            cancel_url=request.build_absolute_uri("/payment-cancelled/"),
        )

        # 2) record the session.id (or .payment_intent) immediately
        Payment.objects.create(
            user=request.user,
            course_name=course_name,
            amount=amount_cents/100,  # convert to dollars
            payment_intent_id=session.id,  # save Checkout Session ID
            status='Pending',
        )

        return JsonResponse({'id': session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# views.py (continued)

def payment_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return render(request, 'payment_success.html', {'error': 'No session ID.'})

    # retrieve the checkout session
    session = stripe.checkout.Session.retrieve(session_id)
    intent_id = session.payment_intent  # this is the actual PaymentIntent ID

    # update our DB record
    try:
        payment = Payment.objects.get(payment_intent_id=session_id)
        payment.payment_intent_id = intent_id  # replace cs_… with pi_…
        payment.status = 'Succeeded'
        payment.save()
    except Payment.DoesNotExist:
        # (optional) handle missing record
        pass

    return render(request, 'payment_success.html')


def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')


@csrf_exempt
@login_required
def enroll_free_course(request):
    if request.method == "POST":
        data = json.loads(request.body)
        course_id = data.get('course_id')
        course_name = data.get('course_name')

        # Save enrollment in your model (optional)
        # UserCourse.objects.get_or_create(user=request.user, course_id=course_id)

        return JsonResponse({'status': 'enrolled'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def home(request):
    return render(request, 'index.html')    # You can access request.user in the template

def about(request):
    return render(request,'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            User_Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True

    return render(request, 'contact.html', {'success': success})


def courses(request):
    return render(request,'courses.html')

def instructor(request):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        subject = request.POST.get('subject')
        address = request.POST.get('address')
        terms_accepted = request.POST.get('terms_accepted') == 'on'  # Checkbox returns 'on' if checked

        if not terms_accepted:
            messages.error(request, "You must accept the terms and conditions.")
            return redirect('instructor')

        Instructor_Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            degree=degree,
            subject=subject,
            address=address,
            terms_accepted=terms_accepted
        )
        messages.success(request, "Your application has been submitted successfully, We will reach out soon!")
        return redirect('instructor')  # Redirect to the same page or thank you page

    return render(request, 'instructor.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('home')  # change 'home' to your dashboard or landing page
            else:
                messages.error(request, 'Invalid credentials.')

        except User.DoesNotExist:
            messages.error(request, 'No account found with this email.')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
            
    return render(request, 'signup.html')

def single(request):
    return render(request,'single.html')

def single2(request):
    return render(request,'single2.html')

def single3(request):
    return render(request,'single3.html')

def single4(request):
    return render(request,'single4.html')

def single5(request):
    return render(request,'single5.html')

def single6(request):
    return render(request,'single6.html')

def single7(request):
    return render(request,'single7.html')

def single8(request):
    return render(request,'single8.html')

def single9(request):
    return render(request,'single9.html')

def single10(request):
    return render(request,'single10.html')

def single11(request):
    return render(request,'single11.html')

def single12(request):
    return render(request,'single12.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # or redirect('home') if you prefer