import json

class Book:
    def __init__(self, title, author, genre, price, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.availability = availability


data = []  

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 10.99, "In stock")
book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 12.99, "In stock")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "Classic", 9.99, "Out stock")

data.append({
    "title" : book1.title,
    "author" : book1.author,
    "genre" : book1.genre,
    "price" : book1.price,
    "availability" : book1.availability
})
data.append({
    "title" : book2.title,
    "author" : book2.author,
    "genre" : book2.genre,
    "price" : book2.price,
    "availability" : book2.availability
})
data.append({
    "title" : book3.title,
    "author" : book3.author,
    "genre" : book3.genre,
    "price" : book3.price,
    "availability" : book3.availability
})



def browse():
    with open('data.json', 'r') as file:
        books = json.load(file)
        index = 1
        print('--- Browse Books ---')
        for i in books:
            print(f'{index}. Title: {books[index-1]["title"]} | Author: {books[index-1]["author"]} | Genre: {books[index-1]["genre"]} | Price: {books[index-1]["price"]}$ | Availability: {books[index-1]["availability"]}')
            index+= 1
    while True:
        brouse_choice = int(input('Enter the number of the book to add to cart (or 0 to go back): '))
        if brouse_choice == 0:
            break
        elif brouse_choice <= len(books):
            cart.append({
                "title" : books[brouse_choice-1]["title"],
                "author" : books[brouse_choice-1]["author"],
                "price" : books[brouse_choice-1]["price"]
            })
            print("Added "+books[brouse_choice-1]["title"]+" to your cart.")
            break
        else:
            print('Invalid choice!')    
cart = []
def view_cart():
    print('--- Cart ---')
    index = 1
    price = 0
    for item in cart:
        print(f'{index}. Title: {cart[index-1]["title"]} | Author: {cart[index-1]["author"]} | Price: {cart[index-1]["price"]}$')
        price += cart[index-1]["price"]
        index+= 1
        
    print('Total price: '+str(price))

def checkout():
    global cart
    print('--- Checkout ---')
    print('Order summary:')
    index = 1
    price = 0
    for item in cart:
        print(f'{index}. Title: {cart[index-1]["title"]} | Author: {cart[index-1]["author"]} | Price: {cart[index-1]["price"]}$')
        price += cart[index-1]["price"]
        index+= 1
        
    print('Total price: '+str(price))
    while True:
        checkout_choice = input('Confirm your purchase (Y/N): ').upper()
        if checkout_choice == 'Y':
            print('Thank you for your purchase! Your order will be shipped soon.')
            cart = []
            break
        elif checkout_choice == 'N':
            break
        else:
            print('Invalid choice!')    


with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

while True:
    print('''Welcome to the Online Bookstore!

    1. Browse Books
    2. Search by Title
    3. Search by Author
    4. View Cart
    5. Checkout
    6. Exit
    ''')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        browse()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        view_cart()
    elif choice == 5:
        checkout()
    elif choice == 6:
        print('Goodbye! Have a great day!')
        quit()    