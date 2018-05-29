# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 阳历平年365(1-12月分别为31天，28天，31天，30天，31天，30天，31天，31天，30天，31天，30天，31天)。
# 闰年共有366天(1-12月分别为31天，29天，31天，30天，31天，30天，31天，31天，30天，31天，30天，31天)。
run_year={}
year1=[1,3,5,7,8,10,12]
year2=[4,6,9,11]
for year in year1:
    run_year[year]='31'
for year in year2:
    run_year[year]='30'
# nyr=input("请输入年月日，例如20180514:\n")
# str = []
# str.append(nyr)
# year = str[0:3]
# month = str[4:5]
# day = str[6:7]


year=input("输入年:\n")
month=input("输入月:\n")
day=input("输入日:\n")



if int(year) %4==0 and int(year)%10==0 and int(year)%400==0:
    print(year+" 是闰年")
    run_year[2]='29'
else:
    print(year + " 是闰年")
    run_year[2]='28'

for k,v in run_year.items():
    if int(k)==int(month):
        month_day=-int(k)*int(v)
        while(k):
            month_day=month_day+int(k)*int(v)
            k=k-1
day_all=month_day+int(day)
