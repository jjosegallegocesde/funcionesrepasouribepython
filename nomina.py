RETE_FUENTE = 0.02
SEGURIDAD_SOCIAL = 0.08
empleados = []
empleado = {}
empleado["Id"] = int(input("Ingrese la identificacion del empleado: "))
empleado["Nombre"] = input("Ingrese el nombre: ")
empleado["HorasTrabajadas"] = int(input("Ingrese la horas trabajadas: "))

while empleado["HorasTrabajadas"] > 48:
        print("no puede trabajar tantas horas!!!")
        empleado["HorasTrabajadas"] = int(input("Ingrese la horas trabajadas: "))

empleado["BaseSalarial"] = int(input("Ingrese el valor de la hora: "))
empleado["Novedades"] = input("Ingrese la novedad presentada: ")
empleado["Fotografia"] = input("Pose pa la foto: ")

def calcularSalario(reteFuente, seguridadSocial):
    totalSalario = empleado["HorasTrabajadas"] * empleado["BaseSalarial"]
    print(totalSalario)
    totalRf = totalSalario * reteFuente
    print(totalRf)
    totalSs = totalSalario * seguridadSocial
    print(totalSs)
    totalBruto = totalSalario  - totalRf - totalSs
    print(totalBruto)
    
    print (f"Para el empleado {empleado['Id']} {empleado['Nombre']}, Su salario total es: {totalBruto}")
    
calcularSalario(RETE_FUENTE, SEGURIDAD_SOCIAL)