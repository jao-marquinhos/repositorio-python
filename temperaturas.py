def menuTemperaturas():
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Celsius")
    print("6. Converter de Kelvin para Fahrenheit")
    print("7. Encerrar programa")
    select = int(input("Escolha uma opção: "))
    return select


while True:
    select = menuTemperaturas()

    if select == 1:
        celsius = float(input("Qual o valor de Celsius? "))
        fahrenheit = celsius * (9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit}°F\n")
               
    elif select == 2:
        celsius = float(input("Qual o valor de Celsius? "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C é igual a {kelvin}°K\n")
    
    elif select == 3:
        fahrenheit = float(input("Qual o valor de Fahrenheit? "))
        celsius = (fahrenheit - 32) * (5/9)
        print(f"{fahrenheit}°F é igual a {celsius}°C\n")
        
    elif select == 4:
        fahrenheit = float(input("Qual o valor de Fahrenheit? "))
        kelvin = (fahrenheit - 32) * (5/9) + 273.15
        print(f"{fahrenheit}°F é igual a {kelvin}°K\n")
        
    elif select == 5:
        kelvin = float(input("Qual o valor de Kelvin? "))
        celsius = kelvin - 273.15
        print(f"{kelvin}°K é igual a {celsius}°C\n")
        
    elif select == 6:
        kelvin = float(input("Qual o valor de Kelvin? "))
        fahrenheit = (kelvin - 273.15) * (9/5) + 32
        print(f"{kelvin}°K é igual a {fahrenheit}°F\n")
    
    elif select == 7:
        print("Encerrando programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
