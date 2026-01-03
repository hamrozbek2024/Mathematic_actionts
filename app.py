# 1. SALOM DUNYO
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}! Python dunyosiga xush kelibsiz!")

print("-" * 40)

# 2. YOSHNI HISOBLASH
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2026 - t_yil
print(f"Siz {yosh} yoshdasiz")

print("-" * 40)

# 3. JUFT YOKI TOQ
son = int(input("Raqam kiriting: "))
if son % 2 == 0:
    print("Bu juft son")
else:
    print("Bu toq son")

print("-" * 40)

# 4. ENG KATTA RAQAM
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
print("Eng katta raqam:", max(a, b, c))

print("-" * 40)

# 5. HARORAT KONVERTORI
tanlov = input("C dan F ga o'tkazish uchun 'C', F dan C ga o'tkazish uchun 'F' ni kiriting: ")

if tanlov.upper() == 'C':
    c = float(input("Selsiy kiriting: "))
    f = (c * 9 / 5) + 32
    print("Farengeyt:", f)
elif tanlov.upper() == 'F':
    f = float(input("Farengeyt kiriting: "))
    c = (f - 32) * 5 / 9
    print("Selsiy:", c)
else:
    print("Noto'g'ri tanlov")

print("-" * 40)

# 6. FAKTORIAL HISOBLAGICH
n = int(input("Son kiriting (faktorial uchun): "))
fakt = 1
for i in range(1, n + 1):
    fakt *= i
print("Faktorial:", fakt)

print("-" * 40)

# 7. TESKARI MATN
matn = input("Matn kiriting: ")
print("Teskari matn:", matn[::-1])

print("-" * 40)

# 8. UNLI HARFLAR SANAQI
matn2 = input("Matn kiriting (unlilarni sanash): ")
unlilar = "aeiouAEIOU"
sanoq = 0

for harf in matn2:
    if harf in unlilar:
        sanoq += 1

print("Unli harflar soni:", sanoq)

print("-" * 40)

# 9. AMALLAR KALKULYATORI
x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == '+':
    print("Natija:", x + y)
elif amal == '-':
    print("Natija:", x - y)
elif amal == '*':
    print("Natija:", x * y)
elif amal == '/':
    print("Natija:", x / y)
else:
    print("Noto'g'ri amal")

print("-" * 40)

# 10. PALINDROM TEKSHIRUVCHI
soz = input("So'z kiriting: ")
if soz == soz[::-1]:
    print("Bu palindrom")
else:
    print("Bu palindrom emas")
