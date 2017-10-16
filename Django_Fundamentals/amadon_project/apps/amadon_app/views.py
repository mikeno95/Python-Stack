from django.shortcuts import render, redirect, HttpResponse

def index(request):
	if 'total_quantity' not in request.session: 
		request.session['total_quantity'] = 0
	if 'shop_total' not in request.session:
		request.session['shop_total'] = 0
	if 'quantity' not in request.session:
		request.session['quantity'] = 0
	if 'item_total' not in request.session:
		request.session['item_total'] = 0
	return render(request,'amadon_app/index.html')

def process(request):
	if request.POST['product_id'] == str(1):
		request.session['item']='Dojo Tshirt'
		request.session['quantity']=int(request.POST['quantity'])
		request.session['item_total']=request.session['quantity']*19.99
	elif request.POST['product_id'] == str(2):
		request.session['item']='Dojo Sweater'
		request.session['quantity']=int(request.POST['quantity'])
		request.session['item_total']=request.session['quantity']*29.99
	elif request.POST['product_id'] == str(3):
		request.session['item']='Dojo Cup'
		request.session['quantity']=int(request.POST['quantity'])
		request.session['item_total']=request.session['quantity']*4.99
	elif request.POST['product_id'] == str(4):
		request.session['item']='Algorithm Book'
		request.session['quantity']=int(request.POST['quantity'])
		request.session['item_total']=request.session['quantity']*49.99
	# if 'tshirt' in request.POST:
	# 	request.session['item']='Dojo Tshirt'
	# 	quantity=int(request.POST['quantity'])
	# 	request.session['item_total']=quantity*19.99
	# elif 'sweater' in request.POST:
	# 	request.session['item']='Dojo Sweater'
	# 	quantity=int(request.POST['quantity'])
	# 	request.session['item_total']=quantity*29.99
	# elif 'cup' in request.POST:
	# 	request.session['item']='Dojo Cup'
	# 	quantity=int(request.POST['quantity'])
	# 	request.session['item_total']=quantity*4.99
	# elif 'book' in request.POST:
	# 	request.session['item']='Algorithm Book'
	# 	quantity=int(request.POST['quantity'])
	# 	request.session['item_total']=quantity*49.99

	request.session['total_quantity'] += request.session['quantity']
	request.session['shop_total'] += request.session['item_total']

	return redirect('/checkout')

def checkout(request):
	return render(request,'amadon_app/checkout.html')

def reset(request):
	del request.session['item_total']
	return redirect('/')
