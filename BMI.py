import tkinter

window= tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=50,pady=50)

def calculate_button():
    height=height_input.get()
    weight= weihgt_input.get()
    bmi=float(weight)/((float(height)/100)**2)
    result=write_result(bmi)
    result_label.config(text=result)

weihgt_input_label=tkinter.Label(text="Enter your weight")
weihgt_input_label.pack()
weihgt_input=tkinter.Entry()
weihgt_input.pack()
height_input_label=tkinter.Label(text="Please enter your height")
height_input_label.pack()
height_input=tkinter.Entry()
height_input.pack()
calculate=tkinter.Button(text="Calculate",command=calculate_button)
calculate.pack()
result_label=tkinter.Label()
result_label.pack()

def write_result(bmi):
    result=f"Your BMI is {round(bmi,2)}. You are "
    if bmi<=16:
        result+= "severely thin!"
    elif 16 < bmi <= 17:
        result += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result += "mild thin!"
    elif 18.5 < bmi <= 25:
        result += "normal weight"
    elif 25 < bmi <= 30:
        result+= "overweight"
    elif 30 < bmi <= 35:
        result += "obese class 1"
    elif 35 < bmi <= 40:
        result+= "obese class 2"
    else:
        result+= "obese class 3"
    return result


window.mainloop()
