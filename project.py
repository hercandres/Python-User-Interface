# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:01:00 2025

@author: Personal
"""
import statistics as stat
import matplotlib.pyplot as plt

def number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def remove_empty(data_set):
    f = open(data_set, "r")
    
    lines = [l for l in f.readlines() if l.strip() != ""]
    f.close()

    f = open(data_set, "w")
    for l in lines:
        f.write(l)
    f.close()


def delete_strings(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    header = lines[0].strip().split(",")
    rows   = [l.strip().split(",") for l in lines[1:]]

    keep = [0]
    for col in range(1, len(header)):
        for r in rows:
            if col < len(r) and (number(r[col]) or r[col] == "-"):
                keep.append(col)
                break

    new_header = [header[i] for i in keep]
    cleaned_lines = [",".join(new_header)]

    for r in rows:
        cleaned_row = []
        for i in keep:
            cleaned_row.append(r[i] if i < len(r) else "")
        cleaned_lines.append(",".join(cleaned_row))

    f = open(path, "w")
    for l in cleaned_lines:
        f.write(l + "\n")
    f.close()

def side_negative(data_set):
    f = open(data_set, "r")
    lines = f.readlines()
    f.close()

    out = []
    for line in lines:
        cells = line.strip().split(",")
        new_cells = []
        for cell in cells:
            cell = cell.strip()
            if " " in cell:
                part = cell.split(" ")
                if len(part) == 2 and part[0].replace(".", "", 1).isdigit():
                    num = float(part[0])
                    if part[1].upper() == "L":
                        num = -num
                    cell = str(num)
            new_cells.append(cell)
        out.append(",".join(new_cells))

    f = open(data_set, "w")
    for l in out:
        f.write(l + "\n")
    f.close()

def clean_data(data_set):
    remove_empty(data_set)
    delete_strings(data_set)
    side_negative(data_set)

def get_data(data_set):
    data = []
    with open(data_set, "r") as f:
        lines = f.read().split("\n")
    for line in lines:
        fields = line.split(",")
        data.append(fields)
    return data

def headers(data_set):
    datos = get_data(data_set)
    headers = datos[0]
    return headers

def clubs(data_set):
    clubs = []
    datos = get_data(data_set)
    for row in range(1, len(datos)):
        club = datos[row][0]
        if club and club not in clubs: 
            clubs.append(club)
    return clubs

def average(data_set, club, position):
    value = 0.0
    divide = 0
    datos = get_data(data_set)
    for rep in range(1, len(datos)):
        if str(datos[rep][0]) == str(club) and datos[rep][position] != "-":
            record = datos[rep][position]
            value += float(record)
            divide +=1
        
    average = value / divide
    average = average * 10000
    average = (average // 10) / 1000

    return average

def stdev(data_set,club,position):
    lista = []
    datos = get_data(data_set)
    for rep in range(1,len(datos)):
        if datos[rep][0] == club:
            if datos[rep][position] != "-":
                lista.append(float(datos[rep][position]))
    if len(lista)>2:
        stdev = stat.stdev(lista)
        stdev = stdev*10000
        stdev = (stdev//10)/100
    else:
        stdev = "Not enought information to calculate STDEV"
    return stdev


def data_summary(data_set):
    data = get_data(data_set)
    club = clubs(data_set)
    retorno = [headers(data_set)]
    for palo in range(0,len(club)):
        """print(club[palo])"""
        temp = [club[palo]]
        for value in range(1,len(data[0])):
            """print(data[0][value])"""
            ave = average(data_set,club[palo],value)
            sta = stdev(data_set,club[palo],value)
            """print(ave)"""
            """print(sta)"""
            tupla = [ave,sta]
            temp.append(tupla)
            
        retorno.append(temp)
        """print(retorno)"""
    return retorno

def buildtxtfile(data_set):
    with open("summary.txt", "w") as f:
        title = "Golf Data Summary\n"
        description = "This file stores the average and standard deviation of every variable recorded\n"
        divide = "-----------------------------------------------------------------------------\n"
        small_divide = "----------\n"
        f.write(title)
        f.write(description)
        f.write(divide)

        lista = data_summary(data_set)

        for x in range(1, len(lista)):
            f.write("Club: " + str(lista[x][0]) + "\n")
            for y in range(1, len(lista[0])):          # use header length
                f.write("Variable: " + str(lista[0][y]) + "\n")
                f.write("Average: " + str(lista[x][y][0]) + "\n")
                f.write("Standard Deviation: " + str(lista[x][y][1]) + "\n")
                f.write(small_divide)
            f.write(divide)
    return None

def get_variable(data_set, position):
    data = data_summary(data_set)
    variable = []
    for x in range(1,len(data)):
        variable.append(data[x][position][0])
    return variable

def display_headers(data_set):
    print("After cleaning process, this are your stored variables:")
    header = headers(data_set)
    position = 0
    message = ""
    for variable in range(0,len(header)):
        message = str(position) + ".  " + str(header[variable]) 
        position +=1
        print(message)
    return None

def data_progress_plot(data_set,position):
    y = get_variable(data_set, position)
    x = clubs(data_set)
    header = headers(data_set)
    fig, ax = plt.subplots() 
    ax.plot(x, y, marker="o", linewidth=2) 
    
    ax.set_xlabel("Club")
    ax.set_ylabel(header[position])
    ax.set_title(str(header[position]) + " Progression Line")
    
    plt.show()
    return None

def compare_values(data_set,position1, position2):
    y = get_variable(data_set, position1)
    x = get_variable(data_set, position2)
    header = headers(data_set)
    fig, ax = plt.subplots() 
    ax.plot(x, y, marker="o", linewidth=0) 
        
    ax.set_ylabel(str(header[position1]))
    ax.set_xlabel(header[position2])
    ax.set_title(str(header[position1]) + " and " + str(header[position2]) + " Relation")
    
    plt.show()
    return None
    
def init():
    print("Welcome to your data visualization App!\n")
    print("Here you can input your data set, make sure the first column works as group identifier for your information.")
    x = True
    while x == True:
        data_set = str(input("Please enter the name of your data set (csv): "))
        file = data_set.split(".")
        if file[1] =="csv":
            x = False
        else:
            print("Make sure your file is a CSV file")

    clean_data(data_set)
    buildtxtfile(data_set)
    
    y = True
    
    while y == True:
        display_headers(data_set)
        w = True
        while w == True:
            print("Please select an Option\n")
            print("1. Visualize a variable progress throughout your bag")
            print("2. Compare variables")
            response = str(input("Type 1 or 2: "))
            if response != "1" and response !="2":
                print("Invalid response, please type 1 or 2")
            else:
                w = False
        
        q = True
        if response == "1":
            while q == True:
                e = str(input("Please enter the variable that you wish to visualize: "))
                print("0 is not accepted as a value of entry")
                display_headers(data_set)
                if int(e) > 0 and int(e) < 13:
                    e = int(e)
                    data_progress_plot(data_set, e)
                    q = False
                else: 
                    print("Entered value is not valid, try again")
        else:
            while q == True:
                e = str(input("Please enter the first variable that you wish to compare: "))
                u = str(input("Please enter the first variable that you wish to compare: "))
                print("0 is not accepted as a value of entry")
                display_headers(data_set)
                if int(e) > 0 and int(e) < 13 and int(u) > 0 and int(u) < 13:
                    e = int(e)
                    u = int(u)
                    compare_values(data_set, e, u)
                    q = False
                else: 
                    print("Entered value is not valid, try again")
        
        more = str(input("Do you want more information? Type y if YES, anything else for NO\n" ))
        if more =="y":
            continue
        else:
            y = False
    return None
        

init()




