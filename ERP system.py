import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from tkcalendar import DateEntry
import json
import os
from datetime import datetime
import csv

# Pliki do przechowywania danych
MACHINES_FILE = "machines.json"
ORDERS_FILE = "orders.json"
DELETED_ORDERS_FILE = "deleted_orders.json"
COMPLETED_ORDERS_FILE = "completed_orders.json"
ARCHIVED_ORDERS_FILE = "archived_orders.json"
ARTICLES_FILE = "articles.json"
MATERIALS_FILE = "materials.json"
RECEIVED_PRODUCTS_FILE = "received_products.json"
TOOLS_FILE = "tools.json"
INSTRUCTIONS_FILE = "instructions.json"
ANALYSIS_FILE = "analysis.json"
CLOSED_ANALYSIS_FILE = "closed_analysis.json"
PARTS_WAREHOUSE_FILE = "parts_warehouse.json"


# Globalne listy danych
machines_list = []
orders_list = []
deleted_orders_list = []
completed_orders_list = []
archived_orders_list = []
articles_list = []
materials_list = []
received_products_list = []
tools_list = []
instructions_list = []
analysis_list = []
closed_analysis_list = []
parts_warehouse_list = []


# Funkcje do zapisu i odczytu danych
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return []

def load_all_data():
    global machines_list, orders_list, deleted_orders_list, completed_orders_list, archived_orders_list, articles_list, materials_list, received_products_list, tools_list, instructions_list, analysis_list, closed_analysis_list
    machines_list = load_data(MACHINES_FILE)
    orders_list = load_data(ORDERS_FILE)
    deleted_orders_list = load_data(DELETED_ORDERS_FILE)
    completed_orders_list = load_data(COMPLETED_ORDERS_FILE)
    archived_orders_list = load_data(ARCHIVED_ORDERS_FILE)
    articles_list = load_data(ARTICLES_FILE)
    materials_list = load_data(MATERIALS_FILE)
    received_products_list = load_data(RECEIVED_PRODUCTS_FILE)
    tools_list = load_data(TOOLS_FILE)
    instructions_list = load_data(INSTRUCTIONS_FILE)
    analysis_list = load_data(ANALYSIS_FILE)
    closed_analysis_list = load_data(CLOSED_ANALYSIS_FILE)

def save_all_data():
    save_data(MACHINES_FILE, machines_list)
    save_data(ORDERS_FILE, orders_list)
    save_data(DELETED_ORDERS_FILE, deleted_orders_list)
    save_data(COMPLETED_ORDERS_FILE, completed_orders_list)
    save_data(ARCHIVED_ORDERS_FILE, archived_orders_list)
    save_data(ARTICLES_FILE, articles_list)
    save_data(MATERIALS_FILE, materials_list)
    save_data(RECEIVED_PRODUCTS_FILE, received_products_list)
    save_data(TOOLS_FILE, tools_list)
    save_data(INSTRUCTIONS_FILE, instructions_list)
    save_data(ANALYSIS_FILE, analysis_list)
    save_data(CLOSED_ANALYSIS_FILE, closed_analysis_list)

# Funkcja do wyświetlania zakładki pomoc
def show_help():
    clear_frame()
    help_text = """
    Program ERP do zarządzania produkcją, jakością, maszynami, narzędziami oraz magazynem.

    Zakładki główne:
    - Produkcja: Zarządzanie zleceniami produkcyjnymi, w tym dodawanie, edytowanie, usuwanie i archiwizacja zleceń.
    - Jakość: Zarządzanie artykułami i analizami jakości, w tym dodawanie artykułów, tworzenie i edytowanie analiz.
    - Maszyny: Zarządzanie listą maszyn, w tym dodawanie, edytowanie i usuwanie maszyn oraz przegląd artykułów przypisanych do maszyn.
    - Magazyn: Zarządzanie materiałami, częściami oraz wysyłkami, w tym dodawanie materiałów, przegląd stanu magazynu, szybkie dodawanie i wydawanie materiałów.
    - Narzędzia: Zarządzanie narzędziami, w tym dodawanie, przegląd, serwis, przeglądy, walidacje i naprawy narzędzi.
    - Instrukcje: Zarządzanie instrukcjami szkoleniowymi, w tym dodawanie i przegląd instrukcji.
    - Pomoc: Informacje na temat programu, zakładek i autorstwa.
    - Kalkulatory: Dodatkowe narzędzia kalkulacyjne.

    Autor: Krystian Staśkiewicz
    """
    label = tk.Label(content_frame, text=help_text, justify=tk.LEFT)
    label.pack(padx=10, pady=10)


# Funkcje zmieniające zawartość okna dla każdej zakładki
def show_production():
    clear_frame()

    # Utworzenie notebooka do dodania podzakładek
    notebook = ttk.Notebook(content_frame)
    notebook.pack(fill="both", expand=True)
    
    # Dodanie zakładki "Zlecenia"
    orders_frame = ttk.Frame(notebook)
    notebook.add(orders_frame, text="Zlecenia")

    # Dodanie zakładki "Lista Zleceń"
    orders_list_frame = ttk.Frame(notebook)
    notebook.add(orders_list_frame, text="Lista Zleceń")
    
    # Dodanie zakładki "Usunięte Zlecenia"
    deleted_orders_frame = ttk.Frame(notebook)
    notebook.add(deleted_orders_frame, text="Usunięte Zlecenia")
    
    # Dodanie zakładki "Zakończone Zlecenia"
    completed_orders_frame = ttk.Frame(notebook)
    notebook.add(completed_orders_frame, text="Zakończone Zlecenia")

    # Dodanie zakładki "Zlecenia Zarchiwizowane"
    archived_orders_frame = ttk.Frame(notebook)
    notebook.add(archived_orders_frame, text="Zlecenia Zarchiwizowane")
    
    # Utworzenie formularza do wprowadzania danych zleceń
    create_order_form(orders_frame)

    # Utworzenie tabeli do wyświetlania listy zleceń
    create_orders_table(orders_list_frame, "orders")

    # Utworzenie tabeli do wyświetlania usuniętych zleceń
    create_orders_table(deleted_orders_frame, "deleted")

    # Utworzenie tabeli do wyświetlania zakończonych zleceń
    create_orders_table(completed_orders_frame, "completed")

    # Utworzenie tabeli do wyświetlania zarchiwizowanych zleceń
    create_orders_table(archived_orders_frame, "archived")

def on_tool_number_selected(event, entries):
    selected_tool_number = entries["Numer Narzędzia"].get()
    for tool in tools_list:
        if tool[1] == selected_tool_number:
            entries["Nazwa Narzędzia"].set(tool[0])
            break

def show_material_calculator():
    clear_frame()
    app = ConversionApp(content_frame)

def create_order_form(frame):
    labels = ["Numer Zlecenia", "Numer Artykułu", "Nazwa Artykułu", "Materiał", "Stan Materiału", "Maszyna", "Numer Narzędzia",
              "Nazwa Narzędzia", "Instrukcja Pakowania", "Ilość", "Data Rozpoczęcia", "Data Zakończenia"]
    entries = {}

    def on_article_number_selected(event, entries):
        selected_article_number = entries["Numer Artykułu"].get()
        for article in articles_list:
            if article[0] == selected_article_number:
                entries["Nazwa Artykułu"].set(article[1])
                entries["Maszyna"].set(article[5])
                entries["Numer Narzędzia"].set(article[2])
                entries["Instrukcja Pakowania"].set(article[3])
                break

    def on_material_selected(event, entries):
        selected_material = entries["Materiał"].get()
        for material in materials_list:
            if material[0] == selected_material:
                entries["Stan Materiału"].set(material[3])
                break

    def on_tool_number_selected(event, entries):
        selected_tool_number = entries["Numer Narzędzia"].get()
        for tool in tools_list:
            if tool[1] == selected_tool_number:
                entries["Nazwa Narzędzia"].set(tool[0])
                break

    validate_cmd = frame.register(lambda P: validate_and_format_quantity(P, quantity_entry_var))

    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Numer Artykułu":
            entry = ttk.Combobox(frame, values=[article[0] for article in articles_list], state="readonly", width=23)
            entry.bind("<<ComboboxSelected>>", lambda event: on_article_number_selected(event, entries))
        elif label_text == "Materiał":
            entry = ttk.Combobox(frame, values=[material[0] for material in materials_list], state="readonly", width=23)
            entry.bind("<<ComboboxSelected>>", lambda event: on_material_selected(event, entries))
        elif label_text == "Nazwa Artykułu" or label_text == "Stan Materiału" or label_text == "Nazwa Narzędzia":
            entry = tk.StringVar()
            entry_widget = ttk.Combobox(frame, textvariable=entry, state="readonly", width=23)
            entry_widget.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        elif label_text == "Maszyna":
            entry = ttk.Combobox(frame, values=[m[1] for m in machines_list], state="readonly", width=23)
        elif label_text == "Numer Narzędzia":
            entry = ttk.Combobox(frame, values=[tool[1] for tool in tools_list], state="readonly", width=23)
            entry.bind("<<ComboboxSelected>>", lambda event: on_tool_number_selected(event, entries))
        elif label_text == "Instrukcja Pakowania":
            entry = ttk.Combobox(frame, values=[instruction["Nazwa instrukcji"] for instruction in instructions_list], state="readonly", width=23)
        elif label_text == "Ilość":
            quantity_entry_var = tk.StringVar()
            entry = tk.Entry(frame, width=25, textvariable=quantity_entry_var, validate="key", validatecommand=(validate_cmd, '%P'))
        elif "Data" in label_text:
            entry = DateEntry(frame, date_pattern='dd.mm.yyyy', width=20)
        else:
            entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do dodawania zlecenia
    add_button = tk.Button(frame, text="Dodaj Zlecenie", command=lambda: add_order(entries))
    add_button.grid(row=len(labels), columnspan=2, pady=10)




def format_number_with_spaces(number):
    number = number.replace(" ", " ")
    return " ".join([number[max(i-3, 0):i] for i in range(len(number), 0, -3)][::-1])

def validate_and_format_quantity(P, quantity_entry_var):
    if P.isdigit() or P == "":
        formatted_number = format_number_with_spaces(P)
        quantity_entry_var.set(formatted_number)
        return True
    else:
        return False


def create_orders_table(frame, table_type):
    if table_type == "deleted":
        columns = ("Numer Zlecenia", "Numer Artykułu", "Nazwa Artykułu", "Materiał", "Stan Materiału", "Maszyna", "Numer Narzędzia",
                   "Nazwa Narzędzia", "Instrukcja Pakowania", "Ilość", "Data Rozpoczęcia", "Data Zakończenia", "Powód usunięcia", "Data usunięcia")
    else:
        columns = ("Numer Zlecenia", "Numer Artykułu", "Nazwa Artykułu", "Materiał", "Stan Materiału", "Maszyna", "Numer Narzędzia",
                   "Nazwa Narzędzia", "Instrukcja Pakowania", "Ilość", "Data Rozpoczęcia", "Data Zakończenia", "Status")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)
    
    if table_type == "orders":
        global orders_tree
        orders_tree = tree
        orders_tree.bind("<Double-1>", on_double_click_order)
        # Załadowanie zapisanych zleceń
        for order in orders_list:
            add_order_to_tree(order, orders_tree)
    elif table_type == "deleted":
        global deleted_orders_tree
        deleted_orders_tree = tree
        deleted_orders_tree.bind("<Double-1>", on_double_click_deleted)
        # Załadowanie usuniętych zleceń
        for order in deleted_orders_list:
            add_order_to_tree(order, deleted_orders_tree)
    elif table_type == "completed":
        global completed_orders_tree
        completed_orders_tree = tree
        completed_orders_tree.bind("<Double-1>", on_double_click_completed)
        # Załadowanie zakończonych zleceń
        for order in completed_orders_list:
            add_order_to_tree(order, completed_orders_tree)
    elif table_type == "archived":
        global archived_orders_tree
        archived_orders_tree = tree
        archived_orders_tree.bind("<Double-1>", on_double_click_archived)
        # Załadowanie zarchiwizowanych zleceń
        for order in archived_orders_list:
            add_order_to_tree(order, archived_orders_tree)



def add_order(entries):
    values = [entry.get() if isinstance(entry, tk.Entry) else entry.get() for entry in entries.values()]
    values.append("Nieaktywne")  # Dodanie początkowego statusu
    add_order_to_tree(values, orders_tree)
    orders_list.append(values)
    save_data(ORDERS_FILE, orders_list)
    messagebox.showinfo("Sukces", "Zlecenie zostało dodane pomyślnie")


def add_order_to_tree(values, tree):
    tag = ""
    if values[-1] == "W trakcie":
        tag = "active"
    elif values[-1] == "Nieaktywne":
        tag = "inactive"
    elif values[-1] == "Przerwane":
        tag = "interrupted"
    elif values[-1] == "Zakończone":
        tag = "completed"
    elif values[-1] == "Gotowe":
        tag = "archived"
    
    tree.insert("", tk.END, values=values, tags=(tag,))
    update_tree_colors(tree)

def update_order_status(item, new_status, tree):
    values = list(tree.item(item, 'values'))
    values[-1] = new_status
    tree.item(item, values=values)
    for order in orders_list:
        if order[0] == values[0]:
            order[-1] = new_status
            break
    save_data(ORDERS_FILE, orders_list)
    update_tree_colors(tree)
    if new_status == "Zakończone":
        move_order_to_completed(values)
    elif new_status == "Przerwane":
        move_order_to_deleted(values)
    elif new_status == "Gotowe":
        move_order_to_archived(values)

def update_tree_colors(tree):
    for item in tree.get_children():
        status = tree.item(item, 'values')[-1]
        if status == "W trakcie":
            tree.item(item, tags=("active",))
        elif status == "Nieaktywne":
            tree.item(item, tags=("inactive",))
        elif status == "Przerwane":
            tree.item(item, tags=("interrupted",))
        elif status == "Zakończone":
            tree.item(item, tags=("completed",))
        elif status == "Gotowe":
            tree.item(item, tags=("archived",))

    tree.tag_configure("active", background="lightgreen")
    tree.tag_configure("inactive", background="lightyellow")
    tree.tag_configure("interrupted", background="lightcoral")
    tree.tag_configure("completed", background="lightseagreen")
    tree.tag_configure("archived", background="lightgoldenrod")

def move_order_to_completed(values):
    orders_list.remove(values)
    completed_orders_list.append(values)
    add_order_to_tree(values, completed_orders_tree)
    save_data(ORDERS_FILE, orders_list)
    save_data(COMPLETED_ORDERS_FILE, completed_orders_list)

def move_order_to_deleted(values):
    orders_list.remove(values)
    deleted_orders_list.append(values + [datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    add_order_to_tree(values + [datetime.now().strftime("%Y-%m-%d %H:%M:%S")], deleted_orders_tree)
    save_data(ORDERS_FILE, orders_list)
    save_data(DELETED_ORDERS_FILE, deleted_orders_list)

def move_order_to_archived(values):
    orders_list.remove(values)
    archived_orders_list.append(values)
    add_order_to_tree(values, archived_orders_tree)
    save_data(ORDERS_FILE, orders_list)
    save_data(ARCHIVED_ORDERS_FILE, archived_orders_list)

def on_double_click_order(event):
    item = orders_tree.selection()[0]
    popup_order_menu(item)

def on_double_click_deleted(event):
    item = deleted_orders_tree.selection()[0]
    popup_delete_menu(item)

def on_double_click_completed(event):
    item = completed_orders_tree.selection()[0]
    popup_completed_menu(item)

def on_double_click_archived(event):
    item = archived_orders_tree.selection()[0]
    popup_archive_menu(item)

def popup_order_menu(item):
    popup = tk.Toplevel()
    popup.title("Zarządzaj zleceniem")

    tk.Button(popup, text="Usuń zlecenie", command=lambda: delete_order(item, popup)).pack(fill="x")
    tk.Button(popup, text="Rozpocznij zlecenie", command=lambda: update_order_status(item, "W trakcie", orders_tree)).pack(fill="x")
    tk.Button(popup, text="Edytuj zlecenie", command=lambda: edit_order(item, popup)).pack(fill="x")
    tk.Button(popup, text="Zakończ zlecenie", command=lambda: update_order_status(item, "Zakończone", orders_tree)).pack(fill="x")
    tk.Button(popup, text="Przerwij zlecenie", command=lambda: update_order_status(item, "Przerwane", orders_tree)).pack(fill="x")
    tk.Button(popup, text="Archiwizuj zlecenie", command=lambda: update_order_status(item, "Gotowe", orders_tree)).pack(fill="x")
    tk.Button(popup, text="Usuń trwale", command=lambda: permanently_delete_order(item, popup)).pack(fill="x")

def popup_delete_menu(item):
    popup = tk.Toplevel()
    popup.title("Czy na pewno usunąć zlecenie?")
    popup.configure(bg="red")
    
    tk.Label(popup, text="Usuń zlecenie", bg="red", fg="white").pack(fill="x", pady=10)
    tk.Button(popup, text="Usuń", bg="red", command=lambda: permanently_delete_deleted_order(item, popup)).pack(fill="x", padx=5, pady=5)
    tk.Button(popup, text="Anuluj", bg="gray", command=popup.destroy).pack(fill="x", padx=5, pady=5)

def popup_completed_menu(item):
    popup = tk.Toplevel()
    popup.title("Czy na pewno usunąć zlecenie?")
    popup.configure(bg="red")
    
    tk.Label(popup, text="Usuń zlecenie", bg="red", fg="white").pack(fill="x", pady=10)
    tk.Button(popup, text="Usuń", bg="red", command=lambda: permanently_delete_completed_order(item, popup)).pack(fill="x", padx=5, pady=5)
    tk.Button(popup, text="Anuluj", bg="gray", command=popup.destroy).pack(fill="x", padx=5, pady=5)

def popup_archive_menu(item):
    popup = tk.Toplevel()
    popup.title("Czy na pewno usunąć zlecenie?")
    popup.configure(bg="red")
    
    tk.Label(popup, text="Usuń zlecenie", bg="red", fg="white").pack(fill="x", pady=10)
    tk.Button(popup, text="Usuń", bg="red", command=lambda: permanently_delete_archived_order(item, popup)).pack(fill="x", padx=5, pady=5)
    tk.Button(popup, text="Anuluj", bg="gray", command=popup.destroy).pack(fill="x", padx=5, pady=5)

def delete_order(item, popup):
    reason = simpledialog.askstring("Powód usunięcia", "Podaj powód usunięcia zlecenia:")
    if reason:
        values = list(orders_tree.item(item, 'values'))
        values[-1] = reason
        deleted_orders_list.append(values + [datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        add_order_to_tree(values + [datetime.now().strftime("%Y-%m-%d %H:%M:%S")], deleted_orders_tree)
        orders_list.remove(values[:-1])
        orders_tree.delete(item)
        save_data(ORDERS_FILE, orders_list)
        save_data(DELETED_ORDERS_FILE, deleted_orders_list)
        popup.destroy()

def permanently_delete_order(item, popup):
    confirm = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz trwale usunąć to zlecenie?")
    if confirm:
        values = list(orders_tree.item(item, 'values'))
        orders_list.remove(values)
        orders_tree.delete(item)
        save_data(ORDERS_FILE, orders_list)
        popup.destroy()

def permanently_delete_deleted_order(item, popup):
    confirm = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz trwale usunąć to zlecenie?")
    if confirm:
        values = list(deleted_orders_tree.item(item, 'values'))
        deleted_orders_list.remove(values)
        deleted_orders_tree.delete(item)
        save_data(DELETED_ORDERS_FILE, deleted_orders_list)
        popup.destroy()

def permanently_delete_completed_order(item, popup):
    confirm = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz trwale usunąć to zlecenie?")
    if confirm:
        values = list(completed_orders_tree.item(item, 'values'))
        completed_orders_list.remove(values)
        completed_orders_tree.delete(item)
        save_data(COMPLETED_ORDERS_FILE, completed_orders_list)
        popup.destroy()

def permanently_delete_archived_order(item, popup):
    confirm = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz trwale usunąć to zlecenie?")
    if confirm:
        values = list(archived_orders_tree.item(item, 'values'))
        archived_orders_list.remove(values)
        archived_orders_tree.delete(item)
        save_data(ARCHIVED_ORDERS_FILE, archived_orders_list)
        popup.destroy()

def edit_order(item, popup):
    values = list(orders_tree.item(item, 'values'))

    edit_popup = tk.Toplevel()
    edit_popup.title("Edytuj zlecenie")

    labels = ["Numer Zlecenia", "Numer Artykułu", "Nazwa Artykułu", "Materiał", "Maszyna", "Numer Narzędzia",
              "Nazwa Narzędzia", "Instrukcja Pakowania", "Ilość", "Data Rozpoczęcia", "Data Zakończenia"]

    entries = {}
    for i, label_text in enumerate(labels):
        label = tk.Label(edit_popup, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Maszyna":
            entry = ttk.Combobox(edit_popup, values=[m[1] for m in machines_list], state="readonly", width=23)
        elif "Data" in label_text:
            entry = DateEntry(edit_popup, date_pattern='dd.mm.yyyy', width=20)
        else:
            entry = tk.Entry(edit_popup, width=25)
        entry.insert(0, values[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    tk.Button(edit_popup, text="Zapisz", command=lambda: save_edited_order(item, entries, edit_popup)).grid(row=len(labels), columnspan=2, pady=10)
    popup.destroy()

def save_edited_order(item, entries, edit_popup):
    values = [entry.get() for entry in entries.values()]
    values.append(orders_tree.item(item, 'values')[-1])  # Zachowaj obecny status
    orders_tree.item(item, values=values)

    for order in orders_list:
        if order[0] == values[0]:
            order_index = orders_list.index(order)
            orders_list[order_index] = values
            break

    save_data(ORDERS_FILE, orders_list)
    edit_popup.destroy()
    update_tree_colors(orders_tree)

def show_quality():
    clear_frame()

    # Utworzenie notebooka do dodania podzakładek
    notebook = ttk.Notebook(content_frame)
    notebook.pack(fill="both", expand=True)

    # Dodanie zakładki "Dodaj artykuł"
    add_article_frame = ttk.Frame(notebook)
    notebook.add(add_article_frame, text="Dodaj artykuł")

    # Dodanie zakładki "Lista artykułów"
    articles_list_frame = ttk.Frame(notebook)
    notebook.add(articles_list_frame, text="Lista artykułów")

    # Dodanie zakładki "Analizy"
    analysis_frame = ttk.Frame(notebook)
    notebook.add(analysis_frame, text="Analizy")

    # Dodanie zakładki "Lista analiz"
    analysis_list_frame = ttk.Frame(notebook)
    notebook.add(analysis_list_frame, text="Lista analiz")

    # Dodanie zakładki "Analizy zamknięte"
    closed_analysis_frame = ttk.Frame(notebook)
    notebook.add(closed_analysis_frame, text="Analizy zamknięte")

    create_article_form(add_article_frame)
    create_articles_table(articles_list_frame)
    create_analysis_table(analysis_frame)
    create_analysis_list_table(analysis_list_frame)
    create_closed_analysis_table(closed_analysis_frame)

def create_article_form(frame):
    labels = ["Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Najczęstsze Problemy", "Maszyna"]
    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Maszyna":
            entry = ttk.Combobox(frame, values=[m[1] for m in machines_list], state="readonly", width=23)
        else:
            entry = tk.Entry(frame, width=50)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do dodawania artykułu
    add_button = tk.Button(frame, text="Dodaj Artykuł", command=lambda: add_article(entries))
    add_button.grid(row=len(labels), columnspan=2, pady=10)

def create_articles_table(frame):
    columns = ("Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Najczęstsze Problemy", "Maszyna")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(fill="both", expand=True)

    global articles_tree
    articles_tree = tree
    articles_tree.bind("<Double-1>", on_double_click_article)
    # Załadowanie zapisanych artykułów
    for article in articles_list:
        add_article_to_tree(article, articles_tree)

def create_analysis_table(frame):
    columns = ("Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Najczęstsze Problemy", "Maszyna", "Status")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(fill="both", expand=True)

    global analysis_tree
    analysis_tree = tree
    analysis_tree.bind("<Double-1>", on_double_click_analysis)
    # Załadowanie zapisanych analiz
    for analysis in analysis_list:
        add_analysis_to_table(analysis, analysis_tree)

def create_analysis_list_table(frame):
    columns = ("Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Najczęstsze Problemy", "Maszyna", "Status")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(fill="both", expand=True)

    global analysis_list_tree
    analysis_list_tree = tree
    analysis_list_tree.bind("<Double-1>", on_double_click_analysis)
    # Załadowanie zapisanych analiz
    for analysis in analysis_list:
        add_analysis_to_table(analysis, analysis_list_tree)

def create_closed_analysis_table(frame):
    columns = ("Numer Artykułu", "Nazwa Artykułu", "Maszyna", "Numer Narzędzia", "Nazwa narzędzia", "Data stworzenia analizy", "Data zamknięcia analizy", "Opis problemu", "Osoby")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(fill="both", expand=True)

    global closed_analysis_tree
    closed_analysis_tree = tree
    # Załadowanie zapisanych zamkniętych analiz
    for analysis in closed_analysis_list:
        add_closed_analysis_to_tree(analysis, closed_analysis_tree)

def add_article(entries):
    values = [entry.get() for entry in entries.values()]
    add_article_to_tree(values, articles_tree)
    articles_list.append(values)
    save_data(ARTICLES_FILE, articles_list)

def add_article_to_tree(values, tree):
    tree.insert("", tk.END, values=values)

def on_double_click_article(event):
    item = articles_tree.selection()[0]
    article_num = articles_tree.item(item, 'values')[0]
    create_analysis_form(article_num)

def create_analysis_form(article_num):
    analysis_popup = tk.Toplevel()
    analysis_popup.title("Analiza problemu")

    labels = ["Numer Zlecenia", "Analiza problemu", "Kto tworzył analizę", "Słowo kluczowe", "Status"]
    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(analysis_popup, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Numer Zlecenia":
            entry = ttk.Combobox(analysis_popup, values=[order[0] for order in orders_list], state="readonly", width=23)
        elif label_text == "Analiza problemu":
            entry = tk.Text(analysis_popup, width=50, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        elif label_text == "Status":
            entry = ttk.Combobox(analysis_popup, values=["Otwarta", "Zamknięta"], state="readonly", width=23)
            entry.set("Otwarta")
        else:
            entry = tk.Entry(analysis_popup, width=50)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    save_button = tk.Button(analysis_popup, text="Zapisz", command=lambda: save_analysis(article_num, entries, analysis_popup))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_analysis(article_num, entries, popup):
    values = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    values["Numer Artykułu"] = article_num
    values["Data Stworzenia"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    analysis_list.append(values)
    add_analysis_to_table(values, analysis_tree)
    save_data(ANALYSIS_FILE, analysis_list)
    popup.destroy()

def add_analysis_to_table(values, tree):
    tree.insert("", tk.END, values=(values.get("Numer Artykułu"), values.get("Nazwa Artykułu"), values.get("Numer Narzędzia"), values.get("Instrukcja Pakowania"), values.get("Najczęstsze Problemy"), values.get("Maszyna"), values.get("Status")))

def on_double_click_analysis(event):
    item = analysis_tree.selection()[0]
    analysis = analysis_tree.item(item, 'values')
    show_analysis_parameters_form(analysis)

def show_analysis_parameters_form(analysis):
    popup = tk.Toplevel()
    popup.title(f"Analiza: {analysis[0]}")

    labels = ["Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Najczęstsze Problemy", "Maszyna", "Status"]
    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(popup, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Status":
            entry = ttk.Combobox(popup, values=["Otwarta", "Zamknięta"], state="readonly", width=25)
            entry.set(analysis[6])
        else:
            entry = tk.Entry(popup, width=50)
            entry.insert(0, analysis[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    save_button = tk.Button(popup, text="Zapisz", command=lambda: save_analysis_parameters(entries, popup, analysis))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_analysis_parameters(entries, popup, analysis):
    values = {label: entry.get() for label, entry in entries.items()}
    for existing_analysis in analysis_list:
        if existing_analysis["Numer Artykułu"] == values["Numer Artykułu"]:
            existing_analysis.update(values)
            if values["Status"] == "Zamknięta":
                existing_analysis["Data Zamknięcia"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                closed_analysis_list.append(existing_analysis)
                analysis_list.remove(existing_analysis)
                add_closed_analysis_to_tree(existing_analysis, closed_analysis_tree)
                save_data(CLOSED_ANALYSIS_FILE, closed_analysis_list)
            break
    save_data(ANALYSIS_FILE, analysis_list)
    update_analysis_table()
    popup.destroy()

def add_closed_analysis_to_tree(values, tree):
    tree.insert("", tk.END, values=(values.get("Numer Artykułu"), values.get("Nazwa Artykułu"), values.get("Maszyna"), values.get("Numer Narzędzia"), values.get("Nazwa narzędzia"), values.get("Data Stworzenia"), values.get("Data Zamknięcia"), values.get("Opis problemu"), values.get("Osoby")))

def update_analysis_table():
    for item in analysis_tree.get_children():
        analysis_tree.delete(item)
    for analysis in analysis_list:
        add_analysis_to_table(analysis, analysis_tree)

def show_machines():
    clear_frame()
    
    columns = ("ID", "Nazwa", "Zlecenie")
    tree = ttk.Treeview(content_frame, columns=columns, show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nazwa", text="Nazwa")
    tree.heading("Zlecenie", text="Zlecenie")
    
    tree.column("ID", width=50, anchor='center')
    tree.column("Nazwa", width=200, anchor='w')
    tree.column("Zlecenie", width=100, anchor='center')
    
    # Dodanie maszyn do tabeli
    global machines_list
    for machine in machines_list:
        tree.insert("", tk.END, values=machine)
    
    tree.pack(fill="both", expand=True)

    tree.bind("<Double-1>", on_double_click_machine)
    
    # Dodanie przycisków do edycji tabeli
    add_button = tk.Button(content_frame, text="Dodaj", command=lambda: add_machine(tree))
    add_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    edit_button = tk.Button(content_frame, text="Edytuj", command=lambda: edit_machine(tree))
    edit_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    delete_button = tk.Button(content_frame, text="Usuń", command=lambda: delete_machine(tree))
    delete_button.pack(side=tk.LEFT, padx=5, pady=5)

def on_double_click_machine(event):
    item = event.widget.selection()[0]
    machine_name = event.widget.item(item, 'values')[1]
    show_machine_articles(machine_name)

def show_machine_articles(machine_name):
    popup = tk.Toplevel()
    popup.title(f"Artykuły dla maszyny: {machine_name}")

    columns = ("Numer Artykułu", "Nazwa Artykułu", "Numer Narzędzia", "Instrukcja Pakowania", "Maszyna")
    tree = ttk.Treeview(popup, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(fill="both", expand=True)

    articles = [article for article in articles_list if article[5] == machine_name]
    for article in articles:
        tree.insert("", tk.END, values=article)

    tree.bind("<Double-1>", on_double_click_machine_article)

def on_double_click_machine_article(event):
    item = event.widget.selection()[0]
    article = event.widget.item(item, 'values')
    show_article_parameters_form(article)

def show_article_parameters_form(article):
    popup = tk.Toplevel()
    popup.title(f"Karta parametrów dla: {article[1]}")

    labels = ["Maszyna", "Numer narzędzia", "Numer artykułu", "Nazwa artykułu", "Numer materiału", "Rozmiar materiału", "Rodzaj złomu",
              "Ramiona haspla (1)", "Ramiona haspla (2)", "Ramiona haspla (3)", "Ustawienia walców prostujących (1)", "Ustawienia walców prostujących (2)", 
              "Ustawienia walców prostujących (3)", "Ustawienia walców prostujących (4)", "Ustawienia walców prostujących (5)", 
              "Ustawienia fazowników (1)", "Ustawienia fazowników (2)", "Ustawienia fazowników (3)", "Ustawienia fazowników (4)", 
              "Ustawienia fazowników (5)", "Wprowadzanie", "Smarowanie", "Cykle podawania oleju (Ilość cykli)", "Cykle podawania oleju (Ilość oleju ms)",
              "Podajnik materiału", "Ciśnienie podajnika materiału", "Długość posuwu", "Długość platyny", "Wysokość prasy", "Pozycja narzędzia",
              "Długość wprowadzania", "Prędkość prasy szt/min", "Walce podajnika", "Długość wypychaczy", "Wejśćie materiału do gięcia", 
              "Adapter stempli", "Płyta adaptera", "Wysokość prowadnicy", "Uwagi"]

    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(popup, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text in ["Wprowadzanie", "Wejśćie materiału do gięcia"]:
            entry = ttk.Combobox(popup, values=["Góra", "Dół"], state="readonly", width=23)
        elif label_text == "Smarowanie":
            entry = ttk.Combobox(popup, values=["RENOFORM UBO 377/13", "Inne"], state="readonly", width=23)
        elif label_text == "Uwagi":
            entry = tk.Text(popup, width=50, height=5, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(popup, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    save_button = tk.Button(popup, text="Zapisz", command=lambda: save_article_parameters(entries, popup))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_article_parameters(entries, popup):
    values = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    # Save values logic here
    messagebox.showinfo("Sukces", "Parametry zostały zapisane pomyślnie")
    popup.destroy()

def add_machine(tree):
    new_id = simpledialog.askstring("Input", "Podaj ID maszyny:")
    new_name = simpledialog.askstring("Input", "Podaj nazwę maszyny:")
    if new_id and new_name:
        machine = (new_id, new_name, "")
        tree.insert("", tk.END, values=machine)
        machines_list.append(machine)
        save_data(MACHINES_FILE, machines_list)
        update_machine_comboboxes()

def edit_machine(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Brak wyboru", "Proszę wybrać maszynę do edycji")
        return
    
    item = selected_item[0]
    current_id, current_name, current_order = tree.item(item, 'values')
    
    new_name = simpledialog.askstring("Input", "Podaj nową nazwę maszyny:", initialvalue=current_name)
    if new_name:
        tree.item(item, values=(current_id, new_name, current_order))
        for machine in machines_list:
            if machine[0] == current_id:
                machine_index = machines_list.index(machine)
                machines_list[machine_index] = (current_id, new_name, current_order)
                break
        save_data(MACHINES_FILE, machines_list)
        update_machine_comboboxes()

def delete_machine(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Brak wyboru", "Proszę wybrać maszynę do usunięcia")
        return
    
    confirm = messagebox.askyesno("Confirm", "Czy na pewno chcesz usunąć tę maszynę?")
    if confirm:
        item = selected_item[0]
        current_id = tree.item(item, 'values')[0]
        tree.delete(item)
        global machines_list
        machines_list = [m for m in machines_list if m[0] != current_id]
        save_data(MACHINES_FILE, machines_list)
        update_machine_comboboxes()

def update_machine_comboboxes():
    # Aktualizacja wartości w comboboxach w formularzu zleceń
    if content_frame.winfo_children():
        orders_frame = content_frame.winfo_children()[0]
        if isinstance(orders_frame, ttk.Notebook):
            for tab in orders_frame.winfo_children():
                for widget in tab.winfo_children():
                    if isinstance(widget, ttk.Combobox) and widget.cget("state") == "readonly":
                        widget['values'] = [m[1] for m in machines_list]

def show_tools():
    clear_frame()

    # Utworzenie notebooka do dodania podzakładek
    notebook = ttk.Notebook(content_frame)
    notebook.pack(fill="both", expand=True)
    
    # Dodanie zakładki "Dodaj narzędzie"
    add_tool_frame = ttk.Frame(notebook)
    notebook.add(add_tool_frame, text="Dodaj narzędzie")
    
    # Dodanie zakładki "Lista narzędzi"
    tools_list_frame = ttk.Frame(notebook)
    notebook.add(tools_list_frame, text="Lista narzędzi")

    # Dodanie zakładki "Serwisy narzędzi"
    services_frame = ttk.Frame(notebook)
    notebook.add(services_frame, text="Serwisy narzędzi")

    # Dodanie zakładki "Przeglądy narzędzi"
    reviews_frame = ttk.Frame(notebook)
    notebook.add(reviews_frame, text="Przeglądy narzędzi")

    # Dodanie zakładki "Walidacje narzędzi"
    validations_frame = ttk.Frame(notebook)
    notebook.add(validations_frame, text="Walidacje narzędzi")

    # Dodanie zakładki "Naprawy narzędzi"
    repairs_frame = ttk.Frame(notebook)
    notebook.add(repairs_frame, text="Naprawy narzędzi")
    
    create_tool_form(add_tool_frame)
    create_tools_table(tools_list_frame)
    create_services_table(services_frame)
    create_reviews_table(reviews_frame)
    create_validations_table(validations_frame)
    create_repairs_table(repairs_frame)

def create_tool_form(frame):
    labels = ["Nazwa narzędzia", "Numer narzędzia"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do dodawania narzędzia
    add_button = tk.Button(frame, text="Dodaj Narzędzie", command=lambda: add_tool(entries))
    add_button.grid(row=len(labels), columnspan=2, pady=10)

def add_tool(entries):
    values = [entry.get() for entry in entries.values()]
    tools_list.append(values)
    add_tool_to_tree(values, tools_tree)
    save_data(TOOLS_FILE, tools_list)
    messagebox.showinfo("Sukces", "Narzędzie zostało dodane pomyślnie")

def create_tools_table(frame):
    columns = ("Nazwa narzędzia", "Numer narzędzia")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)

    global tools_tree
    tools_tree = tree
    tools_tree.bind("<Double-1>", on_double_click_tool)
    # Załadowanie zapisanych narzędzi
    for tool in tools_list:
        add_tool_to_tree(tool, tools_tree)

def add_tool_to_tree(values, tree):
    tree.insert("", tk.END, values=values)

def on_double_click_tool(event):
    item = tools_tree.selection()[0]
    popup_tool_menu(item)

def create_services_table(frame):
    columns = ("Nazwa narzędzia", "Numer narzędzia", "Data serwisu", "Opis serwisu", "Data kolejnego serwisu")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)
    
    global services_tree
    services_tree = tree

def create_reviews_table(frame):
    columns = ("Nazwa narzędzia", "Numer narzędzia", "Data przeglądu", "Opis przeglądu", "Data kolejnego przeglądu")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)
    
    global reviews_tree
    reviews_tree = tree

def create_validations_table(frame):
    columns = ("Nazwa narzędzia", "Numer narzędzia", "Data walidacji", "Opis walidacji")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)
    
    global validations_tree
    validations_tree = tree

def create_repairs_table(frame):
    columns = ("Nazwa narzędzia", "Numer narzędzia", "Data naprawy", "Opis naprawy")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)
    
    global repairs_tree
    repairs_tree = tree

def popup_tool_menu(item):
    popup = tk.Toplevel()
    popup.title("Zarządzaj narzędziem")

    tk.Button(popup, text="Serwis narzędzia", command=lambda: service_tool(item, popup)).pack(fill="x")
    tk.Button(popup, text="Przegląd narzędzia", command=lambda: review_tool(item, popup)).pack(fill="x")
    tk.Button(popup, text="Walidacja narzędzia", command=lambda: validate_tool(item, popup)).pack(fill="x")
    tk.Button(popup, text="Naprawa narzędzia", command=lambda: repair_tool(item, popup)).pack(fill="x")

def service_tool(item, popup):
    tool_data = tools_tree.item(item, 'values')
    popup.destroy()
    service_tool_window(tool_data)

def service_tool_window(tool_data):
    window = tk.Toplevel()
    window.title("Serwis narzędzia")
    
    labels = ["Nazwa narzędzia", "Numer narzędzia", "Data serwisu", "Opis serwisu", "Data kolejnego serwisu"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Data serwisu" or label_text == "Data kolejnego serwisu":
            entry = DateEntry(window, date_pattern='dd.mm.yyyy', width=20)
        elif label_text == "Opis serwisu":
            entry = tk.Text(window, width=40, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(window, width=25)
            entry.insert(0, tool_data[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry
    
    save_button = tk.Button(window, text="Zapisz", command=lambda: save_service_data(tool_data, entries, window))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_service_data(tool_data, entries, window):
    updated_tool_data = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    service_entry = (
        updated_tool_data["Nazwa narzędzia"],
        updated_tool_data["Numer narzędzia"],
        updated_tool_data["Data serwisu"],
        updated_tool_data["Opis serwisu"],
        updated_tool_data["Data kolejnego serwisu"]
    )
    services_tree.insert("", tk.END, values=service_entry)
    save_data(TOOLS_FILE, tools_list)
    messagebox.showinfo("Sukces", "Dane serwisowe zostały zapisane pomyślnie")
    window.destroy()

def review_tool(item, popup):
    tool_data = tools_tree.item(item, 'values')
    popup.destroy()
    review_tool_window(tool_data)

def review_tool_window(tool_data):
    window = tk.Toplevel()
    window.title("Przegląd narzędzia")
    
    labels = ["Nazwa narzędzia", "Numer narzędzia", "Data przeglądu", "Opis przeglądu", "Data kolejnego przeglądu"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Data przeglądu" or label_text == "Data kolejnego przeglądu":
            entry = DateEntry(window, date_pattern='dd.mm.yyyy', width=20)
        elif label_text == "Opis przeglądu":
            entry = tk.Text(window, width=40, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(window, width=25)
            entry.insert(0, tool_data[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry
    
    save_button = tk.Button(window, text="Zapisz", command=lambda: save_review_data(tool_data, entries, window))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_review_data(tool_data, entries, window):
    updated_tool_data = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    review_entry = (
        updated_tool_data["Nazwa narzędzia"],
        updated_tool_data["Numer narzędzia"],
        updated_tool_data["Data przeglądu"],
        updated_tool_data["Opis przeglądu"],
        updated_tool_data["Data kolejnego przeglądu"]
    )
    reviews_tree.insert("", tk.END, values=review_entry)
    save_data(TOOLS_FILE, tools_list)
    messagebox.showinfo("Sukces", "Dane przeglądu zostały zapisane pomyślnie")
    window.destroy()

def validate_tool(item, popup):
    tool_data = tools_tree.item(item, 'values')
    popup.destroy()
    validate_tool_window(tool_data)

def validate_tool_window(tool_data):
    window = tk.Toplevel()
    window.title("Walidacja narzędzia")
    window.state('zoomed')  # Zmaksymalizowanie okna

    # Lista narzędzi po lewej stronie
    list_frame = tk.Frame(window)
    list_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    columns = ("Nazwa narzędzia", "Numer narzędzia")
    tools_listbox = ttk.Treeview(list_frame, columns=columns, show='headings')
    for col in columns:
        tools_listbox.heading(col, text=col)
        tools_listbox.column(col, anchor='center')
    tools_listbox.pack(fill=tk.BOTH, expand=True)

    for tool in tools_list:
        tools_listbox.insert("", tk.END, values=tool)

    # Formularz walidacji po prawej stronie
    form_frame = tk.Frame(window)
    form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    labels = ["Nazwa narzędzia", "Numer narzędzia", "Data walidacji", "Opis walidacji"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(form_frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Data walidacji":
            entry = DateEntry(form_frame, date_pattern='dd.mm.yyyy', width=20)
        elif label_text == "Opis walidacji":
            entry = tk.Text(form_frame, width=40, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(form_frame, width=25)
            entry.insert(0, tool_data[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry
    
    save_button = tk.Button(form_frame, text="Zapisz", command=lambda: save_validate_data(tool_data, entries, window))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_validate_data(tool_data, entries, window):
    updated_tool_data = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    validate_entry = (
        updated_tool_data["Nazwa narzędzia"],
        updated_tool_data["Numer narzędzia"],
        updated_tool_data["Data walidacji"],
        updated_tool_data["Opis walidacji"]
    )
    validations_tree.insert("", tk.END, values=validate_entry)
    save_data(TOOLS_FILE, tools_list)
    messagebox.showinfo("Sukces", "Dane walidacji zostały zapisane pomyślnie")
    window.destroy()

def repair_tool(item, popup):
    tool_data = tools_tree.item(item, 'values')
    popup.destroy()
    repair_tool_window(tool_data)

def repair_tool_window(tool_data):
    window = tk.Toplevel()
    window.title("Naprawa narzędzia")
    
    labels = ["Nazwa narzędzia", "Numer narzędzia", "Data naprawy", "Opis naprawy"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Data naprawy":
            entry = DateEntry(window, date_pattern='dd.mm.yyyy', width=20)
        elif label_text == "Opis naprawy":
            entry = tk.Text(window, width=40, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(window, width=25)
            entry.insert(0, tool_data[i])
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry
    
    save_button = tk.Button(window, text="Zapisz", command=lambda: save_repair_data(tool_data, entries, window))
    save_button.grid(row=len(labels), columnspan=2, pady=10)

def save_repair_data(tool_data, entries, window):
    updated_tool_data = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    repair_entry = (
        updated_tool_data["Nazwa narzędzia"],
        updated_tool_data["Numer narzędzia"],
        updated_tool_data["Data naprawy"],
        updated_tool_data["Opis naprawy"]
    )
    repairs_tree.insert("", tk.END, values=repair_entry)
    save_data(TOOLS_FILE, tools_list)
    messagebox.showinfo("Sukces", "Dane naprawy zostały zapisane pomyślnie")
    window.destroy()

def show_instructions():
    clear_frame()

    # Utworzenie notebooka do dodania podzakładek
    notebook = ttk.Notebook(content_frame)
    notebook.pack(fill="both", expand=True)

    # Dodanie zakładki "Dodaj instrukcję"
    add_instruction_frame = ttk.Frame(notebook)
    notebook.add(add_instruction_frame, text="Dodaj instrukcję")

    # Dodanie zakładki "Lista instrukcji"
    list_instruction_frame = ttk.Frame(notebook)
    notebook.add(list_instruction_frame, text="Lista instrukcji")

    create_instruction_form(add_instruction_frame)
    create_instructions_list(list_instruction_frame)

def create_instruction_form(frame):
    labels = ["Numer instrukcji", "Nazwa instrukcji", "Maszyna/maszyny", "Czas szkolenia", "Opis szkolenia", "Słowo kluczowe"]
    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Maszyna/maszyny":
            entry = ttk.Combobox(frame, values=[m[1] for m in machines_list], state="readonly", width=23)
        elif label_text == "Czas szkolenia":
            entry = ttk.Combobox(frame, values=[f"{i} minut" for i in range(5, 125, 5)], state="readonly", width=23)
        elif label_text == "Opis szkolenia":
            entry = tk.Text(frame, width=50, height=10, wrap=tk.WORD)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            entries[label_text] = entry
            continue
        else:
            entry = tk.Entry(frame, width=50)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do dodawania instrukcji
    add_button = tk.Button(frame, text="Dodaj Instrukcję", command=lambda: add_instruction(entries))
    add_button.grid(row=len(labels), columnspan=2, pady=10)

def add_instruction(entries):
    values = {label: entry.get("1.0", tk.END).strip() if isinstance(entry, tk.Text) else entry.get() for label, entry in entries.items()}
    instructions_list.append(values)
    save_data(INSTRUCTIONS_FILE, instructions_list)
    messagebox.showinfo("Sukces", "Instrukcja została dodana pomyślnie")

def create_instructions_list(frame):
    columns = ("Numer instrukcji", "Słowo kluczowe")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(side=tk.LEFT, fill="both", expand=True)

    global instructions_tree
    instructions_tree = tree
    instructions_tree.bind("<Double-1>", on_double_click_instruction)
    # Załadowanie zapisanych instrukcji
    for instruction in instructions_list:
        instructions_tree.insert("", tk.END, values=(instruction["Numer instrukcji"], instruction["Słowo kluczowe"]))

    # Okno podglądu instrukcji
    instruction_view = tk.Text(frame, width=50, height=20, wrap=tk.WORD)
    instruction_view.pack(side=tk.RIGHT, fill="both", expand=True)

    global instruction_view_widget
    instruction_view_widget = instruction_view

def on_double_click_instruction(event):
    item = instructions_tree.selection()[0]
    instruction_num = instructions_tree.item(item, 'values')[0]

    for instruction in instructions_list:
        if instruction["Numer instrukcji"] == instruction_num:
            instruction_text = f"Numer instrukcji: {instruction['Numer instrukcji']}\nNazwa instrukcji: {instruction['Nazwa instrukcji']}\nMaszyna/maszyny: {instruction['Maszyna/maszyny']}\nCzas szkolenia: {instruction['Czas szkolenia']}\nOpis szkolenia:\n{instruction['Opis szkolenia']}\nSłowo kluczowe: {instruction['Słowo kluczowe']}"
            instruction_view_widget.delete(1.0, tk.END)
            instruction_view_widget.insert(tk.END, instruction_text)
            break

def create_material_form(frame):
    labels = ["Nazwa materiału", "Grubość materiału (mm)", "Szerokość materiału (mm)", "Ilość w kg", "Odpad"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Odpad":
            entry = ttk.Combobox(frame, values=["Złom stalowy", "Złom mangan", "Złom ocynk", "Złom kwasowy", "Inny"], state="readonly", width=23)
        else:
            entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do dodawania materiału
    add_button = tk.Button(frame, text="Dodaj Materiał", command=lambda: add_material(entries))
    add_button.grid(row=len(labels), columnspan=2, pady=10)

def create_stock_status_table(frame):
    columns = ("Nazwa materiału", "Grubość materiału (mm)", "Szerokość materiału (mm)", "Ilość w kg", "Odpad")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    tree.pack(fill="both", expand=True)

    global stock_status_tree
    stock_status_tree = tree

    # Załadowanie zapisanych materiałów
    for material in materials_list:
        add_material_to_tree(material, stock_status_tree)

def create_quick_add_form(frame):
    labels = ["Nazwa materiału", "Ilość w kg"]
    entries = {}
    
    for i, label_text in enumerate(labels):  # Pętla tworząca etykiety i pola w formularzu
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Nazwa materiału":
            # Dodanie pola rozwijanego z nazwami materiałów
            entry = ttk.Combobox(frame, values=[m[0] for m in materials_list], state="readonly", width=23)
        else:
            entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do szybkiego dodawania materiału
    quick_add_button = tk.Button(frame, text="Dodaj Materiał", command=lambda: quick_add_material(entries))
    quick_add_button.grid(row=len(labels), columnspan=2, pady=10)

def create_issue_material_form(frame):
    labels = ["Nazwa materiału", "Ilość w kg"]
    entries = {}
    
    for i, label_text in enumerate(labels):  # Pętla tworząca etykiety i pola w formularzu
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do wydawania materiału
    issue_button = tk.Button(frame, text="Wydaj Materiał", command=lambda: issue_material(entries))
    issue_button.grid(row=len(labels), columnspan=2, pady=10)

def on_order_number_selected(event, entries):
    selected_order_number = entries["Numer Zlecenia"].get()
    for order in orders_list:
        if order[0] == selected_order_number:
            entries["Maszyna"].set(order[5])
            break

def on_machine_selected(event, entries):
    selected_machine = entries["Maszyna"].get()
    for order in orders_list:
        if order[5] == selected_machine:
            entries["Numer Zlecenia"].set(order[0])
            break

def create_receive_product_form(frame):
    labels = ["Numer Zlecenia", "Maszyna", "Numer pojemnika", "Data wysyłki"]
    entries = {}
    
    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=('Helvetica', 10))
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        if label_text == "Numer Zlecenia":
            entry = ttk.Combobox(frame, values=[order[0] for order in orders_list], state="readonly", width=23)
            entry.bind("<<ComboboxSelected>>", lambda event: on_order_number_selected(event, entries))
        elif label_text == "Maszyna":
            entry = ttk.Combobox(frame, values=[m[1] for m in machines_list], state="readonly", width=23)
            entry.bind("<<ComboboxSelected>>", lambda event: on_machine_selected(event, entries))
        elif label_text == "Data wysyłki":
            entry = DateEntry(frame, date_pattern='dd.mm.yyyy', width=20)
        elif label_text == "Numer pojemnika":
            entry = tk.Entry(frame, width=25)
            entry.insert(0, generate_container_number())
            entry.config(state="readonly")
        else:
            entry = tk.Entry(frame, width=25)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
        entries[label_text] = entry

    # Przycisk do przyjmowania wyrobu
    receive_button = tk.Button(frame, text="Przyjmij Wyrób", command=lambda: receive_product(entries))
    receive_button.grid(row=len(labels), columnspan=2, pady=10)

def generate_container_number():
    # Funkcja generująca unikalny numer pojemnika
    return f"CN{len(received_products_list) + 1:04d}"

def receive_product(entries):
    values = {label: entry.get() for label, entry in entries.items()}
    received_products_list.append(values)
    save_data(RECEIVED_PRODUCTS_FILE, received_products_list)
    messagebox.showinfo("Sukces", "Wyrób został przyjęty pomyślnie")

def add_material(entries):
    values = [entry.get() for entry in entries.values()]
    materials_list.append(values)
    add_material_to_tree(values, stock_status_tree)
    save_data(MATERIALS_FILE, materials_list)
    messagebox.showinfo("Sukces", "Materiał został dodany pomyślnie")

def quick_add_material(entries):
    material_name = entries["Nazwa materiału"].get()
    amount = entries["Ilość w kg"].get()
    
    if material_name and amount:
        for material in materials_list:
            if material[0] == material_name:
                material[3] = str(int(material[3]) + int(amount))
                break
        save_data(MATERIALS_FILE, materials_list)
        update_stock_status_table()
        messagebox.showinfo("Sukces", "Materiał został dodany pomyślnie")
    else:
        messagebox.showwarning("Błąd", "Proszę uzupełnić wszystkie pola")

def issue_material(entries):
    material_name = entries["Nazwa materiału"].get()
    amount = entries["Ilość w kg"].get()
    
    if material_name and amount:
        for material in materials_list:
            if material[0] == material_name:
                if int(material[3]) >= int(amount):
                    material[3] = str(int(material[3]) - int(amount))
                    break
                else:
                    messagebox.showwarning("Błąd", "Niewystarczająca ilość materiału")
                    return
        save_data(MATERIALS_FILE, materials_list)
        update_stock_status_table()
        messagebox.showinfo("Sukces", "Materiał został wydany pomyślnie")
    else:
        messagebox.showwarning("Błąd", "Proszę uzupełnić wszystkie pola")

def add_material_to_tree(values, tree):
    tree.insert("", tk.END, values=values)

def update_stock_status_table():
    for item in stock_status_tree.get_children():
        stock_status_tree.delete(item)
    
    for material in materials_list:
        add_material_to_tree(material, stock_status_tree)

def create_parts_warehouse(frame):
    # Dodanie zawartości do zakładki "Magazyn części"
    label = tk.Label(frame, text="Magazyn części - zawartość do dodania", font=('Helvetica', 10))
    label.pack()

def create_shipping_warehouse(frame):
    # Dodanie zawartości do zakładki "Magazyn wysyłka"
    label = tk.Label(frame, text="Magazyn wysyłka - zawartość do dodania", font=('Helvetica', 10))
    label.pack()

def show_warehouse():
    clear_frame()

    # Utworzenie notebooka do dodania podzakładek
    notebook = ttk.Notebook(content_frame)
    notebook.pack(fill="both", expand=True)
    
    # Dodanie zakładki "Dodaj materiał"
    add_material_frame = ttk.Frame(notebook)
    notebook.add(add_material_frame, text="Dodaj materiał")

    # Dodanie zakładki "Stan magazynu"
    stock_status_frame = ttk.Frame(notebook)
    notebook.add(stock_status_frame, text="Stan magazynu")
    
    # Dodanie zakładki "Szybkie dodawanie materiału"
    quick_add_frame = ttk.Frame(notebook)
    notebook.add(quick_add_frame, text="Szybkie dodawanie materiału")

    # Dodanie zakładki "Wydawanie materiału"
    issue_material_frame = ttk.Frame(notebook)
    notebook.add(issue_material_frame, text="Wydawanie materiału")

    # Dodanie zakładki "Magazyn części"
    parts_warehouse_frame = ttk.Frame(notebook)
    notebook.add(parts_warehouse_frame, text="Magazyn części")

    # Dodanie zakładki "Magazyn wysyłka"
    shipping_warehouse_frame = ttk.Frame(notebook)
    notebook.add(shipping_warehouse_frame, text="Magazyn wysyłka")

    # Dodanie zakładki "Magazyn przyjęcie wyrobu"
    receive_product_frame = ttk.Frame(notebook)
    notebook.add(receive_product_frame, text="Magazyn przyjęcie wyrobu")

    create_material_form(add_material_frame)
    create_stock_status_table(stock_status_frame)
    create_quick_add_form(quick_add_frame)
    create_issue_material_form(issue_material_frame)
    create_parts_warehouse(parts_warehouse_frame)
    create_shipping_warehouse(shipping_warehouse_frame)
    create_receive_product_form(receive_product_frame)

def update_status_bar():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_orders = len(orders_list)
    status_text.set(f"Liczba aktualnych zleceń: {num_orders} | Aktualny czas: {current_time} | Autor: Krystian Staśkiewicz")
    status_bar.after(1000, update_status_bar)

# Funkcja czyszcząca zawartość ramki
def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

# Główne okno aplikacji
root = tk.Tk()
root.title("System ERP")
root.state('zoomed')  # Zmaksymalizowanie okna przy uruchomieniu

# Dodanie okna powitalnego
welcome_popup = tk.Toplevel(root)
welcome_popup.title("Informacja")
tk.Label(welcome_popup, text="Uruchomiono program ERP\nAutor: Krystian Staśkiewicz", font=('Helvetica', 16)).pack(padx=20, pady=20)
root.after(8000, welcome_popup.destroy)

# Pasek menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Dodanie zakładek do paska menu
production_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Produkcja", menu=production_menu)
production_menu.add_command(label="Pokaż", command=show_production)

quality_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Jakość", menu=quality_menu)
quality_menu.add_command(label="Pokaż", command=show_quality)

machines_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Maszyny", menu=machines_menu)
machines_menu.add_command(label="Pokaż", command=show_machines)

warehouse_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Magazyn", menu=warehouse_menu)
warehouse_menu.add_command(label="Pokaż", command=show_warehouse)

tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Narzędzia", menu=tools_menu)
tools_menu.add_command(label="Pokaż", command=show_tools)

instructions_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Instrukcje", menu=instructions_menu)
instructions_menu.add_command(label="Pokaż", command=show_instructions)

# Dodanie zakładki "Pomoc" do paska menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Pomoc", menu=help_menu)
help_menu.add_command(label="Pokaż", command=show_help)

# Dodanie zakładki "Kalkulatory" do paska menu
calculator_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Kalkulatory", menu=calculator_menu)
calculator_menu.add_command(label="Kalkulator materiału", command=show_material_calculator)
for i in range(2, 16):
    calculator_menu.add_command(label=f"Przycisk {i}")


# Ramka do zawartości zakładek
content_frame = ttk.Frame(root)
content_frame.pack(fill="both", expand=True)

# Pasek statusu
status_text = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_text, relief=tk.SUNKEN, anchor='w')
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Funkcje zmiany motywu
def apply_theme():
    current_theme = themes_var.get()
    bg_color = themes[current_theme]["bg"]
    fg_color = themes[current_theme]["fg"]

    root.configure(bg=bg_color)
    status_bar.configure(bg=bg_color, fg=fg_color)

    for widget in root.winfo_children():
        widget_type = widget.winfo_class()
        if widget_type not in ('TFrame', 'TLabel', 'TNotebook', 'TButton', 'TCombobox', 'TEntry', 'TTreeview'):
            continue
        widget.configure(bg=bg_color, fg=fg_color)
        if widget_type == 'TNotebook':
            for tab in widget.tabs():
                widget.tab(tab, background=bg_color, foreground=fg_color)

themes = {
    "Azure-Lime": {"bg": "#00FFFF", "fg": "#32CD32"},
    "Dark": {"bg": "black", "fg": "white"}
}

themes_var = tk.StringVar(value="Azure-Lime")
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Motyw", menu=theme_menu)
theme_menu.add_radiobutton(label="Azure-Lime", variable=themes_var, command=apply_theme)
theme_menu.add_radiobutton(label="Dark", variable=themes_var, command=apply_theme)

# Uruchomienie paska statusu
update_status_bar()

# Wczytanie danych
load_all_data()

class ConversionApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Nagłówek
        self.header_frame = ttk.Frame(self.parent, padding="10")
        self.header_frame.grid(row=0, column=0, sticky="ew")

        self.date_time_label = ttk.Label(self.header_frame, text=self.get_current_date_time())
        self.date_time_label.grid(row=0, column=0, sticky="w")
        self.update_date_time()

        self.theme_label = ttk.Label(self.header_frame, text="Motyw:")
        self.theme_label.grid(row=0, column=1, sticky="e")

        self.theme_switch = ttk.Combobox(self.header_frame, values=["Jasny", "Ciemny"])
        self.theme_switch.grid(row=0, column=2, sticky="e")
        self.theme_switch.current(0)
        self.theme_switch.bind("<<ComboboxSelected>>", self.switch_theme)

        # Główna część aplikacji
        self.main_frame = ttk.Frame(self.parent, padding="10")
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.article_name_label = ttk.Label(self.main_frame, text="Nazwa artykułu")
        self.article_name_label.grid(row=0, column=0, sticky="w")

        self.article_name_entry = ttk.Entry(self.main_frame)
        self.article_name_entry.grid(row=0, column=1, sticky="ew")

        self.total_weight_label = ttk.Label(self.main_frame, text="Waga całkowita")
        self.total_weight_label.grid(row=1, column=0, sticky="w")

        self.total_weight_entry = ttk.Entry(self.main_frame)
        self.total_weight_entry.grid(row=1, column=1, sticky="ew")

        self.total_weight_unit = ttk.Combobox(self.main_frame, values=["kg", "g"])
        self.total_weight_unit.grid(row=1, column=2)
        self.total_weight_unit.current(0)

        self.single_weight_label = ttk.Label(self.main_frame, text="Waga 1 sztuki")
        self.single_weight_label.grid(row=2, column=0, sticky="w")

        self.single_weight_entry = ttk.Entry(self.main_frame)
        self.single_weight_entry.grid(row=2, column=1, sticky="ew")

        self.single_weight_unit = ttk.Combobox(self.main_frame, values=["g", "kg"])
        self.single_weight_unit.grid(row=2, column=2)
        self.single_weight_unit.current(0)

        self.waste_weight_label = ttk.Label(self.main_frame, text="Waga odpadu na 1 sztukę")
        self.waste_weight_label.grid(row=3, column=0, sticky="w")

        self.waste_weight_entry = ttk.Entry(self.main_frame)
        self.waste_weight_entry.grid(row=3, column=1, sticky="ew")

        self.waste_weight_unit = ttk.Combobox(self.main_frame, values=["g", "kg"])
        self.waste_weight_unit.grid(row=3, column=2)
        self.waste_weight_unit.current(0)

        self.result_label = ttk.Label(self.main_frame, text="Liczba sztuk: ", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)

        self.error_label = ttk.Label(self.main_frame, text="", foreground="red")
        self.error_label.grid(row=5, column=0, columnspan=3)

        self.calculate_button = ttk.Button(self.main_frame, text="Przelicz", command=self.calculate_pieces)
        self.calculate_button.grid(row=6, column=0, sticky="ew")

        self.reset_button = ttk.Button(self.main_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=6, column=1, sticky="ew")

        self.export_button = ttk.Button(self.main_frame, text="Eksportuj do CSV", command=self.export_to_csv)
        self.export_button.grid(row=7, column=0, columnspan=3, sticky="ew")

        self.history_label = ttk.Label(self.main_frame, text="Historia Kalkulacji", font=("Arial", 12))
        self.history_label.grid(row=8, column=0, columnspan=3, pady=10)

        self.history_tree = ttk.Treeview(self.main_frame, columns=("article", "total", "unit", "single", "s_unit", "waste", "w_unit", "pieces"), show="headings")
        self.history_tree.grid(row=9, column=0, columnspan=3, sticky="nsew")

        self.history_tree.heading("article", text="Nazwa artykułu")
        self.history_tree.heading("total", text="Waga całkowita")
        self.history_tree.heading("unit", text="Jednostka")
        self.history_tree.heading("single", text="Waga 1 sztuki")
        self.history_tree.heading("s_unit", text="Jednostka")
        self.history_tree.heading("waste", text="Waga odpadu")
        self.history_tree.heading("w_unit", text="Jednostka")
        self.history_tree.heading("pieces", text="Liczba sztuk")

        self.summary_label = ttk.Label(self.main_frame, text="Podsumowanie", font=("Arial", 12))
        self.summary_label.grid(row=10, column=0, columnspan=3, pady=10)

        self.summary_content = ttk.Label(self.main_frame, text="", font=("Arial", 10))
        self.summary_content.grid(row=11, column=0, columnspan=3)

        self.reset_summary_button = ttk.Button(self.main_frame, text="Resetuj Podsumowanie", command=self.reset_summary)
        self.reset_summary_button.grid(row=12, column=0, columnspan=3, sticky="ew")

        self.print_button = ttk.Button(self.main_frame, text="Drukuj historię", command=self.print_history)
        self.print_button.grid(row=13, column=0, columnspan=3, sticky="ew")

    def get_current_date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_date_time(self):
        self.date_time_label.config(text=self.get_current_date_time())
        self.parent.after(1000, self.update_date_time)

    def switch_theme(self, event):
        if self.theme_switch.get() == "Ciemny":
            self.parent.tk_setPalette(background='#333', foreground='#fff')
        else:
            self.parent.tk_setPalette(background='#f4f4f9', foreground='#333')

    def calculate_pieces(self):
        try:
            article_name = self.article_name_entry.get()
            total_weight = float(self.total_weight_entry.get())
            single_weight = float(self.single_weight_entry.get())
            waste_weight = float(self.waste_weight_entry.get())
            total_weight_unit = self.total_weight_unit.get()
            single_weight_unit = self.single_weight_unit.get()
            waste_weight_unit = self.waste_weight_unit.get()

            if not article_name or total_weight <= 0 or single_weight <= 0 or waste_weight < 0:
                raise ValueError("Podaj prawidłowe wartości dla nazwy artykułu, wagi całkowitej, wagi 1 sztuki i wagi odpadu.")

            total_weight_g = total_weight * 1000 if total_weight_unit == "kg" else total_weight
            single_weight_g = single_weight * 1000 if single_weight_unit == "kg" else single_weight
            waste_weight_g = waste_weight * 1000 if waste_weight_unit == "kg" else waste_weight

            effective_weight_per_piece_g = single_weight_g + waste_weight_g
            pieces = total_weight_g // effective_weight_per_piece_g

            self.result_label.config(text=f"Liczba sztuk: {int(pieces)}")
            self.error_label.config(text="")

            self.add_to_history(article_name, total_weight, total_weight_unit, single_weight, single_weight_unit, waste_weight, waste_weight_unit, int(pieces))
            self.update_summary()

        except ValueError as e:
            self.error_label.config(text=str(e))

    def reset_form(self):
        self.article_name_entry.delete(0, tk.END)
        self.total_weight_entry.delete(0, tk.END)
        self.single_weight_entry.delete(0, tk.END)
        self.waste_weight_entry.delete(0, tk.END)
        self.result_label.config(text="Liczba sztuk: ")
        self.error_label.config(text="")
        self.total_weight_unit.current(0)
        self.single_weight_unit.current(0)
        self.waste_weight_unit.current(0)

    def add_to_history(self, article_name, total_weight, total_weight_unit, single_weight, single_weight_unit, waste_weight, waste_weight_unit, pieces):
        self.history_tree.insert("", "end", values=(article_name, total_weight, total_weight_unit, single_weight, single_weight_unit, waste_weight, waste_weight_unit, pieces))

    def update_summary(self):
        total_weight_sum = 0
        total_pieces = 0

        for row in self.history_tree.get_children():
            values = self.history_tree.item(row, "values")
            total_weight = float(values[1])
            total_weight_unit = values[2]
            pieces = int(values[7])

            total_pieces += pieces
            total_weight_sum += total_weight * 1000 if total_weight_unit == "kg" else total_weight

        total_weight_sum_kg = total_weight_sum / 1000
        self.summary_content.config(text=f"Łączna waga całkowita: {total_weight_sum_kg:.2f} kg\nŁączna liczba sztuk: {total_pieces}")

    def reset_summary(self):
        self.summary_content.config(text="")

    def export_to_csv(self):
        with open("history.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nazwa artykułu", "Waga całkowita", "Jednostka", "Waga 1 sztuki", "Jednostka", "Waga odpadu", "Jednostka", "Liczba sztuk"])
            for row in self.history_tree.get_children():
                writer.writerow(self.history_tree.item(row, "values"))
        messagebox.showinfo("Eksportuj do CSV", "Historia została wyeksportowana do pliku history.csv")

    def print_history(self):
        # Drukowanie historii nie jest bezpośrednio obsługiwane przez Tkinter, należy zapisać historię do pliku i drukować z zewnętrznego programu
        self.export_to_csv()
        messagebox.showinfo("Drukuj historię", "Historia została zapisana do pliku history.csv. Wydrukuj plik history.csv z użyciem zewnętrznego programu.")


# Uruchomienie aplikacji
root.mainloop()