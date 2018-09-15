from django.shortcuts import render
from weight.models import Weight


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # num_weights = Weight.objects.all().count()

    # The 'all()' is implied by default.
    num_weights = Weight.objects.count()

    context = {
        'num_weights': num_weights,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
