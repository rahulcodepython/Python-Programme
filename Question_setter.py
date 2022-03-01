from tkinter import *

root = Tk()

# Set title of the interface
root.title("First GUI App made by")

# Set the size of the interface
root.geometry("600x600")

# Declair the variable
question = StringVar()
option_A = StringVar()
option_B = StringVar()
option_C = StringVar()
option_D = StringVar()
ans = IntVar()

question_no = 0

list_a = []

# Declair Fuctions
def submit():
	q = question.get()
	a = option_A.get()
	b = option_B.get()
	c = option_C.get()
	d = option_D.get()

	global question_no
	question_no+=1

	list_o = []
	list_q = []

	list_o.append(a)
	list_o.append(b)
	list_o.append(c)
	list_o.append(d)

	list_q.append(question_no)
	list_q.append(q)
	list_q.append(list_o)
	list_q.append(list_o[ans])

	list_a.append(list_q)

	show_data(list_a)

# Show the list of date
def show_data(main):
	f = open("database_question_setter.txt", "a+")
	for sets in main:
		f.write(f"{sets[0]} {sets[1]}\n")
		Label(frame2, text = f"{sets[0]} {sets[1]}").pack()
		op_no = 1
		for value in sets[2]:
			f.write(f"{op_no}.{value}\n")
			Label(frame2, text = f"{op_no}.{value}").pack()
			op_no+=1
		f.write(f"Ans:- {sets[3]}\n")
		Label(frame2, text = f"Ans:- {sets[3]}").pack()
	f.close()
# Define the correct ans index number
def correct_ans(n):
	global ans
	ans = n

# Set the frame and set it
frame1 = Frame(root)
# frame1.grid(row=0, column=0)
frame1.pack(pady=100)

# Set the entry of the question, answers
Label(frame1, text="Enter the question: ").grid(row=0, column=0, sticky="w")
Entry(frame1, font=('calibre',10), textvariable=question, width=100).grid(row=0, column=1, columnspan=4, ipady=10, sticky="w")
Label(frame1, text="Enter the first option: ").grid(row=1, column=0, sticky="w")
Entry(frame1, font=('calibre',10), textvariable=option_A, width=20).grid(row=1, column=1, columnspan=4, ipady=5, sticky="w")
Label(frame1, text="Enter the second option: ").grid(row=2, column=0, sticky="w")
Entry(frame1, font=('calibre',10), textvariable=option_B, width=20).grid(row=2, column=1, columnspan=4, ipady=5, sticky="w")
Label(frame1, text="Enter the third option: ").grid(row=3, column=0, sticky="w")
Entry(frame1, font=('calibre',10), textvariable=option_C, width=20).grid(row=3, column=1, columnspan=4, ipady=5, sticky="w")
Label(frame1, text="Enter the forth option: ").grid(row=4, column=0, sticky="w")
Entry(frame1, font=('calibre',10), textvariable=option_D, width=20).grid(row=4, column=1, columnspan=4, ipady=5, sticky="w")
Label(frame1, text="Choose the correct option: ").grid(row=5, column=0, sticky="w")
Button(frame1, font=('calibre',10), text="Option A", command=lambda: correct_ans(0)).grid(row=6, column=1)
Button(frame1, font=('calibre',10), text="Option B", command=lambda: correct_ans(1)).grid(row=6, column=2)
Button(frame1, font=('calibre',10), text="Option C", command=lambda: correct_ans(2)).grid(row=6, column=3)
Button(frame1, font=('calibre',10), text="Option D", command=lambda: correct_ans(3)).grid(row=6, column=4)

# Set the calculate button
Button(frame1, font=('calibre',10), command=submit, text="Submit").grid(row=7, column=0, pady=10)
Button(frame1, font=('calibre',10), command=root.destroy, text="Quit").grid(row=7, column=1, pady=10)

# Second Frame
frame2 = Frame(root)
frame2.pack()
Label(frame2, text="Data").pack()
# Label(frame2, text=show_text).pack()

root.mainloop()