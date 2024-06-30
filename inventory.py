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
#    product = input("Kindly enter the name of the product you would like to update: ").lower()
    
#    for name, description in products.items():
#        if name == product:
#            print(f"The product {name.title()} is available with {description['quantity']} pieces available.")
#            choice_one = input("Would you like to \n\t1.Add new products or \n\t2. Remove available products from current inventory\nPick a choice(1-2): ")
#            if choice_one == "1":
#                amount = input(f"Enter the amount you would like to add: ")
#                new_quantity = {description["quantity"]} + amount
#            elif choice_one == "2":
#                amount = input(f"Enter the amount you would like to remove from the available inventory: ")
#                if amount < {description["quantity"]}:
#                    new_quantity = {description["quantity"]} - amount
#                else:
#                    print(f"The amount you input {amount} is higher than the amount ({description['quantity']})available.")
#            else:
#                print("Invalid choice")
#        else:
#            print(f"The item {product} is not available in the current inventory.")
    product = input("\nKindly enter the name of the product you would like to update: ").lower()
    
    
    if product in products:
        description = products[product]
        print(f"\nThe product {product.title()} is available with {description['quantity']} pieces available.")
        choice_one = input("Would you like to \n\t1. Add new products or \n\t2. Remove available products from current inventory\nPick a choice (1-2): ")
        
        if choice_one == "1":
            amount = int(input("\nEnter the amount you would like to add: "))
            products[product]['quantity'] += amount
            print(f"\n{amount} items have been added to {product}. New quantity is {products[product]['quantity']}.")
            
        elif choice_one == "2":
            amount = int(input("\nEnter the amount you would like to remove from the available inventory: "))
            if amount <= products[product]['quantity']:
                products[product]['quantity'] -= amount
                print(f"\n{amount} items have been removed from {product}. New quantity is {products[product]['quantity']}.")
            else:
                print(f"\nThe amount you input ({amount}) is higher than the available amount ({description['quantity']}).")
        else:
            print("\nInvalid choice")
    else:
        print(f"\nThe item {product} is not available in the current inventory.")



def add():
    new_name = input("Enter new product name: ")
    new_quantity = int(input("Enter the quantity you wish to add: "))
    new_price = int(input("Enter price for the new product: "))

    new_product = {
        "price": new_price,
        "quantity": new_quantity
    }

    products[new_name] = new_product
    print(f"\nYou have successfully added the product {new_name} with the quantity {new_quantity} and price {new_price} to our inventory.")
    print("\nHere is the updated product list with the new product: ")
    
    view()

def delete():
    delete_product = input("Enter a product you would like to remove/delete: ").lower()
    
    if delete_product in products:
        products.pop(delete_product)
    else:
        print("The product you typed is not in our inventory.")
    
    print(f"\nYou have successfully deleted the product {delete_product} from our inventory.")
    print("\nHere is the updated product list.")
    
    view()


def main():
    
    is_running = True
    while is_running:
        print("\n**********************************************************************************************************************************")
        print("Hello please choose one of the choices below to continue with the program.")
        print("\n\t1.View products")
        print("\n\t2.Update product details")
        print("\n\t3.Add new product")
        print("\n\t4.Delete product")
        print("\n\t5.Exit program")
        choice = input("\nKindly enter your choice(1-4): ")
        print("\n**********************************************************************************************************************************")
        
        if choice == "1":
            view()
        elif choice == "2":
            update()
        elif choice == "3":
            add()
        elif choice == "4":
            delete()
        elif choice == "5":
            is_running = False
        else:
            print("Please enter a valid choice (1-4)")
            
if __name__ == '__main__':
    main()            
        


