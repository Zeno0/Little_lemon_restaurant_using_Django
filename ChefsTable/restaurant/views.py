from django.shortcuts import render, redirect
from .models import Menu, Bookings
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', {'menu': main_data})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, 'menu_item.html', {'menu_item': menu_item})


# def book(request):
#     if request.method == 'POST':
#         fname = request.POST.get('Fname')
#         lname = request.POST.get('Lname')
#         phone = request.POST.get('phone')
#         num_people = request.POST.get('numbers')
#         date = request.POST.get('date')
#         comment = request.POST.get('message')  # Optional comment

#         # Save booking to database
#         booking = Bookings(first_name=fname, last_name=lname, phone=phone, guest_num=num_people, date=date, comment=comment)
#         booking.save()

#         return render(request, 'booking_confirmation.html', {'name': fname})  # Render confirmation page
#     return render(request, 'book.html')

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            fname = request.POST.get('first_name')
            date = request.POST.get('date')
            booking.save()
            return render(request, 'booking_confirmation.html', {'name': fname, 'date': date})  # Redirect to the members page after successful submission
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})
