#calculate the total of a given list of a specific format.
#example of a list accepted by this function: ["0","+","0","10","+","0","20","+"]
#takes in the given list and return the calculated value.
def fn_calculate(list):
    #--format the given list and create new_list for calculation------
    total_of_input=0 #current total
    new_list=[]
    update_list=list[2:len(list)]#remove 1st 2 values.they are there as default values. ie., ignore them for calculation.
    iter_i=0#to count the iterations in below for loop.
    for i in update_list:
        iter_i+=1
        index_of_i=iter_i-1
        #if any of the following conditions are met, do not add that item to new_list. else append to new_list
        if index_of_i==0 or update_list[iter_i-2]=="+" or update_list[iter_i-2]=="-" or update_list[iter_i-2]=="*"or update_list[iter_i-2]=="/" :
            continue
        else:
            new_list.append(i)
    #--do calculations on new_list
    iter_i=0
    for i in new_list:
        iter_i+=1
        index_of_i=iter_i-1#calculate index based on iteration
        if iter_i == 1:#if i is the first value of the list do this
            total_of_input= float(i)
        elif iter_i == len(new_list):#if i is the last value skip. last value will be a math symbol.
            continue
        else:
            if i == "+":
                total_of_input+=float(new_list[index_of_i+1])
            if i == "-":
                total_of_input-=float(new_list[index_of_i+1])
            if i == "*":
                total_of_input*=float(new_list[index_of_i+1])
            if i == "/":
                total_of_input/=float(new_list[index_of_i+1])
    if total_of_input - int(total_of_input) == 0:#check whether the number is a whole number or not.
        return int(total_of_input)#if whole number return without decimal values.
    else:#if float return with decimal. max decimal points set to 10
        total_of_input = round(total_of_input,10)
        return total_of_input


#update a given list of a specific format, remove unneeded stuff. this is used for updating the label widget.
#example of a list accepted by this function: ["0","+","0","10","+","0","20","+"]
#takes in the given list and return a new_list with unneccessory values removed.
#in the above example it will return: ["10","+","20","+"]
def update_list(list):
    new_list=[]
    update_list=list[2:len(list)]##remove 1st 2 values.they are there as default values. ie., ignore them for calculation.
    iter_i=0#to count the iterations in next loop
    for i in update_list:
        iter_i+=1#count increment
        index_of_i=iter_i-1
        #if any of the following conditions are met, do not add that item to new_list. else append to new_list
        if index_of_i==0 or update_list[iter_i-2]=="+" or update_list[iter_i-2]=="-" or update_list[iter_i-2]=="*"or update_list[iter_i-2]=="/" :
            continue
        else:
            new_list.append(i)
    return new_list
