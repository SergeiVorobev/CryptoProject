import os

from django.shortcuts import render, redirect
from .forms import StrategyForm
from .models import Strategy
from django.http import HttpResponseRedirect
from binance.client import Client, AsyncClient



# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_strategies(request):
    strategies = Strategy.objects.all().order_by('date_strategy')
    return render(request, 'strategy/strategies.html', {'strategies': strategies})

def create_strategy(request):
    submitted = False

    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add?submitted=True')
    else:
        form = StrategyForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'strategy/add.html', {'form': form, 'submitted': submitted})

def show_strategy(request, strategy_id):
    strategy = Strategy.objects.get(pk=strategy_id)
    return render(request, 'strategy/show_strategy.html', {'strategy': strategy})


def edit_strategy(request, strategy_id):
    strategy = Strategy.objects.get(pk=strategy_id)
    form = StrategyForm(request.POST or None, instance=strategy)
    if form.is_valid():
        form.save()
        return redirect('show-strategy', strategy_id)
    return render(request, 'strategy/edit_strategy.html', {'strategy': strategy, 'form': form})


def del_strategy(request, strategy_id):
    strategy = Strategy.objects.get(pk=strategy_id)
    strategy.delete()
    return redirect('strategies')


def calculate_orders(request, strategy_id):
    strategy = Strategy.objects.get(pk=strategy_id)
    sn = strategy.total_amount_of_coin
    n = strategy.number_of_orders
    order_q = strategy.margin
    start_price = strategy.start_price
    first_marg = strategy.first_margin
    max_q_price = strategy.max_set_margin
    profit = strategy.profit
    long = strategy.long_strategy
    use_bnb = strategy.use_bnb
    my_orders = {}
    profit_order = {}

    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('SECRET_KEY')
    client = Client(api_key, api_secret)
    # fetch 1 minute klines for the last day up until now
    depth = client.get_order_book(symbol='BNBUSDT')
    current_price = round(float(depth['bids'][0][0]), 5)
    if use_bnb:
        commission = sn * 0.075 / 100 + 0.01  # I am adding 0.01$ just in case
    else:
        commission = sn * 0.1 / 100 + 0.01  # I am adding 0.01$ just in case

    if long:
        # Calculate order amounts
        amounts = []
        order_amounts = 0
        for i in range(1, n):
            if i == 1:
                b1 = round(sn * (1 + order_q / 100 - 1) / ((1 + order_q / 100) ** n - 1), 2)
                amounts.append(b1)
                order_amounts += b1
            if i in range(2, n):
                amount = round(b1 * (1 + order_q / 100) ** (i - 1), 2)
                amounts.append(amount)
                order_amounts += amount

        the_last_order = round(sn - commission - order_amounts, 2)
        amounts.append(the_last_order)
        order_amounts += the_last_order

        # Calculate order prices
        o1_temp = start_price * (1 + first_marg / 100)
        bn = start_price + (start_price * max_q_price / 100)
        q_price = (bn / o1_temp) ** (1 / n)
        coins_byied = 0
        amounts_made = 0
        n_made_orders = 0
        average = 0
        print(f'Orders made: ')

        for i in range(1, n + 1):
            if i == 1:
                o = round(2 * start_price - o1_temp, 5)
                my_orders[o] = amounts[i - 1]
            if i in range(2, n + 1):
                o = o1_temp * q_price ** (i - 1)
                o = round(2 * start_price - o, 5)
                my_orders[o] = amounts[i - 1]

            amounts_made += my_orders[o]
            coins_byied += my_orders[o] / o
            n_made_orders += 1
            print(o, ' : ', my_orders[o])

            # if current_price < o:
            #     amounts_made += my_orders[o]
            #     coins_byied += my_orders[o] / o
            #     n_made_orders += 1
            #     print(o, ' : ', my_orders[o])

        average = amounts_made / coins_byied
        fix_price = average * (1 + profit / 100)

        if use_bnb:
            commission = amounts_made * 0.075 / 100 * 2
        else:
            commission = amounts_made * 0.1 / 100 * 2

        fix_price = round(fix_price + commission / coins_byied, 5)
        profit_order[fix_price] = round(coins_byied, 5)
        print(f'Fix price: {fix_price} for {profit_order[fix_price]} coins(with profit {profit} percentage).'
              f'It\'s {round(profit_order[fix_price] * fix_price * profit / 100, 2)}')

    return render(request, 'strategy/calculate_orders.html', {
        'strategy': strategy, 'my_orders': my_orders.items(),
        'profit_order': profit_order.items(), 'current_price': current_price})