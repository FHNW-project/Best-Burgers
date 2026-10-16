# Best burger
### A project made by Group-H from FHNW
## 💡 Idea
Our Idea stems from the desire to create the Best Burger to satisfy every type of dietary requirement. 

To do this, we’ve developed this program where customers can choose to build their own burger from scratch or select one of the options we’ve already created.

Customers can choose to pair the burger with a side dish and a drink to create a meal, or purchase just the burger. Once they have made their selection, they will see the nutritional information and price before proceeding to checkout.

## 📝 Analysis

### 🤔 problem
People who love burgers (who) experience long queues and waiting times (what) during the ordering process of a custom burger at the casheer (where), resulting in frustrated customers/employees and a higher risk of mistakes (why).

## 💡 Scenario
Best Burger solves the problem of frustrated customers and employees in a Take-Away Imbiss by allowing the user create their own custom burger in a console, by selecting from a defined list of ingredients, automatically showing the costs and the nutritional values, getting discounts, paying and generate an invoice with the order number, without waiting in line.

### 👤 User Roles
| Role | Description |
|------|-------------|
| **Customer** | Orders burgers and wants to know what they have ordered, how much they need to pay and nutritional values of the order. |
| **Owner** | Runs the Burger shop, maintains the menu, keeps records of all sales and checks weekly reports. |

## 👥 User stories:

#### US-1: Title @Filippo Paccagnella
1. As a customer, I want to be able to customize a burger to satisfy my taste, allergies and dietary requirements. 

**Acceptance criteria:**
- The list of buns (with price and calories) will be displayed when the customer selects option 1 ("Create a Custom Burger") in the main menu.
- The list of patties (with price and calories) will be displayed after the customer choose the buns.
- The list of cheese (with price and calories) will be displayed after the customer choose the patties.
- The list of vegetables (with price and calories) will be displayed after the customer choose the cheese.
- The list of sauces (with price and calories) will be displayed after the customer choose the vegetables.
- After the choice of the sauce a recap of all the ingredients will be shown to the customer.
---
#### US-2: Title @Filippo Paccagnella
2. As a customer, I want to order a Preset burger to have a faster meal and try the chef's ideas. 

**Acceptance criteria:**
- The list of Preset Burger (with price and calories) will be displayed when the customer selects option 2 ("Choose a preset Burger") in the main menu.
---
#### US-3: Title @Filippo Paccagnella
3. As a customer, I want the possibility to order extras/sides and drinks to create a menu to get a full meal plan. 

**Acceptance criteria:**
-  After the choice of Custom or Preset burger the customer need to choose if they want to make a menu or not.
-  If the Customer choose "yes" the list of available Sides/Extra (with price and calories) will be shown to them.
-  After they choose they need to say if they want also a drink or not.
-  If they answer yes the list of available drink (with price and calories) will be shown to them.
-  After they select their option a recap of the order will be shown to them.
---
#### US-4: Group order @Andrei Parnia
4. As a customer, I want to be able to be able to order for an entire group, so the ordering is fast.

**Acceptence criteria:**
- TBD
---
#### US-5: Current costs @Andrei Oros
5. As a customer, I want to see the current subtotal with VAT included after every decision at every step of the order, so that I know when to stop ordering.

**Acceptance criteria:**
- Given the Customer navigates through the ordering process, when they have to make a choice at every step, then the Current Cost (Subtotal incl. VAT) is showed in the prompt.
- Given the Subtotal shows in the prompt, when it's value is above 0, then it's formated like "Your Subtotal is now CHF 123.45 (incl. VAT)  | " and followed by the prompt "Enter your selection: "
- Given the Shopping Basket is empty, when the Customer navigates through the Program, then the subtotal is not showing.
---
#### US-6: Nutritional values and allergens @Andrei Parnia
6. As a customer, I want to know the  nutritional values and allergens of my selected products.

**Acceptance criteria:**
- *Given* different products or elements of a product have different nutritional values, **when** the customer orders a product or builds a burger, nutritional values will be calculated *then* the `calories`, `Fats`, `Sugars`, `Protein` and `Fibers` will be displayed on the screen.
- *Given* the customer is decided on a product, *when* it goes to payment, it will have displayed the final nutritional values, *then* the customer takes an assumed decision.  
---
#### US-7: Costs and Taxes @Andrei Oros
7. As a customer, I want to see the Final Order, the Total Cost, the Subtotal, the VAT rate, and VAT amount before checking out, to make sure they have ordered everything right.

**Acceptance criteria:**
- Given the Customer finished ordering, when they are selecting to "Finish your order", then the ordered items are listed in the format "Item number, Item Name, Pieces ordered, Item price, VAT rate"
- Given the Customer is not sure about the Order, when they are at the Final Order page, then they have the option to "Cancel the Order".
---
#### US-8: Discounts for Students @Andrei Oros
7. As a Customer, I also want to apply my student status during the final order review, so that I can receive a discount on my purchase.

**Acceptance criteria:**
- Given the customer is on the Final Order page, when they are asked if they are a Student, then they have to confirm with yes or no.
- Given the customer answered the question, when they confirm their Student Status, then they asked for the Matriculation Number to validate the eligibility or to bypass the step.
- Given the customer entered their Matriculation number, when the eligibility is confirmed, then the 10% discount is applied to the Total Cost.
- Given the discount is confirmed, when the Total Cost is updated, then the Customer can go further to check-out.
- Given the customer is not interested in the Student Discount, when they are facing the Final Order page, they can ignore "Cancel your Order", "Student Discount" and select "Continue to Payment".

---
#### US-9: Payment Methods @Andrei Oros
7. As a Customer, after confirming the Order I want to have different payment options (cash or card), so that I can pay with the method of my choice.

**Acceptance criteria:**
- Given the customer continues to payment, when they check-out, then they can choose betwen paying Cash or Card.
- Given the customer doesn't have cash, when they select Card, then they have to type in their Card Details and CVV code. (card payment simulation)
- Given the customer wants to pay cash, when they select Cash, then they receive the Invoice with the Order number and they can use it to pay when they pick-up their Order.
---

#### US-10: Receiving an Invoice @Andrei Oros
8. As a customer, after the payment is succesful I want to receive a printed invoice with the order number and all the details so I can pickup the order, and for tax purposes.

**Acceptance criteria:**
- After the payment is accepted, the details of the order are written to a new .txt file stored in the orders folder, so that the customer gets a printed copy and the order gets processed.
- The invoice file is created, it is named by the date and the order number, so they can be filtered by date and have unique series.
- The invoice saves the following details: business location, date of the order, client name, order number, items per piece ordered with their respective cost and VAT rate,
  the total nutritional value, alergens contained, subtotal and total cost, payment method, and a good bye message, so that the customer has a clear record of it's purchase.
- Given the Invoice is ready, when the data is printed on the screen in the console, then the program counts down 20 seconds until it resets to the first step "Hello".
- After the creation of the invoice file, they should be accesible by the Administrator, so that they can be used for further processes
---
#### US-11: Admin menu @Andrei Parnia
9. As an owner, I want to have an admin panel, where I can check the previous orders, and get a weekly sales report so I can take data driven decisions on existing and new products.
**Acceptance criteria:**
- *Given* the owner needs to check the previous orders, *when* it access the `Admin` menu by entering the `Administrator` name at the greeting screen, *then* it will be able to access all the previous orders done. 
- *Given* the owner needs to understand the sales, *when* accessing the `Admin` menu, *then* can see a weekly report with income from sales, quantity of products sold and a comparation with the previous week.
- *Given* the owner needs to know the available stock, *when* accessing the `Admin` menu, *then* it can see the available stock of each product it has in the store.

## 🚧 Structure

```mermaid
flowchart TD
start["Start"] --> ask_name["Ask customer name"]
ask_name --> check_admin["Username = admin?"]
check_admin -->|Yes| admin_menu["Admin menu"]
admin_menu --> passowrd["admin passowrd"]
check_admin -->|No| order_type["Choose order type"]
passowrd --> invoices["check invoices"]
passowrd --> report["Check weekly report"]
invoices --> download["Donwload"]
report --> download["Donwload"]

order_type --> preset_burger["Preset burger"]
order_type --> custom_burger["Custom burger"]
order_type --> extras_only["Extras only"]

preset_burger --> select_preset["Select preset burger"]
select_preset --> ask_menu["Ask if menu"]
ask_menu -->|Yes| choose_menu_items["Choose side, drink, size"]
ask_menu -->|No| skip_menu["Skip menu"]

custom_burger --> choose_bun["Choose bun"]
choose_bun --> choose_patty_type["Choose patty type"]
choose_patty_type --> choose_patty_size["Choose patty size"]
choose_patty_size --> choose_vegetables["Choose vegetables"]
choose_vegetables --> choose_sauce["Choose sauce"]
choose_sauce --> ask_menu

extras_only --> choose_menu_items

choose_menu_items --> show_summary["Show price and nutrition"]
skip_menu --> show_summary
show_summary --> continue_order["Continue order"]
show_summary --> go_payment["Go to payment"]
show_summary --> cancel_order["Cancel order"]

continue_order --> order_type
go_payment --> payment_options["Choose payment options"]

payment_options --> confirm_payment["Confirm payment"]
confirm_payment --> generate_order_number["Generate unique order number"]
generate_order_number --> save_order["Save order details to file"]
save_order --> show_goodbye["Show order number and goodbye"]
show_goodbye --> delay["wait 15 seconds"]
delay -->|Start new order| ask_name
```
## Function tree

```text
best_burger/
├── main.py
├── menu_data.py
├── calculators.py
├── order.py
├── data/
│   ├── ingredients.csv
│   ├── preset_burgers.csv
│   ├── sides.csv
│   ├── drinks.csv
│   └── orders.csv
└── README.md
```

## how it works
1. The program starts by asking for the customer's name. Then the customer chooses between a preset burger, a custom burger, or extras only.
    1.1. The owner will have a dedicated name that will open the admin side of the program.
    1.2. The owner can access the recipes or weekdly sales reports

2. For preset burgers, the customer selects one of the available burgers and can add a menu with sides and a drink.

3. For custom burgers, the customer chooses the bun, patty, patty size, vegetables, and sauce. After that, they can add sides and a drink.

4. Before finishing, the program shows the total price and nutritional values. The customer can continue ordering, cancel the order, or choose a payment method. After the payment method is selected, the program generates a unique order number and saves the order details to a file.

