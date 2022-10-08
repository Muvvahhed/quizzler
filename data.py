import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzler Setup")
window.config(padx=30, pady=20, bg=THEME_COLOR)
data = NONE


def submit():
    global data
    categories = {
        "General Knowledge": 9,
        "Science & Nature": 17,
        "Sports": 21,
        "Geography": 22,
        "History": 23,
        "Animals": 27,
        "Movies": 11,
    }
    difficulty = {
        "Normal": "easy",
        "Hard": "medium"
    }
    parameters = {
        "amount": int(spin_box.get()),
        "type": "boolean",
        "difficulty": difficulty[difficulty_combo_box.get()],
        "category": categories[category_combo_box.get()],
    }
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        data = response.json()

    except:
        messagebox.showinfo("Quizzler", "No Internet Connection")

    else:
        if len(data["results"]) == 0:
            messagebox.showinfo("Quizzler", "No Questions\n\n"
                                            " Please change the number of questions or the difficulty")
        else:
            window.destroy()


# labels
label0 = Label(text="Quizzler", font=("Jokerman", 40, "bold"), fg="white", bg=THEME_COLOR)
label0.grid(row=0, column=0, columnspan=2, )

label1 = Label(text="Please select the following", font=("Courier", 18, "bold"), fg="white", bg=THEME_COLOR)
label1.grid(row=1, column=0, columnspan=2, sticky=W, ipady=10)

label2 = Label(text="Difficulty:", font=("Courier", 18, "bold"), fg="white", bg=THEME_COLOR)
label2.grid(row=2, column=0, sticky=W)

label3 = Label(text="Category:", font=("Courier", 18, "bold"), fg="white", bg=THEME_COLOR)
label3.grid(row=3, column=0, sticky=W)

label4 = Label(text="Number of questions:", font=("Courier", 18, "bold"), fg="white", bg=THEME_COLOR)
label4.grid(row=4, column=0, sticky=W)


# combo box


difficulty_combo_box = ttk.Combobox(values=("Normal", "Hard"), state='readonly', )
difficulty_combo_box.current(newindex=0)
difficulty_combo_box.grid(row=2, column=1, sticky=EW)


categories_list = ("General Knowledge", "Science & Nature", "Sports", "Geography", "History", "Animals", "Movies")
category_combo_box = ttk.Combobox(values=categories_list, state='readonly', width=20)
category_combo_box.current(newindex=0)
category_combo_box.grid(row=3, column=1, sticky=EW)


# spin_box
current_value = StringVar(value=10)

spin_box = ttk.Spinbox(
    window,
    from_=10,
    to=50,
    textvariable=current_value,
    values=(10, 15, 20),
    state="readonly")

spin_box.grid(row=4, column=1, sticky=EW)

# button
submit_button = Button(text="START", bg="cyan", activebackground="cyan", command=submit)
submit_button.grid(row=5, column=0, columnspan=3, sticky=EW, pady=10, ipady=10)

window.mainloop()



try:
    question_data = data["results"]
except TypeError:
    pass