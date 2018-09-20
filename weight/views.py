from django.shortcuts import render
from django.http import JsonResponse
from weight.models import Weight
from django.contrib.auth.models import User

from datetime import datetime


def timestamp(date):
    return int(datetime.combine(date, datetime.min.time()).timestamp()) * 1000


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


def weights(request):
    user = User.objects.get(username='Tom')
    dataset = Weight.objects\
        .values('date', 'weight')\
        .filter(user_id=user.id)\
        .order_by('date')
    print(dataset)
    context = {
        'dataset': dataset,
    }
    return render(request, 'weights.html', context=context)


def json_example(request):
    return render(request, 'json_example.html')


def chart_data(request):
    user = User.objects.get(username='Tom')
    dataset = Weight.objects\
        .values('date', 'weight')\
        .filter(user_id=user.id)\
        .order_by('date')
    print(dataset)
    for row in dataset:
        print(timestamp(row['date']), row['weight'])

    chart = {
        'rangeSelector': {
            'selected': 1
        },
        'title': {
            'text': 'Weight Chart'
        },
        'series': [{
            'name': 'Weight',
            'tooltip': {
                'valueDecimals': 2
            },
            'data': list(map(lambda row: [timestamp(row['date']), row['weight']], dataset))
        }]
    }
    print(chart)

    return JsonResponse(chart)
