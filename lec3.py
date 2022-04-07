from zeep import Client
client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
for service in client.wsdl.services.values():
    print("Сервис:", service.name)
    for port in service.ports.values():
        for operation in port.binding._operations.values():
            print("Метод:", operation.name)
            print("  параметр:", operation.input.signature())

result = client.service.Add(intA=2, intB=3)
print(result)