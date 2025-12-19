from netmiko import ConnectHandler

appareil = {
"device_type": "cisco_ios",
"hôte": "192.168.20.1"
"",
"nom d'utilisateur": "test",
"mot de passe": "test",
"secret" : "test"
}

net_connect = ConnectHandler(**device)
net_connect.activer()
sortie = net_connect.send_config_set(liste_de_commandes)
net_connect.déconnecter()
