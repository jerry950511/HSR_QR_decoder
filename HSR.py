#取得資料
barcode = input("請輸入你QR CODE的資料: ")
ticket_number = barcode[0:13]
reservation_number = barcode[13:21]
car_number = barcode[24:28]
departure_station = barcode[28:31]
depature_datetime = barcode[31:43]
arrival_station = barcode[45:48]
arrival_datetime = barcode[48:60]
seat_number = barcode[76:84]
price = barcode[90:94]
boarding_date = barcode[110:118]

#設定使輸出結果更易懂
station = ["南港站","台北站","板橋站","桃園站","新竹站","苗栗站","台中站","彰化站","雲林站","嘉義站","台南站","高雄站"]
seat = ["A","B","C","D","E"]
if car_number[0] == "0":
    car_number = car_number[1:]
departure_station = station[int(departure_station)-1]
def amorpm(datetime):
    if int(datetime[8:10]) <= 11:
        return "上午"
    else:
        return "下午"
if amorpm(depature_datetime) == "上午":
    depature_datetime = f"上午{int(depature_datetime[8:10])}點{str(depature_datetime[10:12])}分"
else:
    depature_datetime = f"下午{int(depature_datetime[8:10])-12}點{str(depature_datetime[10:12])}分"

if amorpm(arrival_datetime) == "上午":
    arrival_datetime = f"上午{int(arrival_datetime[8:10])}點{str(arrival_datetime[10:12])}分"
else:
    arrival_datetime = f"下午{int(arrival_datetime[8:10])-12}點{str(arrival_datetime[10:12])}分"

arrival_station = station[int(arrival_station)-1]
seat_number = f"{int(seat_number[0:2])}車{int(seat_number[2:5])}號{seat[int(seat_number[5:])-1]}"
price = str(int(price))+"元"
boarding_date = f"{str(boarding_date[0:4])}年{str(boarding_date[4:6])}月{str(boarding_date[6:8])}日"

#印出
import os
os.system("clear")
print("票號:",ticket_number)
print("訂位代號:",reservation_number)
print("車次: ",car_number)
print("搭乘日期:",boarding_date)
print("上車站: ",departure_station)
print("上車時間:",depature_datetime)
print("下車站:",arrival_station)
print("下車時間:",arrival_datetime)
print("座位:",seat_number)
print("票面金額:",price)