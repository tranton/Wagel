from guizero import App, Box, Text, TextBox, Picture, PushButton, ButtonGroup, info

# Chi so luong co so va luong toi thieu vung
Luong_Co_So_2021 = 1490000  # 1,490,000
Luong_Toi_Thieu_Vung_1 = 4420000  # 4,420,000
Luong_Toi_Thieu_Vung_2 = 3920000  # 3,920,000
Luong_Toi_Thieu_Vung_3 = 3430000  # 3,430,000
GTGC = 11000000
GTNPT = 4400000

# Muc dong bao hiem xa hoi, bao hiem y te, bao hiem that nghiep
BHXH = 0.08
BHYT = 0.015
BHTN = 0.01


def Gross_To_Net():
    Gross_Salary = int(User_Input_Salary_Gross.value)
    Luong_Co_So_2021_Toithieu = Luong_Co_So_2021*20
    LTTV = int(Luong_Toi_Thieu_Vung_Options.value)
    SNPT = int(So_Nguoi_Phu_Thuoc_Options.value)

    if LTTV == 1:
        Luong_Toi_Thieu_Vung = Luong_Toi_Thieu_Vung_1
    elif LTTV == 2:
        Luong_Toi_Thieu_Vung = Luong_Toi_Thieu_Vung_2
    elif LTTV == 3:
        Luong_Toi_Thieu_Vung = Luong_Toi_Thieu_Vung_3
    else:
        print('Can not specify LTTV')

    # Tinh Luong Dong BHXH, BHYT, BHTN

    if Gross_Salary <= Luong_Co_So_2021_Toithieu:
        Luong_Dong_BHXH = Gross_Salary * BHXH
        Luong_Dong_BHYT = Gross_Salary * BHYT
        Luong_Dong_BHTN = Gross_Salary * BHTN
    else:
        Luong_Dong_BHXH = Luong_Co_So_2021*20*BHXH
        Luong_Dong_BHYT = Luong_Co_So_2021*20*BHYT
        Luong_Dong_BHTN = Luong_Toi_Thieu_Vung*20*BHTN

    print("Bao Hiem Xa Hoi:", Luong_Dong_BHXH)
    print("Bao Hiem Y Te:", Luong_Dong_BHYT)
    print("Bao Hiem That Nghiep:", Luong_Dong_BHTN)
    TNTT = (Gross_Salary - (Luong_Dong_BHXH +
            Luong_Dong_BHYT + Luong_Dong_BHTN) - GTGC - (SNPT*GTNPT))
    print("Thu Nhap Tinh Thue: ", TNTT)

    if TNTT <= 5000000:
        Thue_TNCN = TNTT*0.05
    elif TNTT <= 10000000:
        Thue_TNCN = TNTT*0.1 - 250000
    elif TNTT <= 18000000:
        Thue_TNCN = TNTT*0.15 - 750000
    elif TNTT <= 32000000:
        Thue_TNCN = TNTT*0.20 - 1650000
    elif TNTT <= 52000000:
        Thue_TNCN = TNTT*0.25 - 3250000
    elif TNTT <= 80000000:
        Thue_TNCN = TNTT*0.30 - 5850000
    else:
        Thue_TNCN = TNTT*0.35 - 9850000

    print("Thue Thu Nhap Ca Nhan: ", Thue_TNCN)

    NET_Salary = Gross_Salary - \
        (Luong_Dong_BHXH + Luong_Dong_BHYT + Luong_Dong_BHTN) - Thue_TNCN

    print("Luong NET: ", NET_Salary, '\n')
    Result_Net_Salary.append(NET_Salary)
    Result_Thue_TNCN.append(Thue_TNCN)
    Result_BHXH.append(Luong_Dong_BHXH)
    Result_BHYT.append(Luong_Dong_BHYT)
    Result_BHTN.append(Luong_Dong_BHTN)
    


app = App(title="Salary Tool", width=500, height=300, layout="grid")
Title_Gross_Salary = Text(
    app, text="Enter your Gross Wages:", grid=[0, 0], align="left")
User_Input_Salary_Gross = TextBox(
    app, width=10, height=1, grid=[1, 0], align="left")
Options_text1 = Text(app, text="Luong Toi Thieu Vung: ",
                     grid=[0, 2], align="left")
Luong_Toi_Thieu_Vung_Options = ButtonGroup(app, options=[["Vung 1", "1"], ["Vung 2", "2"], [
                                           "Vung 3", "3"]], selected="1", horizontal=True, grid=[1, 2], align="left")
Options_text2 = Text(app, text="So nguoi phu thuoc: ",
                     grid=[0, 3], align="left")
So_Nguoi_Phu_Thuoc_Options = ButtonGroup(app, options=[["1", "1"], ["2", "2"], [
    "3", "3"]], selected="1", horizontal=True, grid=[1, 3], align="left")
Submit_Button = PushButton(app, command=Gross_To_Net,
                           text="Submit", grid=[1, 4])
Result_Text = Text(app, text="Your NET Salary is: ", grid=[0, 5], align="left")
Result_Net_Salary = Text(app, "", grid=[1, 5], align="right")
Result_Text = Text(app, text="Thue Thu Nhap Ca Nhan: ", grid=[0, 6], align="left")
Result_Thue_TNCN = Text(app, "", grid=[1, 6], align="right")
Result_Text = Text(app, text="Bao Hiem Xa Hoi: ", grid=[0, 7], align="left")
Result_BHXH = Text(app, "", grid=[1, 7], align="right")
Result_Text = Text(app, text="Bao Hiem Y Te: ", grid=[0, 8], align="left")
Result_BHYT = Text(app, "", grid=[1, 8], align="right")
Result_Text = Text(app, text="Bao Hiem That Nghiep: ", grid=[0, 9], align="left")
Result_BHTN = Text(app, "", grid=[1, 9], align="right")


app.display()
