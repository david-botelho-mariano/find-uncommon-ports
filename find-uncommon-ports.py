import subprocess

db_portas_incomuns = []

hosts = """google.com
example.com
vulnerable.com.br"""

hosts_array = hosts.split("\n")

for dominio in hosts_array:

  try:

    resultado = subprocess.run(["nmap", dominio], capture_output=True).stdout.decode()
    
    resultado_filtrado = resultado.split("SERVICE")[1].split("Nmap done")[0]

    for porta in resultado_filtrado.split("\n"):          

      if porta.split("/")[0] not in db_portas_incomuns and "open" in porta:

        print(dominio, porta)
        db_portas_incomuns.append(porta.split("/")[0])

  except Exception as erro:      
    pass 
