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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_weights': num_weights,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def weights(request):
    return render(request, 'weights.html')


def weights_data(request):
    user = User.objects.get(username='Tom')
    dataset = Weight.objects\
        .values('date', 'weight')\
        .filter(user_id=user.id)\
        .order_by('date')
    data = list(
        map(
            lambda row: [timestamp(row['date']), row['weight']],
            dataset
        )
    )

    chart = {
        'rangeSelector': {
            'selected': 1
        },

        'title': {
            'text': 'Weight Chart'
        },

        'legend': {
            'enabled': True
        },

        'plotOptions': {
            'series': {
                'showInLegend': True
            }
        },

        'series': [{
            'id': 'weight',
            'name': 'Weight',
            'tooltip': {
                'valueDecimals': 2
            },
            'data': data
        }, {
            'type': 'ema',
            'linkedTo': 'weight',
            'params': {
                'period': 10
            }
        }]
    }

    return JsonResponse(chart)
