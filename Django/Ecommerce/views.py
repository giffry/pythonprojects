from Django.Ecommerce.models import product,carts


def authenticate(id,mobile_name):
    user_data1=[user for user in product if user["id"]==id and user["mobile_name"]==mobile_name]
    return user_data1

user=authenticate(1000,"y9i")

if user:
    print("product available")
else:
    print("product out of stock")

