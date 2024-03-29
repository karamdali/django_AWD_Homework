from django.shortcuts import render
from .forms import StockForm
import yfinance as yf
import json
# Create your views here.
def home(request):
    return render(request,"stock_form.html")

def stock_form(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data['ticker_symbol']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
            open_prices = stock_data['Open'].values.tolist()
            close_prices = stock_data['Close'].values.tolist()
            dates = [date.strftime('%Y-%m-%d') for date in stock_data.index]
            data = {
                "open_prices": open_prices,
                "close_prices": close_prices,
                "dates": dates
            }
            json_data = json.dumps(data)
            return render(request, 'stock_form.html', {'form': form,'stock_data': json_data})
        else:
            form = StockForm()
    return render(request, 'stock_form.html', {'form': form})