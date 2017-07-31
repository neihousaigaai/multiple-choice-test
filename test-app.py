#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox, filedialog
from datetime import datetime

WIDTH = 800   # WIDTH = root.winfo_screenwidth()
HEIGHT = 450  # HEIGHT = root.winfo_screenheight()
WW = 250
WH = 250
w = 50
h = 25
killed = False
ans = {}
resLab = {}
time_lasted = 0


def MainWindow(event):
	global questions, subject, name, date, time
	questions = questions_entry.get()
	subject = subject_entry.get()
	name = name_entry.get()
	date = str(datetime.now())
	_time = time_entry.get()

	if (date.find('.') != -1):
		date = date[:date.find('.')]
	date = date.replace(" ", "_")

	global N, T
	try:
		N = int(questions)
	except:
		N = -1
	try:
		T = int(_time)
	except:
		T = -1

	if not (questions != '' and N > 0 and subject != '' and name != '' and _time != '' and T > 0):
		return None

	win.destroy()


def Answer(st):
	for i in range(1, N + 1):
		A[i].config(state=st)
		B[i].config(state=st)
		C[i].config(state=st)
		D[i].config(state=st)


def Start():
	# if (startButton["state"] == NORMAL or startButton["state"] == "active"): # same as below
	if (startButton["state"] != 'disabled'):
		startButton.config(state=DISABLED)
		stopButton.config(state=NORMAL)
		Answer(NORMAL)
		root.after(1000, countdown)


def countdown():
	_h = int(hourBox.get())
	_m = int(minBox.get())
	_s = int(secBox.get())

	if (_h + _m + _s == 0 or killed is True):
		checkButton.config(state=NORMAL)
		stopButton.config(state=DISABLED)
		Answer(DISABLED)
		if (_h + _m + _s == 0):
			messagebox.showinfo("Notification", "Test has been ended.", )
		return None

	global time_lasted
	time_lasted += 1

	if _s > 0:
		_s -= 1
	else:
		if _m > 0:
			_m -= 1
			_s += 59
		else:
			if _h > 0:
				_h -= 1
				_m += 59
				_s += 59

				hourBox.config(state=NORMAL)
				hourBox.delete(0, END)
				hourBox.insert(END, ('0' if _h < 10 else '') + str(_h))
				hourBox.config(state=DISABLED)
			else:
				return None

		minBox.config(state=NORMAL)
		minBox.delete(0, END)
		minBox.insert(END, ('0' if _m < 10 else '') + str(_m))
		minBox.config(state=DISABLED)

	secBox.config(state=NORMAL)
	secBox.delete(0, END)
	secBox.insert(END, ('0' if _s < 10 else '') + str(_s))
	secBox.config(state=DISABLED)

	root.after(1000, countdown)


def Stop():
	if messagebox.askyesno("Stop", "Do you really want to stop? You can't redo this."):
		global killed
		killed = True
		Answer(DISABLED)
		messagebox.showinfo("Stopped", "You have stopped the test.")


def Check():
	# True: u'\u2713'
	# False: u'\u2717'

	s = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

	fi = open(s, 'r')
	while 1 == 1:
		ss = fi.readline()
		if len(ss) == 0:
			break
		else:
			if ss[len(ss)-1] == '\n':
				ss = ss[:len(ss)-1]

		ss.replace(' ', '')
		ans[int(ss[:len(ss)-1])] = ss[len(ss)-1]

	global true, false, blank
	true = 0
	false = 0
	blank = 0

	for i in range(1, N + 1):
		if var[i].get() == ans[i]:
			resLab[i].config(text=u'\u2713', fg="#00FF00")
			true += 1
		else:
			resLab[i].config(text=u'\u2717', fg="#FF0000")
			if (var[i].get() != "E"):
				false += 1
			else:
				blank += 1
	exportButton.config(state=NORMAL)

	global score
	score = ((true*1.0)/(N*1.0))*10.0

	scoreBox.config(state=NORMAL)
	scoreBox.delete(0, END)
	scoreBox.insert(END, str("{0:.2f}".format(score)))
	scoreBox.config(state=DISABLED)


def Export():
	fo = filedialog.asksaveasfile(title="Save report file", filetypes=[("Text files", "*.txt")], defaultextension='.txt')

	fo.write("Date: " + date + '\n')
	fo.write("Name: " + name + '\n')
	fo.write("Subject: " + subject + '\n')

	fo.write("Time: "
	         + ('0' if (time_lasted // 3600) < 10 else '') + str(time_lasted // 3600) + ':'
	         + ('0' if ((time_lasted % 3600) // 60) < 10 else '') + str((time_lasted % 3600) // 60) + ':'
	         + ('0' if (time_lasted % 60) < 10 else '') + str(time_lasted % 60) + "/"
	         + ('0' if (T // 60) < 10 else '') + str(T // 60) + ':'
	         + ('0' if (T % 60) < 10 else '') + str(T % 60) + ':00\n')
	fo.write("------------------------------\n")
	fo.write("Result: \n")
	fo.write("False: " + str(false) + "/" + str(N) + '\n')
	fo.write("Blank: " + str(blank) + "/" + str(N) + '\n')
	fo.write("True: " + str(true) + "/" + str(N) + '\n')
	fo.write("Score: " + str("{0:.2f}".format(score)) + '\n')
	fo.close()

	messagebox.showinfo("Saved", "Report has been saved.")


#-------------------------------------------------------------------
win = Tk()
win.wm_title("Init")
win.geometry("%dx%d+%d+%d" % (WW, WH, (win.winfo_screenwidth() - WW) // 2, (win.winfo_screenheight() - WH) // 2))
win.resizable(0, 0)

_h = 20
normal_font = "Arial 9"

questions_label = Label(win, text="Number of questions: ", anchor='w') #, font=normal_font)
questions_label.pack()
questions_label.place(x=20, y=5, height=_h, width=120)

questions_entry = Entry(win, bd=1) #, font=normal_font)
questions_entry.pack()
questions_entry.place(x=150, y=5, height=_h, width=WW-150-20)

subject_label = Label(win, text="Subject: ", anchor='w') #, font=normal_font)
subject_label.pack()
subject_label.place(x=20, y=35, height=_h, width=50)

subject_entry = Entry(win, bd=1) #, font=normal_font)
subject_entry.pack()
subject_entry.place(x=80, y=35, height=_h, width=WW-80-20)

name_label = Label(win, text="Name: ", anchor='w') #, font=normal_font)
name_label.pack()
name_label.place(x=20, y=65, height=_h, width=40)

name_entry = Entry(win, bd=1) #, font=normal_font)
name_entry.pack()
name_entry.place(x=70, y=65, height=_h, width=WW-70-20)

time_label = Label(win, text="Time (min): ", anchor='w') #, font=normal_font)
time_label.pack()
time_label.place(x=20, y=95, height=_h, width=65)

time_entry = Entry(win, bd=1) #, font=normal_font)
time_entry.pack()
time_entry.place(x=95, y=95, height=_h, width=WW-95-20)

OK = Button(win, text="OK", command=lambda event=None: MainWindow(event))
OK.pack()
OK.place(x=(WW - w) // 2, y=210, height=h, width=w)

win.bind('<Return>', MainWindow)
win.mainloop()
#-------------------------------------------------------------------
root = Tk()
root.wm_title("Test")
root.resizable(0, 0)
root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, (root.winfo_screenwidth() - WIDTH) // 2,
                               (root.winfo_screenheight() - HEIGHT) // 2))

_w = 50
_d = 10
_L = 50
BG = "#00FFFF"
FONT = "Arial 20"

#frame 1
fr1 = Frame(root, bg=BG, bd=0)
fr1.pack()
fr1.place(x=(WIDTH-(3*_w+2*_d)) // 2, y=25, height=_w, width=3*_w+2*_d)

hourBox = Entry(fr1, bg=BG, bd=0, justify=CENTER, font=FONT, cursor="arrow")
hourBox.pack()
hourBox.place(x=0, y=0, height=_w, width=_w)
hourBox.insert('end', ('0' if (T // 60) < 10 else '') + str(T // 60))
hourBox.config(state=DISABLED, disabledbackground=BG, disabledforeground="#000000")

l1 = Label(fr1, text=":", bg=BG, bd=0, justify=CENTER, font=FONT)
l1.pack()
l1.place(x=_w, y=0, height=_w, width=_d)

minBox = Entry(fr1, bg=BG, bd=0, justify=CENTER, font=FONT, cursor="arrow")
minBox.pack()
minBox.place(x=_w+_d, y=0, height=_w, width=_w)
minBox.insert('end', ('0' if (T % 60) < 10 else '') + str(T % 60))
minBox.config(state=DISABLED, disabledbackground=BG, disabledforeground="#000000")

l2 = Label(fr1, text=":", bg=BG, bd=0, justify=CENTER, font=FONT)
l2.pack()
l2.place(x=2*_w+_d, y=0, height=_w, width=_d)

secBox = Entry(fr1, bg=BG, bd=0, justify=CENTER, font=FONT, cursor="arrow")
secBox.pack()
secBox.place(x=2*(_w+_d), y=0, height=_w, width=_w)
secBox.insert('end', '00')
secBox.config(state=DISABLED, disabledbackground=BG, disabledforeground="#000000")

#frame 2
_h = 30
fr2 = Frame(root, bd=0)
fr2.pack()
fr2.place(x=_L, y=35, height=_h, width=4*(_w+_d)-_d)

startButton=Button(fr2, text="Start", command=Start, state=NORMAL)
startButton.pack()
startButton.place(x=0, y=0, height=_h, width=_w)

stopButton=Button(fr2, text="Stop", command=Stop, state=DISABLED)
stopButton.pack()
stopButton.place(x=_w+_d, y=0, height=_h, width=_w)

checkButton=Button(fr2, text="Check", command=Check, state=DISABLED)
checkButton.pack()
checkButton.place(x=2*(_w+_d), y=0, height=_h, width=_w)

exportButton=Button(fr2, text="Export", command=Export, state=DISABLED)
exportButton.pack()
exportButton.place(x=3*(_w+_d), y=0, height=_h, width=_w)

#frame 3
fr3 = Frame(root, bg=BG, bd=0)
fr3.pack()
fr3.place(x=WIDTH-_L-(2*_w), y=25, height=_w, width=2*_w)

scoreBox = Entry(fr3, justify=CENTER, font=FONT, cursor="arrow")
scoreBox.pack()
scoreBox.place(x=0, y=0, height=_w, width=2*_w)
scoreBox.config(state=DISABLED, disabledforeground="#FF0000")

#frame 4
var, A, B, C, D = {}, {}, {}, {}, {}
_m = 4
_n = int(N % _m > 0) + N // _m
_X = 0
_Y = 100
lenN = len(str(N))

fr4 = Frame(root)
fr4.pack()
fr4.place(x=_X, y=_Y, height=_Y+_n*23, width=_X+_m*200)

for i in range(_m):
	for j in range(_n):
		n = i*_n + (j+1)
		if (n > N):
			break

		fr = Frame(fr4)
		fr.place(x=i*200, y=j*23)

		num = Label(fr, text=str(n) + '.', width=lenN + 2)
		num.grid(row=0, column=0)

		var[n] = StringVar()
		var[n].set(" ")

		A[n] = Radiobutton(fr, text="A", variable=var[n], value="A", state=DISABLED)
		A[n].grid(row=0, column=1)
		B[n] = Radiobutton(fr, text="B", variable=var[n], value="B", state=DISABLED)
		B[n].grid(row=0, column=2)
		C[n] = Radiobutton(fr, text="C", variable=var[n], value="C", state=DISABLED)
		C[n].grid(row=0, column=3)
		D[n] = Radiobutton(fr, text="D", variable=var[n], value="D", state=DISABLED)
		D[n].grid(row=0, column=4)

		resLab[n] = Label(fr, text='', font="Arial 16")
		resLab[n].grid(row=0, column=5)

root.mainloop()