import datetime
import babel.dates

diena = int(input("Ievadi datumu"))
menesis = int(input("Ievadi mēnesi!"))
gads = int(input("Ievadi gadu!"))

datums = datetime.date(gads, menesis, diena)
datums_lv = babel.dates.format_date(datums, locale='lv')

print(datums_lv)
dienasNos = datums.strftime("%A")

dienas_en = babel.dates.get_day_names(locale='en')
for each in dienas_en:
  if dienasNos == dienas_en[each]:
    print(babel.dates.get_day_names(locale='lv')[each])