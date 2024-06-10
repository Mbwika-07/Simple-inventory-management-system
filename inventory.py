products = {
    "shoes":{
        "price": 1200,
        "quantity": 7
    },
    "tshirts":{
        "price": 500,
        "quantity": 20
    },
    "socks":{
        "price": 100,
        "quantity": 17
    },
    "jackets":{
        "price": 3200,
        "quantity": 4
    },
    "shorts":{
        "price": 200,
        "quantity": 44
    }
}



def view():
    for name, description in products.items():
        print(f"\nProduct: {name.title()}")
        print(f"\tPrice: {description['price']}")
        print(f"\tQuantity: {description['quantity']}")

def update():
    pass

def delete():
    pass


is_running = True
while is_running:
    print("**********************************************************************************************************************************")
    print("Hello please choose one of the choices below to continue with the program.")
    print("\n\t1.View products")
    print("\n\t2.Update products")
    print("\n\t3.Delete products")
    print("\n\t4.Exit program")
    choice = input("\nKindly enter your choice(1-4): ")
    print("**********************************************************************************************************************************")
    
    if choice == "1":
        view()
    elif choice == "2":
        update()
    elif choice == "3":
        delete()
    elif choice == "4":
        is_running = False
    else:
        print("Please enter a valid choice (1-4)")