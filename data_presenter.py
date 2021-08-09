import math

open_file = open("./CupcakeInvoices.csv")

total = 0

for line in open_file:
  # print(line)
  line = line.rstrip("\n").split(",")
  # print(line[2])
  print(math.trunc(float(line[3]) * float(line[4]))) #math.trunc() removes any decimals
  total = total + float(line[3]) * float(line[4])
  # print(total)

open_file.close()

open_file = open("./CupcakeInvoices.csv")

total_choc = 0
total_vanilla = 0
total_strawb = 0

for line in open_file:
  line = line.rstrip("\n").split(",")
  if "Chocolate" in line:
    total_choc += 1
  elif "Vanilla" in line:
    total_vanilla += 1
  elif "Strawberry" in line:
    total_strawb += 1

print(total_choc, total_vanilla, total_strawb)