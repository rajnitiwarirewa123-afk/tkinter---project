import tkinter as tk

def result():
    try:
        m1 = int(sub1.get())
        m2 = int(sub2.get())
        m3 = int(sub3.get())
        m4 = int(sub4.get())

        total = m1 + m2 + m3 + m4
        percent = total / 4

        output.config(
            text=f"Total Marks: {total}\nPercentage: {percent}%"
        )
    except:
        output.config(text="Please enter only numbers")

root = tk.Tk()
root.title("Student Result System")
root.geometry("400x500")
root.configure(bg="lightgray")

tk.Label(root, text="Student Result Management System",
         font=("Arial", 14), bg="lightgray").pack(pady=10)

tk.Label(root, text="Roll Number", bg="lightgray").pack()
roll_input = tk.Entry(root)
roll_input.pack()

tk.Label(root, text="Student Name", bg="lightgray").pack()
name_input = tk.Entry(root)
name_input.pack()

tk.Label(root, text="Python Marks", bg="lightgray").pack()
sub1 = tk.Entry(root)
sub1.pack()

tk.Label(root, text="Maths Marks", bg="lightgray").pack()
sub2 = tk.Entry(root)
sub2.pack()

tk.Label(root, text="English Marks", bg="lightgray").pack()
sub3 = tk.Entry(root)
sub3.pack()

tk.Label(root, text="Discrete Maths Marks", bg="lightgray").pack()
sub4 = tk.Entry(root)
sub4.pack()

tk.Button(root, text="Calculate Result",
          command=result).pack(pady=10)

output = tk.Label(root, text="", bg="lightgray", font=("Arial", 12))
output.pack()

root.mainloop()
