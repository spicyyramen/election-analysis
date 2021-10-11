#sets temperature to be what the user inputs to the question, sets input as integer
temperature = int(input("What is the temperature outside? "))
#if temperature is greater than 80, print turn on the AC
if temperature >80:
    print("turn on the AC.")
#if temperature is less than 80 print open the windows
else:
    print("Open the windows.")

