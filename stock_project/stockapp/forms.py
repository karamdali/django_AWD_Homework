from django import forms

class StockForm(forms.Form):
    ticker_symbol = forms.CharField(label='Stock Ticker Symbol', max_length=10,widget=forms.TextInput(attrs={"id":"ticker","name":"ticker", "placeholder":"Enter stock ticker symbol","value":"AAPL"}))
    start_date = forms.DateField(label='Start Date',widget=forms.TextInput(attrs={"type":"date", "id":"start-date","name":"start-date", "placeholder":"YYYY-MM-DD","value":"2024-02-29"}))
    end_date = forms.DateField(label='End Date',widget=forms.TextInput(attrs={"type":"date","id":"end-date","name":"end-date", "placeholder":"YYYY-MM-DD","value":"2024-03-29"}))