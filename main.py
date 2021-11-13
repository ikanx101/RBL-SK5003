lagi = "y"

while lagi == "y" or lagi == "Y":
  exec(open("program.py").read())
  lagi = input("Coba lagi? (y/n) \n")

print("\n\n")
print("==== Terima kasih ====")
