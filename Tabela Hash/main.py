#Edimilton Ferreira

from chainedhashtable import ChainedHashTable

print("Entrada:")

m = int(input())

repetitions = int(input())

commands = []

for i in range(repetitions):
  commands.append(input())

print("\nSaida:")

table = ChainedHashTable(m)

def commandVerification(command):
  if command[0] == "a":
    table.add(command[4:])

  elif command[0] == "d":
    table.remove(command[4:])

  elif command[0] == "f":
    if table.find(command[5:]) == None: print("no")
    else: print("yes")

  else:
    chain = list(table.check(int(command[6:])))
    chain.reverse()
    for c in chain:
        print(c, end = " ")
    print("")

for command in commands:
  commandVerification(command)