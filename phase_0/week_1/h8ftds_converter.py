def celcius(nilai_suhu_kelvin):
    celcius = nilai_suhu_kelvin  + 273.15
    return celcius

def kelvin(nilai_suhu_celcius):
    kelvin = nilai_suhu_celcius - 273.15
    return kelvin

def farenheit(nilai_suhu_kf):
    farenheit = (nilai_suhu_kf*1.8) - 459.67
    return farenheit

def farenheit1(nilai_suhu_cf):
    farenheit1 = (nilai_suhu_cf*1.8) + 32
    return farenheit1

def kelvin1(nilai_suhu_fk):
    kelvin1 = (nilai_suhu_fk + 459.97) / 1.8
    return kelvin1

def celcius1 (nilai_suhu_fc):
    celcius1 =(nilai_suhu_fc - 32) / 1.8
    return celcius1
    
def konversi(nilai_suhu_kelvin):
    print("Hasil Celcius", celcius(nilai_suhu_kelvin),"K")
def konversi1(nilai_suhu_celcius):
    print("Hasil Kelvin",kelvin(nilai_suhu_celcius), "C")
def konversi2 (nilai_suhu_kf) :
    print("Hasil Kelvin - Farenheit",farenheit(nilai_suhu_kf), "F")
def konversi3 (nilai_suhu_cf) :
    print("Hasil Celcius - Farenheit",farenheit1(nilai_suhu_cf), "F")
def konversi4 (nilai_suhu_fk) :
    print("Hasil Farenheit - Kelvin",kelvin1(nilai_suhu_fk), "K")
def konversi5 (nilai_suhu_fv) :
    print("Hasil Farenheit - Celcius",celcius1(nilai_suhu_fc), "C")


nilai_suhu_kelvin = int(input("Masukan Nilai Suhu C ="))
nilai_suhu_celcius= int(input("Masukan Nilai Suhu K ="))
nilai_suhu_kf = int(input("Masukan Nilai Suhu K - F ="))
nilai_suhu_cf= int(input("Masukan Nilai Suhu C - F ="))
nilai_suhu_fk= int(input("Masukan Nilai Suhu F - K ="))
nilai_suhu_fc= int(input("Masukan Nilai Suhu F - C ="))


print("*"*50)

konversi(nilai_suhu_kelvin)
print ("="*50)
konversi1(nilai_suhu_celcius)
print("="*50)
konversi2(nilai_suhu_kf)
print("="*50)
konversi3(nilai_suhu_cf)
print("="*50)
konversi4(nilai_suhu_fk)
print("="*50)
konversi5(nilai_suhu_fc)
