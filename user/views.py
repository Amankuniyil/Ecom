from django.shortcuts import render

from django.contrib.auth import authenticate,login
# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm,LoginForm,Productform,CatForm
from .models import Account,Product,CartItem,Cart

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Extract validated data from form
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            age = form.cleaned_data.get('age')
            password = form.cleaned_data.get('password')
            
            # Create a new user
            user = Account.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                age=age,
                password=password
            )

            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                
                login(request,user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('home') 
            else:
                messages.error(request, 'Invalid email or password.')
            
    else:
        form=LoginForm(request.POST)
    form=LoginForm(request.POST)
    return render(request,'login.html',{'form':form})



def NewProduct(request):
    if request.method=='POST':
        form=Productform(request.POST)
        if form.is_valid():

            form.save()




    else:
        form=Productform(request.POST)
        p=Product.objects.all()
        return render(request,'product.html',{'form':form,'p':p})
    
    form=Productform(request.POST)
    p=Product.objects.all()
    return render(request,'product.html',{'form':form,'p':p})



def addproduct(request,product_id):
    if request.method=='POST':
        user=request.user
        product=Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
      
        
        if not created:
            # Update quantity if the item already exists in the cart
            cart_item.quantity += 1
            cart_item.save()
        else:
            # Initialize quantity if the item was just created
            cart_item.quantity = 1
            cart_item.save()

        return redirect('cart') 

        

    # Return a 404 response if product is not found or another appropriate response
    return HttpResponse("Product not found")
    
def Carts(request):
    user=request.user
    cart=Cart.objects.get(user=user)
    cartitems=CartItem.objects.filter(cart=cart)

    # total=cartitems.quantity*(cartitems.product.p_price)
    # print(total)
    
    
    
   

 
    return render(request,'cart.html',{'cartitems':cartitems})


    

def home(request):
    print(request.user)

    return render(request,'home.html')