from netmiko import ConnectHandler

# Dictionnaire des appareils
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

# Fonction pour se connecter et exécuter une commande
def check_device(device_name, device_info):
    print(f"\n=== Connexion à {device_name} ({device_info['ip']}) ===")
    
    # Ici tu définis le dictionnaire Netmiko
    netmiko_params = {
        "device_type": "cisco_ios",  # tous nos devices sont Cisco ici
        "host": device_info["ip"],
        "username": "admin",         # mettre le vrai user
        "password": "admin123",      # mettre le vrai password
        "secret": "enab"
        "le123",       # si mode enable requis
    }
    
    # Simulation (décommenter pour connexion réelle)
    # try:
    #     net_connect = ConnectHandler(**netmiko_params)
    #     net_connect.enable()  # si nécessaire
    #     output = net_connect.send_command("show ip interface brief")
    #     print(output)
    #     net_connect.disconnect()
    # except Exception as e:
    #     print(f"Erreur de connexion à {device_name}: {e}")
    
    # Comme simulation, on affiche juste les infos
    print(f"Device info: Vendor={device_info['vendor']}, Model={device_info['model']}, IOS={device_info['ios']}")

# Parcours de tous les appareils
for name, info in london_co.items():
    check_device(name, info)