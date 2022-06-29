dias = float(input("Ingrese los días:  "))
horas = float(input("Ingrese las horas:  "))
min = float(input("Ingrese los minutos:  "))
seg = float(input("Ingrese los segundos:  ")) 

num_seg = dias*24*3600 + horas*3600 + min*60 + seg

print("han transcurrido: ", int(num_seg), " segundos.")


