# =========================
# Simulation Netmiko
# =========================

routers = {
    "rtr1": {
        "f0_ip": "192.168.20.1"
    },
    "rtr2": {
        "f0_ip": "192.168.20.2"
    },
    "rtr3": {
        "f0_ip": "192.168.20.3"
    },
    "rtr4": {
        "f0_ip": None  # IP non fournie dans l'énoncé
    }
}

LOOPBACK_IP = "192.168.20.5"
MASK_24 = "255.255.255.0"
MASK_32 = "255.255.255.255"

USERNAME = "test"
PASSWORD = "test"

for router, data in routers.items():
    print("\n==============================")
    print(f"Connexion simulée à {router}")
    print("==============================")

    print("configure terminal")
    print(f"hostname {router}")

    print(f"username {USERNAME} password {PASSWORD}")
    print("line vty 0 4")
    print(" login local")
    print("exit")

    print("interface fastEthernet0/0")
    if data["f0_ip"]:
        print(f" ip address {data['f0_ip']} {MASK_24}")
    print(" no shutdown")
    print("exit")

    print("interface loopback0")
    print(f" ip address {LOOPBACK_IP} {MASK_32}")
    print("exit")

    print("end")
    print("write memory")

print("\n=== Fin de la simulation Netmiko ===")
