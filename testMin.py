print("DEBUT")

devices = {"r1": {"ip": "1.1.1.1"}}

def f(n, i):
    print(n, i["ip"])

for n, i in devices.items():
    f(n, i)

print("FIN")
