import datetime
import pytz  

class Greeter:
    def greet(self, name):
        
        # Recorta la entrada
        trimmed_name = name.strip()

        # Pone en mayúscula la primera letra del nombre
        formatted_name = trimmed_name.capitalize()

        # Define la zona horaria de Honduras (UTC-6)
        honduras_timezone = pytz.timezone("America/Tegucigalpa")

        # Obtiene la hora actual en la zona horaria de Honduras
        current_time = datetime.datetime.now(honduras_timezone).time()

        # Determina el saludo según la hora del día
        if datetime.time(6, 0) <= current_time < datetime.time(12, 0):
            greeting = "Buenos días"
        elif datetime.time(18, 0) <= current_time < datetime.time(22, 0):
            greeting = "Buenas noches"
        else:
            greeting = "Buenas noches"

        # Construye el mensaje final
        message = f"{greeting}, {formatted_name}"

        # Inicia sesión en la consola
        self.log_to_console(message)

        # Retorna el mensaje
        return message

    def log_to_console(self, message):
        # Simula iniciar sesión en la consola
        print("Iniciando sesión en la consola...")
        print(message)

# Ejemplo de uso
greeter = Greeter()
greeter.greet("rubi")