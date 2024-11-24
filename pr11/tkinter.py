import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Создание основного окна
root = tk.Tk()
root.title("Maksimenko A.S.")
root.geometry("500x500")

# Создание виджета Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Создание вкладок
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Добавление вкладок
notebook.add(tab1, text='Калькулятор')
notebook.add(tab2, text='Чекбоксы')
notebook.add(tab3, text='Текст')

# Калькулятор
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "!OOPS!ERЯ0R!: Вы делите на 0 >:("

    label_result.config(text=f"Результат: {result}")

label_num1 = ttk.Label(tab1, text="Первое число:")
label_num1.pack(pady=10)

entry_num1 = ttk.Entry(tab1)
entry_num1.pack(pady=10)

label_num2 = ttk.Label(tab1, text="Второе число:")
label_num2.pack(pady=10)

entry_num2 = ttk.Entry(tab1)
entry_num2.pack(pady=10)

operation_var = tk.StringVar(value='+')
operation_dropdown = ttk.Combobox(tab1, textvariable=operation_var, values=['+', '-', '*', '/'])
operation_dropdown.pack(pady=10)

button_calculate = ttk.Button(tab1, text="Посчитать", command=calculate)
button_calculate.pack(pady=20)

label_result = ttk.Label(tab1, text="Тут будет результат вашего примера :р")
label_result.pack(pady=10)

# Чекбоксы
def show_selection():
    selected_options = []
    if checkbox1_var.get():
        selected_options.append("Голубой цвет")
    if checkbox2_var.get():
        selected_options.append("Красный цвет")
    if checkbox3_var.get():
        selected_options.append("Желтый цвет")
    if checkbox4_var.get():
        selected_options.append("Фиолетовый цвет")
    if checkbox5_var.get():
        selected_options.append("Никакой цвет")

    messagebox.showinfo("Ваш предпочитаемый цвет?", "Вы выбрали: " + ", ".join(selected_options))

checkbox1_var = tk.IntVar()
checkbox2_var = tk.IntVar()
checkbox3_var = tk.IntVar()
checkbox4_var = tk.IntVar()
checkbox5_var = tk.IntVar()

checkbox1 = ttk.Checkbutton(tab2, text="Голубой", variable=checkbox1_var)
checkbox1.pack(pady=20)

checkbox2 = ttk.Checkbutton(tab2, text="Красный", variable=checkbox2_var)
checkbox2.pack(pady=20)

checkbox3 = ttk.Checkbutton(tab2, text="Желтый", variable=checkbox3_var)
checkbox3.pack(pady=20)

checkbox4 = ttk.Checkbutton(tab2, text="Фиолетовый", variable=checkbox4_var)
checkbox4.pack(pady=20)

checkbox5 = ttk.Checkbutton(tab2, text="Никакой)0)", variable=checkbox5_var)
checkbox5.pack(pady=20)

button_show_selection = ttk.Button(tab2, text="Показать мой ответ", command = show_selection)
button_show_selection.pack(pady=40)


# Текст
def load_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        text_area.delete(1.0, tk.END)  # Очистка текстовой области
        text_area.insert(tk.END, content)  # Загрузка текста


text_area = tk.Text(tab3, wrap='word', height=15)
text_area.pack(expand=True, fill='both')

button_load = ttk.Button(tab3, text="Загрузить текст из файла", command=load_file)
button_load.pack(pady=10)

root.mainloop()
