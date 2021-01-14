from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm, StockForm
from .models import Post, Stock
import requests as requests
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import intcomma


# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/node_modules/startbootstrap-full-width-pics/index.html", context={}, status=200)

def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = Postform()
    return render(request, "components/form.html", context={"form": form}, status=200)

def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    posts_list = [{"id": x.id, "content": x.content, "likes": 1, "dislikes": 2} for x in qs]
    data = {
        "isUser": False,
        "response": posts_list
    }
    return JsonResponse(data)

'''
def post_detail_view(request, post_id, *args, **kwargs):
    try:
        obj = Post.objects.get(id=post_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Hello {post_id} - {obj.content}</h1>")

def post_detail_view(request, post_id, *args, **kwargs):
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_3f02ef0a7ed24c6ab94fe22de7fe01cd")

    
    api = json.loads(api_request.content)
    
    return render(request, 'pages/quotes.html', {'api':api})


def quotes_home_view(request, *args, **kwargs):
    import urllib.request
    import json

    #if request.method == 'POST':
    #    ticker = request.POST["ticker"]

    data = {
        "userId": 101,
        "id": 100,
        "title": "This is a POST request",
        "completed": True
    }
    # Dump the todo object as a json string
    data = json.dumps(data)

    req = urllib.request.Request(url = 'https://jsonplaceholder.typicode.com/todos/', data = bytes(data.encode("utf-8")), method = "POST")

    # Add the appropriate header.
    req.add_header("Content-type", "application/json; charset=UTF-8")

    with urllib.request.urlopen(req) as resp:
        api = json.loads(resp.read().decode("utf-8"))
        print(api)
        return render(request, "pages/quotes.html", context={'ticker':'Enter a ticker'}, status=200) 
'''

'''
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
    


    else:
	    return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

'''
'''
working version:
    data = {
        "userId": 101,
        "id": 100,
        "title": "This is a POST request",
        "completed": True
    }

    # Dump the todo object as a json string
    data = json.dumps(data)

    req = urllib.request.Request(url = 'https://jsonplaceholder.typicode.com/todos/', data = bytes(data.encode("utf-8")), method = "POST")

    # Add the appropriate header.
    req.add_header("Content-type", "application/json; charset=UTF-8")

    with urllib.request.urlopen(req) as resp:
        api = json.loads(resp.read().decode("utf-8"))
        print(api)
        return render(request, "pages/quotes.html", context={'api':api}, status=200) 
'''
'''
    #public key from iexcloud.io: pk_3f02]uest = urllib.request.Request("https://iextrading.com/apps/stocks/AAPL/quote?token=pk_3f02ef0a7ed24c6ab94fe22de7fe01cd")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api: "Error"
    return render(request, "pages/quotes.html", context={}, status=200) 
'''

def about_view(request, *args, **kwargs):
    return render(request, "pages/about.html", context={}, status=200)



def quotes_home_view(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3f02ef0a7ed24c6ab94fe22de7fe01cd")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'pages/quotes.html', {'api': api})

    else:
        return render(request, 'pages/quotes.html', {'ticker': "Enter a Ticker Symbol Above^"})



def add_stock_view(request, *args, **kwargs):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Added!"))
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_3f02ef0a7ed24c6ab94fe22de7fe01cd")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request,'pages/add_stock.html', {'ticker':ticker, 'output':output})

    #ticker = Stock.objects.all()
    #return render(request, "pages/add_stock.html", context={'ticker':ticker}, status=200)

def delete_view(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted!"))
	return redirect('add_stock')

def delete_stock_view(request):
	ticker = Stock.objects.all()
	return render(request, 'pages/delete_stock.html', {'ticker': ticker})


def crypto_view(request, *args, **kwargs):
    import requests
    import json
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP,DOT,LTC,ADA,BCH,XLM,LINK&tsyms=USD&api_key={0cea649a1f01fce70095f810a832bbbfb9327072019b898bd73ca71463c4fe67}")
    price = json.loads(price_request.content)
    return render(request, 'pages/crypto_view.html', {'price': price})


