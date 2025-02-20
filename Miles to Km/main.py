from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    if miles:
        km = float(miles) * 1.609
        kilometer_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Miles to KM Converter")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * 0.3)
window_height = int(screen_height * 0.2)

window.geometry(f"{window_width}x{window_height}+{int(screen_width*0.35)}+{int(screen_height*0.3)}")
window.config(padx=window_width // 20, pady=window_height // 20)



miles_input = Entry(width=10)
miles_input.grid(column=1, row=0, padx=window_width//40, pady=window_height//40)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=window_width//40, pady=window_height//40)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx=window_width//40, pady=window_height//40)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1, padx=window_width//40, pady=window_height//40)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1, padx=window_width//40, pady=window_height//40)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2, padx=window_width//40, pady=window_height//30)

window.mainloop()
