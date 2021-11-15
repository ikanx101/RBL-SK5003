# ========================================
# program yang akan dieksekusi oleh user
# kelompok rbl 2
# 20921003 Winda Wijayasari
# 20921004 Mohammad Rizka Fadhli
# ========================================

# jika user baru pertama kali mengeksekusi
lagi = "y"
while lagi == "y" or lagi == "Y":
  exec(open("program.py").read())
  # ditanyakan jika user hendak mencoba kembali atau tidak?
  lagi = input("Coba lagi? (y/n) \n")

print("\n\n")
print("==== Terima kasih ====")
