from datetime import datetime
from pyfiglet import Figlet
from termcolor import colored
import time
from matplotlib import pyplot as plt
import plotext as plt

def calcular_edad(day, month, year):
    time_actual = datetime.now()
    year_actual = time_actual.year
    month_actual = time_actual.month
    day_actual = time_actual.day
    days = 0
    if day > day_actual:
        days = (day + 30) - day_actual
        month -= 1
    elif day < day_actual:
        days = day_actual - day
    if month > month_actual:
        days += (month_actual - month) * 30
        year_actual -= 1
    birth_date = datetime(year, month, day)
    time_difference = time_actual - birth_date
    days += time_difference.days
    return days

def print_results(days):
    # calculo de la edad
    print(f"Tienes {colored(days // 365, 'red')} años de edad.")
    # grafiquito de la vida restante.
    calcular_porcentaje_vida_transcurrido(days)
    # calculos de dias, horas, minutos y segundos.
    print(f"Has vivido {colored(days, 'red')} dias.")
    print(f"Has vivido {colored(days * 24, 'red')} horas.")
    print(f"Has vivido {colored(days * 24 * 60, 'red')} minutos.")    
    print(f"Has vivido {colored(days * 24 * 60 * 60, 'red')} segundos.")
    # calculos curiosillos
    banio =  (days * 15) // (60 * 24)
    print(f"Te has pasado {colored(banio, 'red')} dias sentado en el inodoro cagando.")
    ducha = (days * 30) // (60 * 24)
    print(f"Te has pasado {colored(ducha, 'red')} dias duchandote.")
    print(f"Te has cortado las uñas {colored(days // 7, 'red')} veces.")
    respiraciones = (days * 60)*15
    print(f"Has hecho {colored(respiraciones, 'red')} respiraciones.")
    pasos = days * 9000
    print(f"Has hecho {colored(pasos, 'red')} pasos.")
    latidos = days * 100000
    print(f"Tu corazon a latido {colored(latidos, 'red')} veces.")
    dormir = (days * 8) // (24)
    print(f"Te has pasado {colored(dormir, 'red')} dias durmiendo.")

#GRAFICOS
# Dias
    variables = ["Vivido", "Poop", "Duchandote", "Durmiendo"]
    values = [int(days), int(banio), int(ducha), int(dormir)]
    plt.simple_bar(variables,values, width = 100, title="Dias vividos contra dias gastados en:")
    plt.show()
# Datos random
    variables_random = ["Respiraste", "Te latio el corazon", "Hiciste un paso"]
    val = [int(respiraciones), int(latidos), int(pasos)]
    plt.simple_bar(variables_random, val, width = 100, title="Veces que:")
    plt.show()


def contacto():
    print(colored("Contact me \n Email: joaquin.lisotti@gmail.com \n Linkedin: Joaquin Lisotti \n Github: Joaco Lisotti",'blue'))

def menu():
    print(colored("╔===================╦========================================╗",'green'))
    print(colored("║To try the program ║ type RUN.                              ║",'green'))
    print(colored("║===================╬========================================║",'green'))
    print(colored("║To contact me      ║ type CONTACT.                          ║",'green'))
    print(colored("║===================╬========================================║",'green'))
    print(colored("║To exit            ║ type EXIT.                             ║",'green'))
    print(colored("╚===================╩========================================╝",'green'))

def run_program():
    nombre = input("¿Cuál es tu nombre? ")
    print("¡Hola,",nombre,"!")
    vivis = input("¿En qué ciudad vives? ")
    print("Oh ", vivis, "es hermoso. ")
    day = int(input("¿Qué día naciste? indica solo el numero del dia en que naciste! "))
    month = int(input("¿En qué mes naciste? indica solo el numero del mes en que naciste "))
    year = int(input("¿En qué año naciste? "))

    days = calcular_edad(day, month, year)
    print_results(days)

def calcular_porcentaje_vida_transcurrido(edad_dias):
    edad_promedio = 28000  # Edad promedio en días

    porcentaje_transcurrido = (edad_dias / edad_promedio) * 100
    porcentaje_restante = 100 - porcentaje_transcurrido

    barra_transcurrido = "█" * int(porcentaje_transcurrido // 2)
    barra_restante = " " * int(porcentaje_restante // 2)

    print("Vida: ", end="")
    for i in range(51):
        barra_actual = barra_transcurrido[:i] + barra_restante[:50 - i]
        porcentaje_actual = (i / 50) * porcentaje_transcurrido

        print("\rProgreso: [{:<50}]".format(barra_actual), end="")
        print("{:.2f}%".format(porcentaje_actual), end="")
        time.sleep(0.05)

    print("\nPorcentaje de vida transcurrido: {:.2f}%".format(porcentaje_transcurrido))
    print("Porcentaje de vida restante: {:.2f}%".format(porcentaje_restante))


def main():
    f = Figlet(font='slant')
    print(colored(f.renderText("Joaquin Lisotti"), 'blue'))
    print(colored("This is a remake of the first program that I made when I was 11 years old. =)", 'blue'))
    print(colored("This program was made as a joke, the results provided are not exact nor do they claim to be.", 'red'))
    while True:
        menu()
        user_input = input().lower()

        if user_input == "run":
            run_program()
        elif user_input == "contact":
            contacto()
        elif user_input == "exit":
            print(colored("Exiting the program...",'red'))
            break
        else:
            print(colored("Invalid input. Please try again.",'red'))
main()