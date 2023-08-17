from classCar import Car

import tkinter
from tkinter import ttk  # themed tkinter for combobox widget
from tkinter import messagebox  # pop-up window


#
# Checking if customer money < car price
def result():
    terms_status = terms_status_var.get()
    if terms_status == 'Accepted':
        name = name_entry.get()
        age = int(age_spinbox.get())
        gender = gender_combobox.get()
        money = float(money_spinbox.get())

        result_str = f'\n{name} can buy:\n\n'
        for car in cars_obj_list:
            if money >= car.price:
                result_str += car.__str__() + '\n'

        if result_str != f'\n{name} can buy:\n\n':  # if cars added
            result_label['text'] = result_str  # ['text']?
        else:  # if not enough money
            result_label['text'] = result_str + 'Bicycle\n'
    else:  # if Terms not accepted show Warning
        tkinter.messagebox.showwarning(title='Warning', message='You have not accepted Terms & Conditions.')


#
# CARS INFO from file
with open('Cars_data.txt', 'r') as file:  # read data from file to list
    li = file.readlines()
# print(li)

cars_obj_list = []
for i in li:  # each item from list to Car class instance and all class instances to list
    temp_list = i.split()
    obj = Car(temp_list[0], temp_list[1], float(temp_list[2]), int(temp_list[3]))
    cars_obj_list.append(obj)
# print(cars_obj_list[0].__str__())

#
# TKINTER
font_params = ('Arial', 11)
window = tkinter.Tk()
window.title('Auto Shop')

frame = tkinter.Frame(window)  # create / define widget
frame.pack()  # place widget

#
# Output Cars info
cars_info_frame = tkinter.LabelFrame(frame, text='Available Cars', font=font_params)  # tkinter.$$$(PARENT, PARAMS)
cars_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='news')  # sticky='news' - expand frame NorthEastWestSouth

car_01_image = tkinter.PhotoImage(file='car_red_01.png')
car_01_image_label = tkinter.Label(cars_info_frame, image=car_01_image)
car_01_image_label.grid(row=0, column=0)

car_01_info = tkinter.Label(cars_info_frame, text=cars_obj_list[0].__str__(), font=font_params)
car_01_info.grid(row=0, column=1, sticky='w')

car_02_image = tkinter.PhotoImage(file='car_green_01.png')
car_02_image_label = tkinter.Label(cars_info_frame, image=car_02_image)
car_02_image_label.grid(row=1, column=0)

car_02_info = tkinter.Label(cars_info_frame, text=cars_obj_list[1].__str__(), font=font_params)
car_02_info.grid(row=1, column=1, sticky='w')

car_03_image = tkinter.PhotoImage(file='car_white_01.png')
car_03_image_label = tkinter.Label(cars_info_frame, image=car_03_image)
car_03_image_label.grid(row=2, column=0)

car_03_info = tkinter.Label(cars_info_frame, text=cars_obj_list[2].__str__(), font=font_params)
car_03_info.grid(row=2, column=1, sticky='w')

for widget in cars_info_frame.winfo_children():  # Spacing Cars elements
    widget.grid_configure(padx=10, pady=5)

#
# CUSTOMER INFO from input
customer_info_frame = tkinter.LabelFrame(frame, text='Customer Information', font=font_params)
customer_info_frame.grid(row=1, column=0, padx=20, pady=10, sticky='news')  # New main frame Row

name_label = tkinter.Label(customer_info_frame, text='Name', font=font_params)
name_label.grid(row=0, column=0)

age_label = tkinter.Label(customer_info_frame, text='Age', font=font_params)
age_label.grid(row=0, column=1)

name_entry = tkinter.Entry(customer_info_frame, font=font_params)
name_entry.grid(row=1, column=0)

age_spinbox = tkinter.Spinbox(customer_info_frame, from_=18, to=99, font=font_params)
age_spinbox.grid(row=1, column=1)

gender_label = tkinter.Label(customer_info_frame, text='Gender', font=font_params)
gender_label.grid(row=2, column=0)

money_label = tkinter.Label(customer_info_frame, text='Money', font=font_params).grid(row=2, column=1)

gender_combobox = ttk.Combobox(customer_info_frame, values=['', 'male', 'female'], font=font_params)
gender_combobox.grid(row=3, column=0)

money_spinbox = tkinter.Spinbox(customer_info_frame, from_=5000, to=50000, increment=1000, font=font_params)
money_spinbox.grid(row=3, column=1)

for widget in customer_info_frame.winfo_children():  # Spacing Customer elements
    widget.grid_configure(padx=10, pady=5)

#
# Terms Frame
terms_frame = tkinter.LabelFrame(frame, text='Terms & Conditions', font=font_params)
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_status_var = tkinter.StringVar(value='Accepted')
terms_check = tkinter.Checkbutton(terms_frame, text='I accept terms and conditions', variable=terms_status_var,
                                  onvalue='Accepted', offvalue='Not accepted', font=font_params)
terms_check.grid(row=0, column=0, padx=10, pady=5)

#
# Button
button = tkinter.Button(frame, text='What can buy?', command=result, font=font_params)
button.grid(row=3, column=0, sticky='news', padx=80, pady=10)

#
# RESULT output
result_label = tkinter.Label(frame, bg='#d7d7d7', fg='black', height=5, font=font_params)
result_label.grid(row=4, column=0, sticky='news', padx=20, pady=10)


window.mainloop()
