# Best burger
## A project made by Group-H from FHNW
### 💡 Idea
Our Idea stems from the desire to create the Best Burger to satisfy every type of dietary requirement. 

To do this, we’ve developed this program where customers can choose to build their own burger from scratch or select one of the options we’ve already created.

Customers can choose to pair the burger with a side dish and a drink to create a meal, or purchase just the burger. Once they have made their selection, they will see the nutritional information and price before proceeding to checkout.

### 🤔 problem we try to solve
We want to build a kiosk machine software where people can customize their desired burger or menu at peace, exactly as the indidual desires. It's important for the clients to know in real time the nutritional values they have on their plate each time, to offer transparency over how the menu is composed, so people can balance as they need.

👤 User Roles
| Role | Description |
|------|-------------|
| **Customer** | Orders burgers and wants to know what they have ordered, how much they need to pay and nutritional values of the order. |
| **Owner** | Runs the Burger shop, maintains the menu, keeps records of all sales and checks weekly reports. |

### 👥 User stories:
#### Andrei Cosmin Parnia:
1. As a customer, I want to have right data about orice, nutritional values and allergens, so that I can adjust the order.
2. As an owner, I want to have an admin pannel, so that I can check the orders.
3. As an owner, I want to have a weekly report with the sales, so I can take data driven decisions on existing and new products.

#### Filippo Paccagnella

#### Andrei Oros

### 🚧 Structure

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
#### Function tree

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

### how it works
1. The program starts by asking for the customer's name. Then the customer chooses between a preset burger, a custom burger, or extras only.
    1.1. The owner will have a dedicated name that will open the admin side of the program.
    1.2. The owner can access the recipes or weekdly sales reports

2. For preset burgers, the customer selects one of the available burgers and can add a menu with sides and a drink.

3. For custom burgers, the customer chooses the bun, patty, patty size, vegetables, and sauce. After that, they can add sides and a drink.

4. Before finishing, the program shows the total price and nutritional values. The customer can continue ordering, cancel the order, or choose a payment method. After the payment method is selected, the program generates a unique order number and saves the order details to a file.

