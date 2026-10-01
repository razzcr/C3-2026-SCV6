#driver license status check

person_age = int(input("Edad del conductor: "))
person_has_driver_license = input("El conductor posee licencia de conducir? Si/No: ").lower() == "si"
valid_driver_license = input("El conductor posee licencia de conducir valida? Si/No: ").lower() == "si"
underage_special_permit = input("El conductor posee permiso especial de conducir? Si/No: ").lower() == "si"

if person_age >= 18 and person_has_driver_license and valid_driver_license:
    permission_status = "Autorizado para conducir"
elif person_age < 18 and underage_special_permit:
    permission_status = "Habilitado para conducir con permiso especial" 
elif underage_special_permit and (person_age < 18 or not valid_driver_license):
    permission_status = "Habilitado para conducir con permiso especial"       
else:
    permission_status = "No esta habilitado para conducir"    

print("-" * 79)
print(f"Estado de Permiso de Conducir: {permission_status}")
print("-" * 79)


