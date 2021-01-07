from tkinter import *
from Nesi_Modules import fn_calculate as get_total
from Nesi_Modules import update_list

root=Tk()
root.title("Nesi's PyCalculator")

user_inputs=["0","+"]#this values are here to avoid problems while using the following functions.
#we use this list to do almost all things in this program.
#this list have a specific format. default values are ["0","+"]. each value we need to calculate are addedd to this list
#before adding a number a "0" is added. (why we need to add zero? explained on first use..)
myLabel=Label(root, padx=40, pady=20, text="0",justify="right")#in the begining of the program value in label is set to zero


def button_click(number,list):#this function is called when a number 0-9 is clicked.
    global user_inputs
    #check the last value in user_inputs
    if list[-1] == "b" or list[-1] == "be":#if the value "b"
        del(user_inputs[-1])#remove last item
        #"b" is appended to list when a backspace is used.
        #"be" is appended to list when a backspace is used after pressing equalto symbol
    current=str(e.get())#store the existing value in entrybox to this variable.
    if list[-1] == "=":#if the last value is an equal to symbol
        user_inputs=["0","+"]#clear the user_inputs list, reset to default values.
        myLabel.config(text="0")#reset the value in label to zero
        user_inputs.append("0")
        # we append 0 to user_inputs, otherwise the next time you click a number
        # existing user_inputs will be ["0","+"], last value will remain a symbol.
        # since we already cleared the user_inputs, and we are going to check for symbols next, we dont want that to happen.
        e.delete(0,END)#delete the value in entry box
        e.insert(0,str(number))#insert number from the button to entry box.

    #now lets check if the last value is a symbol.
    elif list[-1]== '+' or list[-1]=="-" or list[-1]=="*" or list[-1]=="/":
        e.delete(0,END)#if symbol delete the value in e.box
        e.insert(0,str(number))
        user_inputs.append("0")#update the user_inputs so that next time the check return false.
    elif current=="0":#if the value in ebox is zero
        e.delete(0,END)#clear ebox
        e.insert(0,str(number))#replace zero with new number.
    else:#if last value is none of the symbols.
        e.delete(0,END)#clear ebox
        e.insert(0,current+str(number))#str(storedvalue)+str(clicked number)


def button_add(list):#this function is called when + is clicked.
    global user_inputs
    #check the last value
    if user_inputs[-1]== 'be':#check if a backspace was used after an equalto symbol.
        del(user_inputs[-1])
        user_inputs.append("0")

    if user_inputs[-1]== '+' or user_inputs[-1]=="-" or user_inputs[-1]=="*" or user_inputs[-1]=="/" or user_inputs[-1]=="b" :
        #if the last value is any of the symbols. replace the symbol.
        user_inputs[-1]="+"#change last value to +
        current=str(e.get())
        e.delete(0,END)#clear ebox
        e.insert(0,current)#return the same value, basically means do nothing.

    elif user_inputs[-1]=="=":#if the last value is an equalto symbol. do nothing, but clear the user_inputs.
        user_inputs=["0","+"]#clear the user_inputs. set to default values.
        current=str(e.get())#get current ebox balue
        user_inputs.extend(("0",current,"+"))#add values to user_inputs.
        e.delete(0,END)#clear ebox
        e.insert(0,current)#insert the same value.
        #reset the value in label to new values in user_inputs.
        myLabel.config(text="".join(update_list(user_inputs)))#here we need the new_user_inputs, lets call user_inputs update function here.

    else:#if the last value is neither of the above.
        current=str(e.get())#get ebox to current
        user_inputs.extend((current,"+"))#add curren value and + to the user_inputs.
        e.delete(0,END)#clear the ebox
        e.insert(0,str(get_total(user_inputs)))#insert the total of the user_inputs
        myLabel.config(text="".join(update_list(user_inputs)))#update label with new_user_inputs


def button_sub(list):#execute this when - is pressed.
    global user_inputs
    #check the last value
    if user_inputs[-1]== 'be':
        del(user_inputs[-1])
        user_inputs.append("0")
    if user_inputs[-1]== '+' or user_inputs[-1]=="-" or user_inputs[-1]=="*" or user_inputs[-1]=="/" or user_inputs[-1]=="b" :
        #if the last value is any of the symbols. replace the symbol.
        user_inputs[-1]="-"
        current=str(e.get())
        e.delete(0,END)#clear ebox
        e.insert(0,current)#return the same value, basically means do nothing.

    elif user_inputs[-1]=="=":#if the last value is an equalto symbol. do nothing, but clear the user_inputs.
        user_inputs=["0","+"]#clear the user_inputs. set to default values.
        current=str(e.get())#get current ebox balue
        user_inputs.extend(("0",current,"-"))#add values to user_inputs.
        e.delete(0,END)#clear ebox
        e.insert(0,current)#insert the same value.
        #reset the value in label to new values in user_inputs.
        myLabel.config(text="".join(update_list(user_inputs)))#here we need the new_user_inputs, lets call user_inputs update function here.

    else:#if the last value is none of the above.
        current=str(e.get())#get ebox to current
        user_inputs.extend((current,"-"))#add curren value and - to the user_inputs.
        e.delete(0,END)#clear the ebox
        e.insert(0,str(get_total(user_inputs)))#insert the total of the user_inputs
        myLabel.config(text="".join(update_list(user_inputs)))#update label with new_user_inputs


def button_mul(list):#execute this when * is pressed.
    global user_inputs
    #check the last value
    if user_inputs[-1]== 'be':
        del(user_inputs[-1])
        user_inputs.append("0")
    if user_inputs[-1]== '+' or user_inputs[-1]=="-" or user_inputs[-1]=="*" or user_inputs[-1]=="/" or user_inputs[-1]=="b" :
        #if the last value is any of the symbols. replace the symbol.
        user_inputs[-1]="*"#
        current=str(e.get())
        e.delete(0,END)#clear ebox
        e.insert(0,current)#return the same value, basically means do nothing.

    elif user_inputs[-1]=="=":#if the last value is an equalto symbol. do nothing, but clear the user_inputs.
        user_inputs=["0","+"]#clear the user_inputs. set to default values.
        current=str(e.get())#get current ebox balue
        user_inputs.extend(("0",current,"*"))#add values to user_inputs.
        e.delete(0,END)#clear ebox
        e.insert(0,current)#insert the same value.
        #reset the value in label to new values in user_inputs.
        myLabel.config(text="".join(update_list(user_inputs)))#here we need the new_user_inputs, lets call user_inputs update function here.

    else:#if the last value is neither of the above.
        current=str(e.get())#get ebox to current
        user_inputs.extend((current,"*"))#add curren value and * to the user_inputs.
        e.delete(0,END)#clear the ebox
        e.insert(0,str(get_total(user_inputs)))#insert the total of the user_inputs
        myLabel.config(text="".join(update_list(user_inputs)))#update label with new_user_inputs


def button_div(list):#execute this when / is pressed.
    global user_inputs
    #check the last value
    if user_inputs[-1]== 'be':
        del(user_inputs[-1])
        user_inputs.append("0")
    if user_inputs[-1]== '+' or user_inputs[-1]=="-" or user_inputs[-1]=="*" or user_inputs[-1]=="/" or user_inputs[-1]=="b" :
        #if the last value is any of the symbols. replace the symbol.
        user_inputs[-1]="/"#
        current=str(e.get())
        e.delete(0,END)#clear ebox
        e.insert(0,current)#return the same value, basically means do nothing.

    elif user_inputs[-1]=="=":#if the last value is an equalto symbol. do nothing, but clear the user_inputs.
        user_inputs=["0","+"]#clear the user_inputs. set to default values.
        current=str(e.get())#get current ebox balue
        user_inputs.extend(("0",current,"/"))#add values to user_inputs.
        e.delete(0,END)#clear ebox
        e.insert(0,current)#insert the same value.
        #reset the value in label to new values in user_inputs.
        myLabel.config(text="".join(update_list(user_inputs)))#here we need the new_user_inputs, lets call user_inputs update function here.

    else:#if the last value is neither of the above.
        current=str(e.get())#get ebox to current
        user_inputs.extend((current,"/"))#add curren value and / to the user_inputs.
        e.delete(0,END)#clear the ebox
        e.insert(0,str(get_total(user_inputs)))#insert the total of the user_inputs
        myLabel.config(text="".join(update_list(user_inputs)))#update label with new_user_inputs


def button_equal(list):#execute this when = is pressed
    global user_inputs
    if user_inputs[-1]== 'be':#did you press backspace after = ?
        del(user_inputs[-1])#if pressed delete the last value in list.
        user_inputs.append("0")
    if user_inputs[-1]=="=":#if = was already pressed once.
        current=str(e.get())
        user_inputs=["0","+"]#reset the list.
        user_inputs.extend(("0",current,list[-4],"0",list[-2],"="))#add these values to list.
        e.delete(0,END)#clear entrybox
        e.insert(0,str(get_total(user_inputs)))#calculate total of the given list, and insert to entry box.
        myLabel.config(text="".join(update_list(user_inputs)))#udate the label.
    else:
        #if none of the above conditions are true, append the number in entrybox to list.
        #do not clear the user_inputs. next time you press any other button it will clear the list.
        current=str(e.get())#get the value in ebox.
        user_inputs.extend((current,"="))#add the current value and = to the user_inputs.
        e.delete(0,END)#clear entry box
        e.insert(0,str(get_total(user_inputs)))#insert the total of the user_inputs
        myLabel.config(text="".join(update_list(user_inputs)))#update label with new_user_inputs


def button_clear():
    global user_inputs
    e.delete(0,END)#clear the entry box.
    e.insert(0,"0")#show zero in the ebox.
    user_inputs=["0","+"]#clear the user_inputs. set to default values.
    myLabel.config(text="0")#update label to default.


def button_backspace():#delete ebox entry letter by letter.
    global user_inputs
    current=str(e.get())#store the current value.
    if user_inputs[-1]=='=':#check whethe = was pressed before pressing backspace this button,
        user_inputs=["0","+","be"]#reset the list to this values.
        myLabel.config(text="0")#update label to zero.
        current=str(e.get())
        e.delete(0,END)
        e.insert(0,current)
    elif user_inputs[-1] =="be":# if you pressed = befor pressing backspace button, then...
        current=str(e.get())
        e.delete(0,END)
        e.insert(0,current)

    elif user_inputs[-1]=="b":#if backspace pressed just before this..
        if len(current)== 1:#if its a single digit number.
            e.delete(0,END)#clear the ebox.
            e.insert(0,"0")#show zero in the ebox.
            user_inputs.append("b")
        else:#if its not a single digit number then..
            e.delete(0,END)#clear the ebox.
            e.insert(0,current[:-1])#remove the last value from given number.
            user_inputs.append("b")
        user_inputs[-1]="b"
    elif len(current)== 1:#if its a single digit number.
        e.delete(0,END)#clear the ebox.
        e.insert(0,"0")#show zero in the ebox.
        user_inputs.append("b")
    else:
        e.delete(0,END)#clear the ebox.
        e.insert(0,current[:-1])#show zero in the ebox.
        user_inputs.append("b")


e = Entry(root,width=35,borderwidth=2)
e.insert(0,"0")

button_0=Button(root,text="0",padx=88,pady=20,command=lambda:button_click(0,user_inputs))
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1,user_inputs))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2,user_inputs))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3,user_inputs))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4,user_inputs))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5,user_inputs))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6,user_inputs))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7,user_inputs))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8,user_inputs))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9,user_inputs))

button_add_=Button(root,text="+",padx=40,pady=20,command=lambda:button_add(user_inputs))
button_sub_=Button(root,text="-",padx=40,pady=20,command=lambda:button_sub(user_inputs))
button_mul_=Button(root,text="*",padx=40,pady=20,command=lambda:button_mul(user_inputs))
button_div_=Button(root,text="/",padx=41,pady=20,command=lambda:button_div(user_inputs))
button_equal_=Button(root,text="=",padx=88,pady=20,command=lambda:button_equal(user_inputs))
button_clear_=Button(root,text="C",padx=88,pady=20,command=button_clear)
button_backspace_=Button(root,text="B",padx=40,pady=20,command=button_backspace)

myLabel.grid(row=0,column=0,columnspan=4)
e.grid(row=1,column=0,columnspan=4,padx=3,pady=10)

button_0.grid(row=6,column=0,columnspan=2)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_add_.grid(row=5,column=3)
button_sub_.grid(row=4,column=3)
button_mul_.grid(row=3,column=3)
button_div_.grid(row=2,column=3)

button_equal_.grid(row=6,column=2,columnspan=2)
button_clear_.grid(row=2,column=0,columnspan=2)
button_backspace_.grid(row=2,column=2)

root.mainloop()
