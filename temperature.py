kinds = input('請問您輸入的為攝氏還是華氏：')

if kinds == '攝氏' :
    temper = input('請輸入溫度：')
    temper = float(temper)
    temper = temper * 9 / 5 + 32
    print('華氏溫度為',temper,'度')
elif kinds == '華氏' :
    temper = input('請輸入溫度：')
    temper = float(temper)
    temper = (temper - 32 ) * 5 / 9
    print('攝氏溫度為',temper,'度')
else :
    print('請輸入攝氏或是華氏')