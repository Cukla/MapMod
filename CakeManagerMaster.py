from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from time import strftime

width = 0.06 - 0.01
height = 0.06 - 0.01
houry = 0.28
total_value = 0
name_list = []
prices_list = []
name_price = []
prices = []
str_value = []
int_value = []
button = []
clients_names_list = []
record_values = []
processed_record_values = []
label = []
labell = []
edited_prices = []
description_list = []
dates_list = []
edited_prices_name = []
entry = []
orders_list = []
edit_value = 0
color_interface = "#e6e6e6"
contrast_color_interface = "#f2f2f2"
frame = []
type_entrace = " "
entry_dict = {}
time_elapsed = " "
exit_condition = 0
total_value = 0
index = 0
new_date = ""
order_str = []
foo2 = []
num = 0
order_labell = []
order_label = []
order_prices = []
order_price_list = []
ing_p_val = []
ing_n_val = []

# this saves the prices of the orders
order_price_file = open("order_price.txt", "r+")
order_price_list = order_price_file.readlines()
order_price_file.close()
for j in range(len(order_price_list)):
    if order_price_list[j] != "\n" and order_price_list[j] != " " or order_price_list[j] is not False:
        order_prices.append(order_price_list[j].replace("\n", ""))


def data_manager(fut_vary, name):
    # this saves the values from entryPriceAdd to prices.txt
    entry_price = fut_vary
    my_price = open(name, "a+")
    if entry_price != " " or entry_price != "" or entry_price != "\n" or entry_price is not False:
        my_price.write(entry_price + "\n")
    my_price.close()


def data_manager_comb(fut_name, name, fut_price, price):
    data_manager(fut_name, name)
    data_manager(fut_price, price)

# esto guarda los datos en txt files
my_name = open("names.txt", "r+")
name_list = my_name.readlines()
my_name.close()

my_ing_n = open("recipe_name.txt", "r+")
ing_n = my_ing_n.readlines()
my_ing_n.close()

my_ing_p = open("recipe_price.txt", "r+")
ing_p = my_ing_p.readlines()
my_ing_p.close()

my_price = open("prices.txt", "r+")
prices_list = my_price.readlines()
my_price.close()

date_file = open("dates.txt", "r+")
dates = date_file.readlines()
date_file.close()

orders_file = open("order.txt", "r+")

for line in orders_file:
    stripped_line_order = line.strip()
    line_list_orders = stripped_line_order.split()
    orders_list.append(line_list_orders)

orders_file.close()

description_file = open("description.txt", "r+")
descriptions = description_file.readlines()
description_file.close()

for j in range(len(descriptions)):
    if descriptions[j] != "\n" and descriptions[j] != " " or descriptions[j] is not False:
        description_list.append(descriptions[j].replace("\n", ""))

for j in range(len(ing_n)):
    if ing_n[j] != "\n" and ing_n[j] != " ":
        ing_n_val.append(ing_n[j].replace("\n", ""))
    if ing_p[j] != "\n" and ing_p[j] != " ":
        ing_p_val.append(ing_p[j].replace("\n", ""))


def show_ingredients(tab, p, row):
    global ing_n_val, ing_p_val, row1
    dict = {"canvas_add": canvas_add, "ingredients_frame": ingredients_frame}
    if p == 1:
        ing_button = tk.Button(dict[tab], text="Agregar ingrediente: ", relief=RAISED, width=17)
        ing_button.grid(row=0, column=0)
        name_ing = tk.Entry(dict[tab], relief=RAISED, width=17)
        name_ing.grid(row=1, column=0)
        price_ing = tk.Entry(dict[tab], relief=RAISED, width=10)
        price_ing.grid(row=1, column=1)
        ing_price_btn = tk.Button(dict[tab], text="Confirmar",
                               command=lambda: data_manager_comb(name_ing.get(), "recipe_name.txt", price_ing.get(), "recipe_price.txt"), relief=RAISED,
                               width=8)
        ing_price_btn.grid(row=1, column=2)
    ing_name_lbl = []
    ing_price_lbl = []
    i = 0
    row = row
    for i in range(len(ing_n_val)):
        row = row + 1
        button.append(name_price[i] + "button" + str(i))
        ing_name_lbl.append(prices[i] + "lbl" + str(i))
        entry.append("Spinbox" + str(i))
        ing_price_lbl.append(prices[i] + "lbll" + str(i))
        ing_name_lbl[i] = tk.Label(dict[tab], text=ing_n_val[i], height=2, relief=None, bg=contrast_color_interface, width=17)
        ing_name_lbl[i].grid(row=row + 1, column=0)
        ing_price_lbl[i] = tk.Label(dict[tab], text=ing_p_val[i], height=2, relief=None, bg=contrast_color_interface, width=10)
        ing_price_lbl[i].grid(row=row + 1, column=1)
        if p == 2:
            tk.Spinbox(dict[tab], width=2).grid(row=row + 1, column=2)
    row1 = row

    row = 0

# this show the menu for clients
def show_orders():
    global orders_list, prices_list, order_str, index, foo2, num, order_labell, order_label
    num = num + 1
    foo2.clear()

    order_list = orders_list[index]
    cunt = 0
    for i in range(len(order_list)):
        foo = name_price[i] + " " + order_list[i]
        for element in range(len(foo)):
            coun = foo[element].count("0")
            cunt = cunt + coun
        element = 0
        if cunt == 0:
            foo2.append(foo)
        cunt = 0
    row1 = 0
    order_str2 = ""
    for j in range(len(foo2)):
        if num == 1:
            for p in range(len(order_labell)):
                order_labell[p].config(text="                                                                         ")
            num = 0
            p = 0

        row1 = row1 + 1
        if j == 0:
            order_label = []
            order_label.clear()
            order_labell = []
            order_labell.clear()
        order_label.append(foo2[j]+"lbl")
        order_str2 = str(foo2[j])
        order_label[j] = tk.Label(order_frame, text=order_str2, width=30)
        order_labell.append(order_label[j])
        order_labell[j].grid(row=row1, column=0)

        order_str2 = ""


def show_menu_clients():
    global clients_names_list, order_str
    var = IntVar()

    name_label = tk.Label(clients_frame)
    global order_canvas, order_frame
    order_canvas = tk.Canvas(clients_frame)
    order_frame = tk.Frame(order_canvas)

    description_message = tk.Message(clients_frame)

    oder_scrollbar = ttk.Scrollbar(order_canvas, orient="vertical", command=canvas.yview)
    oder_scrollbar.configure(command=order_canvas.yview)
    oder_scrollbar.place(relx=0.93, relwidth=0.07, relheight=1)
    order_frame.bind("<Configure>", lambda e: order_canvas.configure(scrollregion=order_canvas.bbox("all")))
    order_canvas.create_window((0, 0), window=order_frame, anchor="nw")
    order_canvas.configure(yscrollcommand=oder_scrollbar.set)

    def clients_interface(var):
        global order_label, order_prices
        description_label = tk.Label(clients_frame, bg=color_interface, text="Descripcion", relief=RAISED)
        description_label.place(relx=0.4, rely=0.05, relwidth=0.25, relheight=0.05)
        order_label = tk.Label(clients_frame, bg=color_interface, text="Pedido", relief=RAISED)
        order_label.place(relx=0.67, rely=0.05, relwidth=0.25, relheight=0.05)
        order_prices_lbl = tk.Label(clients_frame)
        order_prices_lbl.place(relx=0.67, rely=0.51, relwidth=0.25, relheight=0.05)
        global clients_names_list, dates_list, index, foo2
        index = var
        order_prices_lbl.config(text="El total es: " + str(order_prices[index]), relief=RAISED, bg=color_interface)
        name_label.config(text="Nombre: " + clients_names_list[index], relief=RAISED, height=2)
        name_label.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.05)
        rest_time_label.place(relx=0.05, rely=0.11, relwidth=0.3, relheight=0.05)
        define_time()
        rest_time_label.config(text="El tiempo restante es: " + str(time_elapsed), relief=RAISED, height=2)
        description_message.config(text=description_list[index], bg=color_interface, relief=RAISED)
        description_message.place(relx=0.4, rely=0.1, relwidth=0.25, relheight=0.4)
        description_message.grid_propagate()
        show_orders()
        order_canvas.place(relx=0.67, rely=0.1, relwidth=0.25, relheight=0.4)
        order_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    clients_menu = []
    y = 0
    for i in range(len(clients_names_list)):
        clients_menu.append("clients_menu" + str(i))
        clients_menu[i] = tk.Radiobutton(canvas_menu_clients, text=clients_names_list[i], variable=var, value=i, command=lambda :clients_interface(var.get()), bg=color_interface)
        clients_menu[i].place(relx=0, rely=y , relwidth=1, relheight=0.07)
        y = y + 0.07
# this show the news products


def show_products(type_entrace, row, tab):
    global labell, button, label, frame, entry, record_values, total_value, exit_condition

    dict = {"clients_frame": clients_frame, "products_frame": products_frame, "registration_frame": registration_frame,
            "canvas": canvas, "canvas_add": canvas_add}
    i = 0

    for i in range(len(prices)):
        row = row+1
        button.append(name_price[i] + "button" + str(i))
        label.append(prices[i] + "lbl" + str(i))
        entry.append("Spinbox" + str(i))
        labell.append(prices[i] + "lbll" + str(i))
        label[i] = tk.Label(dict[tab], text=name_price[i], height =2, relief=None, bg=color_interface, width=21)
        label[i].grid(row=row+1, column=0)
        labell[i] = tk.Label(dict[tab], text=prices[i], height =2, relief=None, bg=color_interface, width=9)
        labell[i].grid(row=row+1, column=1)
        if type_entrace == "button":
            button[i] = tk.Button(dict[tab], image = photoimage,
                            command=lambda edit_value=i: data_remplacer_interface(edit_value), relief=None, bg=color_interface)
            button[i].grid(row=row+1, column=2)
        else:
            entry[i] = tk.Spinbox(dict[tab], from_=0, to=1000, width=2, relief=None, bg=color_interface)
            entry[i].grid(row=row+1, column=2)
            entry_dict[str(entry[i])] = entry[i]
        if exit_condition == 1:
            exit_condition = 0
            update_list()
            return

    i = 0

# this function gives the total of the record
    def get_amounts():
        record_values.clear()
        global processed_record_values, total_value, order_prices, total_value
        new_record_values = []
        for i in range(len(prices)):
            record_values.append(entry_dict[str(entry[i])].get())
            processed_record_values.append(float(prices[i]) * float(record_values[i]))

        total_value = sum(processed_record_values)
        processed_record_values.clear()
        record_button_label.config(text="El total es: " + str(total_value), relief=RAISED, bg=color_interface)

    if type_entrace != "button":
        record_button = tk.Button(dict[tab], text="Calcular", command=lambda: get_amounts(), relief=RAISED, bg=color_interface)
        record_button.grid(row=row+2, column=0)
        record_button_label = tk.Label(dict[tab])
        record_button_label.grid(row=row + 2, column=1)

        record_client_button = tk.Button(dict[tab], relief=RAISED,bg=color_interface, text="Registrar cliente", command=lambda: combine_funcs(clients_day_entry.get(),clients_hour_entry.get(), record_values, clients_name_entry.get(), description_entry.get(), total_value))
        record_client_button.grid(row=row+3, column=0)


def manage_clients_orders(record_values):
    # this saves the values from record_values to order.txt
    global orders_list
    my_orders = open("order.txt", "a+")
    for i in range(len(record_values)):
        if record_values[i] != " " or record_values[i] != "" or record_values[i] != "\n":
            my_orders.write(record_values[i] + " ")
    my_orders.write(" \n")
    my_orders.close()


def combine_funcs(day, hour, records, c_name, descrip_e, t_v):
    manage_time(day, hour)
    manage_clients_orders(records)
    manage_names(c_name)
    manage_descriptions(descrip_e)
    show_menu_clients()
    manage_order_prices(t_v)

# this function saves the order prices into a txt file

def manage_order_prices(order_pr):
    order_price = order_pr
    print(type(order_price))

# this saves the clients name into the clients_name.txt
    order_price_file = open("order_price.txt", "a+")
    if order_price != "\n" and order_price != " " or order_price is not False:
        order_price_file.write(str(order_price)+ " \n")
    order_price_file.close()

# this function manages the descriptions
def manage_descriptions(description_entry):
    global description_list
    description = description_entry

# this saves the clients name into the clients_name.txt
    description_file = open("description.txt", "a+")
    if description != "\n" and description != " " or description is not False:
        description_file.write(description + " \n")
    description_file.close()

# this adds all the names from descriptions.txt to description_list
    description_file = open("clients_name.txt", "r+")
    descriptions = description_file.readlines()
    description_file.close()
    for j in range(len(descriptions)):
        if descriptions[j] != "\n" and descriptions[j] != " " or descriptions[j] is not False:
            description_list.append(descriptions[j].replace("\n", ""))

# this function manages the clients names
def manage_names(clients_name_entry):
    global clients_names_list
    clients_name = clients_name_entry

# this saves the clients name into the clients_name.txt
    clients_name_file = open("clients_name.txt", "a+")
    if clients_name != "\n" and clients_name != " " or clients_name is not False:
        clients_name_file.write(clients_name + " \n")
    clients_name_file.close()

def show_names():
    # this adds all the names from clients_name.txt to names_list
    clients_name_file = open("clients_name.txt", "r+")
    names = clients_name_file.readlines()
    clients_name_file.close()
    for j in range(len(names)):
        if names[j] != "\n" and names[j] != " " or names[j] is not False:
            clients_names_list.append(names[j].replace("\n", ""))


show_names()
# this updates the list
def update_list():

    global name_list, prices_list
    my_name = open("names.txt", "r+")
    name_list = my_name.readlines()
    my_name.close()

    my_price = open("prices.txt", "r+")
    prices_list = my_price.readlines()
    my_price.close()

def define_time():
# this calculates the rest time to the delivery
    global dates_list, time_elapsed, index, new_date
    new_date = ""
    for i in range(19):
        new_date = new_date + dates_list[int(index)][i]

    calculate_time()


now = ""


def calculate_time():
    global new_date, time_elapsed, now
    new_date = datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S')
    now = strftime('%Y-%m-%d %H:%M:%S')
    now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
    time_elapsed = new_date - now
    #print_time()


def print_time():
    global new_date, time_elapsed
    time_elapsed = new_date - now
    root.after(1000, calculate_time())


def manage_time(clients_day_entry, clients_hour_entry):
# this calculates the rest time to the delivery
    global dates_list, time_elapsed, dates
    date_str = clients_day_entry + " " + clients_hour_entry + ":00"
    date_dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')


# this saves the dates
    date_file = open("dates.txt", "a+")
    date_file.write(str(date_dt) + " \n")
    date_file.close()

# this adds all the dates from dates.txt to dates_list

for j in range(len(dates)):
    if dates[j] != "\n" and dates[j] != " ":
        dates_list.append(dates[j].replace("\n", ""))


# this takes off the "\n" of the string name, to avoid a problem with tkinter, also if the value is inexistent
# it ignores it
for j in range(len(name_list)):
    if name_list[j] != "\n" and name_list[j] != " ":
        str_value.append(name_list[j].replace("\n", ""))
    if prices_list[j] != "\n" and prices_list[j] != " " :
        int_value.append(prices_list[j].replace("\n", ""))

name_price = str_value
prices = int_value


# esto guarda los datos en txt files
# this is an interface that shows up when you press the button "editar"
def data_remplacer_interface(edit_value):
    edit_frame = tk.Label(root, bg=contrast_color_interface)
    edit_frame.place(relx=0.25, rely=0.15, relwidth=0.50, relheight=0.25)
    close_button = tk.Button(edit_frame, bg="#ff0000", text="X", command=lambda: edit_frame.place_forget())
    close_button.place(relx=0.95, rely=0, relwidth=0.05, relheight=0.1)

    edit_entry_price = tk.Entry(edit_frame)
    edit_entry_price.place(relx=0.05, rely=0.79, relwidth=0.5, relheight=0.2)
    edit_button = tk.Button(edit_frame, text="Editar",
                            command=lambda: data_remplacer_price(edit_value, edit_entry_price.get()))
    edit_button.place(relx=0.56, rely=0.79, relwidth=0.1, relheight=0.2)
    edit_label_price = tk.Label(edit_frame, text="precio: ")
    edit_label_price.place(relx=0.05, rely=0.55, relwidth=0.5, relheight=0.2)

    edit_entry_name = tk.Entry(edit_frame)
    edit_entry_name.place(relx=0.05, rely=0.31, relwidth=0.5, relheight=0.2)
    edit_button_name = tk.Button(edit_frame, text="Editar",
                                 command=lambda: data_remplacer_name(edit_value, edit_entry_name.get()))
    edit_button_name.place(relx=0.56, rely=0.31, relwidth=0.1, relheight=0.2)
    edit_label_name = tk.Label(edit_frame, text="nombre: ")
    edit_label_name.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=0.2)
    delete_product = tk.Button(edit_frame, text="Borrar",
                                 command=lambda: data_deleter_product(edit_value))
    delete_product.place(relx=0.76, rely=0.42, relwidth=0.1, relheight=0.2)


# this funtion edits the value of the prices in prices.txt
def data_remplacer_price(edit_value, edit_entry_price):
    global prices_list, edited_prices
    editentryprice = edit_entry_price
    edited_prices.extend(prices_list)
    edited_prices[edit_value] = editentryprice + "\n"
    my_pricees = open("prices.txt", "w+")
    for o in range(len(edited_prices)):
        my_pricees.write(edited_prices[o])
    my_pricees.close()


# this function edits the value of the names in names.txt
def data_remplacer_name(edit_value, edit_entry_name):
    global name_list, edited_prices_name
    editentryname = edit_entry_name
    edited_prices_name.extend(name_list)
    edited_prices_name[edit_value] = editentryname + "\n"
    my_names = open("names.txt", "w+")
    for h in range(len(edited_prices_name)):
        my_names.write(edited_prices_name[h])
    my_names.close()


def data_deleter_product(edit_value):
    global name_list, prices_list, edited_prices, edited_prices_name
    edited_prices.extend(prices_list)
    del edited_prices[edit_value]
    edited_prices_name.extend(name_list)
    del edited_prices_name[edit_value]
    my_names = open("names.txt", "w+")
    for h in range(len(edited_prices_name)):
        my_names.write(edited_prices_name[h])
    my_names.close()

    my_pricees = open("prices.txt", "w+")
    for o in range(len(edited_prices)):
        my_pricees.write(edited_prices[o])

    name_list = edited_prices_name
    prices_list = edited_prices
    edited_prices_name.clear()
    edited_prices.clear()
    update_list()


WIDTH = 1600
HEIGHT = 900

root = tk.Tk()
photo = PhotoImage(file = r"/home/casa/PycharmProjects/cakeproject/tuerca.png")
photoimage = photo.subsample(3, 3)

#root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.wm_state('normal')
canvas = tk.Canvas(root, bg="#e6ffff")
canvas.place(relheight=1, relwidth=1)
root.title("Cake Manager Master")
canvas_products = tk.Canvas(root, bg=color_interface)
canvas_products.place(relx=0.762, rely=0, relwidth=0.24, relheight=0.495)
canvas_registry = tk.Canvas(root)
canvas_registry.place(relx=0.762, rely=0.5, relwidth=0.24, relheight=0.50)
canvas_menu_clients = tk.Canvas(root, bg=color_interface)
canvas_menu_clients.place(relx=0.001, rely=0.001, relwidth=0.147, relheight=0.65)
canvas_clients = tk.Canvas(root, bg=color_interface)
canvas_clients.place(relx=0.15, rely=0.001, relwidth=0.61, relheight=0.65)
canvas_ingredients = tk.Canvas(root, bg=color_interface)
canvas_ingredients.place(relx=0.53, rely=0.655, relwidth=0.23, relheight=0.35)
canvas_add = tk.Canvas(root, bg=color_interface)
# this is the tabs clients
ingredients_frame = tk.Frame(canvas_ingredients, bg=contrast_color_interface, relief=GROOVE)
ingredients_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

products_frame = tk.Frame(canvas_products, bg=contrast_color_interface, relief=GROOVE)
products_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

registration_frame = tk.Frame(canvas_registry, bg=contrast_color_interface, relief=GROOVE)
registration_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

clients_frame = tk.Frame(canvas_clients, bg=contrast_color_interface, relief=GROOVE)
clients_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

clients_menu_frame = tk.Frame(canvas_menu_clients, bg=contrast_color_interface, relief=GROOVE)
clients_menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

rest_time_label = tk.Label(clients_frame, relief=RAISED)

#products ingredients
scrollbar_ingredients = ttk.Scrollbar(canvas_ingredients, orient="vertical", command=canvas.yview)
scrollbar_ingredients.configure(command=canvas_ingredients.yview)
scrollbar_ingredients.place(relx=0.93, relwidth=0.07, relheight=1)
ingredients_frame.bind("<Configure>",lambda e: canvas_ingredients.configure(scrollregion=canvas_ingredients.bbox("all")))
canvas_ingredients.create_window((0, 0), window=ingredients_frame, anchor="nw")
canvas_ingredients.configure(yscrollcommand=scrollbar_ingredients.set)

#products scrollbar
scrollbar_products = ttk.Scrollbar(canvas_products, orient="vertical", command=canvas.yview)
scrollbar_products.configure(command=canvas_products.yview)
scrollbar_products.place(relx=0.93, relwidth=0.07, relheight=1)
products_frame.bind("<Configure>",lambda e: canvas_products.configure(scrollregion=canvas_products.bbox("all")))
canvas_products.create_window((0, 0), window=products_frame, anchor="nw")
canvas_products.configure(yscrollcommand=scrollbar_products.set)

show_ingredients("ingredients_frame", 1, 1)
#registry scrollbar
scrollbar_registry = ttk.Scrollbar(canvas_registry, orient="vertical", command=canvas.yview)
scrollbar_registry.configure(command=canvas_registry.yview)
scrollbar_registry.place(relx=0.94, relwidth=0.06, relheight=1)
registration_frame.bind(
    "<Configure>",
    lambda e: canvas_registry.configure(
        scrollregion=canvas_registry.bbox("all")
    )
)
canvas_registry.create_window((0, 0), window=registration_frame, anchor="nw")
canvas_registry.configure(yscrollcommand=scrollbar_registry.set)


def add_products():
    global row1
    canvas_add.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.40)
    hide_button = tk.Button(canvas_add, text="X", command=lambda: canvas_add.place_forget())
    hide_button.place(relx=0.9, relwidth=0.1, relheight=0.1)
    show_ingredients("canvas_add", 2, 1)

# this is the interface to add new products
#frame_add = tk.Frame(products_frame, bg=contrast_color_interface)
#frame_add.grid(row=0, column=0)
priceAdd = tk.Button(products_frame, text="Agregar receta", relief=RAISED, command=lambda: add_products())
priceAdd.grid(row=0, column=0)
tk.Label(canvas_add, text="Nombre del producto").grid(row=1, column=0)
entryNameAdd = tk.Entry(canvas_add, relief=RAISED, width=15)
entryNameAdd.grid(row=1, column=1)
tk.Label(canvas_add, text="Precio del producto   ").grid(row=2, column=0)
entryPriceAdd = tk.Entry(canvas_add, relief=RAISED, width=15)
entryPriceAdd.grid(row=2, column=1)
buttonPriceAdd = tk.Button(canvas_add, text="Confirmar",
                           command=lambda: data_manager_comb(entryNameAdd.get(), "names.txt", entryPriceAdd.get(), "prices.txt", 0), relief=RAISED, width=7)
buttonPriceAdd.grid(row=row1+2, column=1)

show_products("button", 0, "products_frame")

# this is the records tab
# this is the interface for the clients creation tab
new_clients_label = tk.Label(registration_frame, text="Registrar un nuevo cliente:", relief=RAISED)
new_clients_label.grid(row=0, column=0)
# name
clients_name_label = tk.Label(registration_frame, text="Nombre:", relief=RAISED, width=18)
clients_name_label.grid(row=1, column=0)
clients_name_entry = tk.Entry(registration_frame, width=14, relief=RAISED)
clients_name_entry.grid(row=1, column=1)
# date

clients_date_label = tk.Label(registration_frame, text="Fecha de entrega:", relief=RAISED, width=18)
clients_date_label.grid(row=3, column=0)
clients_day_entry = tk.Entry(registration_frame, width=14, relief=RAISED)
clients_day_entry.grid(row=3, column=1)


clients_hour_label = tk.Label(registration_frame, text="Hora:", relief=RAISED, width=18)
clients_hour_label.grid(row=4, column=0)
clients_hour_entry = tk.Entry(registration_frame, width=14, relief=RAISED)
clients_hour_entry.grid(row=4, column=1)


description_label = tk.Label(registration_frame, text="Descripcion:", relief=RAISED, width=18)
description_label.grid(row=5, column=0)
description_entry = tk.Entry(registration_frame, width=14, relief=RAISED, text="Descripcion")
description_entry.grid(row=5, column=1)

show_products("lala", 5, "registration_frame")
# this is the records tab

# this is the clients tab
# this is the description message
#fr_description_message = tk.Frame(canvas, bg=color_interface)
#fr_description_message.place(relx=0.6, rely=0.05, relwidth=0.35, relheight=0.25)
#description_message = tk.Message(fr_description_message)
#description_message.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
# this is the name label
#fr_name_label = tk.Frame(canvas, bg=color_interface)
#fr_name_label.place(relx=0.2, rely=0.05, relwidth=0.35, relheight=0.05)
#name_label = tk.Message(fr_name_label)
#name_label.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.8)

# this is the clients tab
show_menu_clients()
root.mainloop()

# python CakeManagerMaster.py
