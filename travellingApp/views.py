from .models import Availability, Booking, Ticket
from django.shortcuts import render
from .forms import ContactForm, AvailabilityForm, BookingForm
from .utils import (
    getTicketsArray,
    getPackagesArray,
    getFeaturedTrips,
    getActivities,
    getHotels,
)

# Create your views here.
def home(request):
    contactform = ContactForm()
    availabilityform = AvailabilityForm()
    bookingform = BookingForm()
    return render(
        request,
        "index.html",
        context={
            "activeTickets": getTicketsArray()[0],
            "numTickets": getTicketsArray()[1],
            "tickets": getTicketsArray()[2],
            "packages": getPackagesArray(),
            "activeTrip": getFeaturedTrips()[0],
            "numTrips": getFeaturedTrips()[1],
            "trips": getFeaturedTrips()[2],
            "activeActivity": getActivities()[0],
            "numActivities": getActivities()[1],
            "activities": getActivities()[2],
            "hotels": getHotels(),
            "contactform": contactform,
            "contactresponse": "Get in touch",
            "bookingform": bookingform,
            "bookingresponse": "Book Your Flight",
            "availabilityform": availabilityform,
            "availabilityresponse": "Check Availability",
        },
    )


def contacted(request):
    contactform = ContactForm()
    availabilityform = AvailabilityForm()
    bookingform = BookingForm()
    if request.method == "POST":
        data = ContactForm(request.POST)
        if data.is_valid():
            data.save()
            return render(
                request,
                "index.html",
                context={
                    "activeTickets": getTicketsArray()[0],
                    "numTickets": getTicketsArray()[1],
                    "tickets": getTicketsArray()[2],
                    "packages": getPackagesArray(),
                    "activeTrip": getFeaturedTrips()[0],
                    "numTrips": getFeaturedTrips()[1],
                    "trips": getFeaturedTrips()[2],
                    "activeActivity": getActivities()[0],
                    "numActivities": getActivities()[1],
                    "activities": getActivities()[2],
                    "hotels": getHotels(),
                    "contactresponse": "Your Message Has Been Sent Successfully",
                    "bookingform": bookingform,
                    "bookingresponse": "Book Your Flight",
                    "availabilityform": availabilityform,
                    "availabilityresponse": "Check Availability",
                },
            )
        else:
            return render(
                request,
                "index.html",
                context={
                    "activeTickets": getTicketsArray()[0],
                    "numTickets": getTicketsArray()[1],
                    "tickets": getTicketsArray()[2],
                    "packages": getPackagesArray(),
                    "activeTrip": getFeaturedTrips()[0],
                    "numTrips": getFeaturedTrips()[1],
                    "trips": getFeaturedTrips()[2],
                    "activeActivity": getActivities()[0],
                    "numActivities": getActivities()[1],
                    "activities": getActivities()[2],
                    "hotels": getHotels(),
                    "contactresponse": "Your Message Has not been sent Successfully",
                    "bookingform": bookingform,
                    "bookingresponse": "Book Your Flight",
                    "availabilityform": availabilityform,
                    "availabilityresponse": "Check Availability",
                },
            )

    return render(
        request,
        "index.html",
        context={
            "activeTickets": getTicketsArray()[0],
            "numTickets": getTicketsArray()[1],
            "tickets": getTicketsArray()[2],
            "packages": getPackagesArray(),
            "activeTrip": getFeaturedTrips()[0],
            "numTrips": getFeaturedTrips()[1],
            "trips": getFeaturedTrips()[2],
            "activeActivity": getActivities()[0],
            "numActivities": getActivities()[1],
            "activities": getActivities()[2],
            "hotels": getHotels(),
            "contactform": contactform,
            "contactresponse": "Get in touch",
            "bookingform": bookingform,
            "bookingresponse": "Book Your Flight",
            "availabilityform": availabilityform,
            "availabilityresponse": "Check Availability",
        },
    )


def checked(request):
    contactform = ContactForm()
    availabilityform = AvailabilityForm()
    bookingform = BookingForm()

    if request.method == "POST":
        data = AvailabilityForm(request.POST)
        if data.is_valid():
            check = Ticket.objects.filter(
                date=request.POST.get("date"), country=request.POST.get("country")
            )

            if check.count() > 0:
                availabilityresponse = "Available, Kindly proceed to booking"
            else:
                availabilityresponse = "Not Available, Kindly try some other time"

            return render(
                request,
                "index.html",
                context={
                    "activeTickets": getTicketsArray()[0],
                    "numTickets": getTicketsArray()[1],
                    "tickets": getTicketsArray()[2],
                    "packages": getPackagesArray(),
                    "activeTrip": getFeaturedTrips()[0],
                    "numTrips": getFeaturedTrips()[1],
                    "trips": getFeaturedTrips()[2],
                    "activeActivity": getActivities()[0],
                    "numActivities": getActivities()[1],
                    "activities": getActivities()[2],
                    "hotels": getHotels(),
                    "contactform": contactform,
                    "contactresponse": "Get in touch",
                    "bookingform": bookingform,
                    "bookingresponse": "Book Your Flight",
                    "availabilityresponse": availabilityresponse,
                },
            )
        else:
            return render(
                request,
                "index.html",
                context={
                    "activeTickets": getTicketsArray()[0],
                    "numTickets": getTicketsArray()[1],
                    "tickets": getTicketsArray()[2],
                    "packages": getPackagesArray(),
                    "activeTrip": getFeaturedTrips()[0],
                    "numTrips": getFeaturedTrips()[1],
                    "trips": getFeaturedTrips()[2],
                    "activeActivity": getActivities()[0],
                    "numActivities": getActivities()[1],
                    "activities": getActivities()[2],
                    "hotels": getHotels(),
                    "contactform": contactform,
                    "contactresponse": "Get in touch",
                    "bookingform": bookingform,
                    "bookingresponse": "Book Your Flight",
                    "availabilityform": availabilityform,
                    "availabilityresponse": "Check Availability",
                },
            )

    return render(
        request,
        "index.html",
        context={
            "activeTickets": getTicketsArray()[0],
            "numTickets": getTicketsArray()[1],
            "tickets": getTicketsArray()[2],
            "packages": getPackagesArray(),
            "activeTrip": getFeaturedTrips()[0],
            "numTrips": getFeaturedTrips()[1],
            "trips": getFeaturedTrips()[2],
            "activeActivity": getActivities()[0],
            "numActivities": getActivities()[1],
            "activities": getActivities()[2],
            "hotels": getHotels(),
            "contactform": contactform,
            "contactresponse": "Get in touch",
            "bookingform": bookingform,
            "bookingresponse": "Book Your Flight",
            "availabilityform": availabilityform,
            "availabilityresponse": "Check Availability",
        },
    )


def booked(request):
    contactform = ContactForm()
    availabilityform = AvailabilityForm()
    bookingform = BookingForm()
    if request.method == "POST":
        data = BookingForm(request.POST)
        if data.is_valid():
            data.save()
            return render(
                request,
                "index.html",
                context={
                    "activeTickets": getTicketsArray()[0],
                    "numTickets": getTicketsArray()[1],
                    "tickets": getTicketsArray()[2],
                    "packages": getPackagesArray(),
                    "activeTrip": getFeaturedTrips()[0],
                    "numTrips": getFeaturedTrips()[1],
                    "trips": getFeaturedTrips()[2],
                    "activeActivity": getActivities()[0],
                    "numActivities": getActivities()[1],
                    "activities": getActivities()[2],
                    "hotels": getHotels(),
                    "contactform": contactform,
                    "contactresponse": "Get in touch",
                    "bookingresponse": "Your Flight is booked we would contact you in a bit",
                    "availabilityresponse": "Available, Kindly proceed to booking",
                },
            )
    return render(
        request,
        "index.html",
        context={
            "activeTickets": getTicketsArray()[0],
            "numTickets": getTicketsArray()[1],
            "tickets": getTicketsArray()[2],
            "packages": getPackagesArray(),
            "activeTrip": getFeaturedTrips()[0],
            "numTrips": getFeaturedTrips()[1],
            "trips": getFeaturedTrips()[2],
            "activeActivity": getActivities()[0],
            "numActivities": getActivities()[1],
            "activities": getActivities()[2],
            "hotels": getHotels(),
            "contactform": contactform,
            "contactresponse": "Get in touch",
            "bookingform": bookingform,
            "bookingresponse": "Book Your Flight",
            "availabilityform": availabilityform,
            "availabilityresponse": "Available, Kindly proceed to booking",
        },
    )
