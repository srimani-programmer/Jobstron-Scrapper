from bs4 import BeautifulSoup

string = '''<div class='explanation' id='explain30'>
<div class='exp_tit'>Explanation:</div><br />
<div class='exp_text'>Let original length = x<br />
and original breadth = y.<br />
<strong>Original area = length x breadth = xy</strong><br />
<br />
New length = x/2<br />
New breadth = 3y.<br />
<strong>New area =</strong> (x/2) x 3y = (3/2) xy = <strong>1.5 xy</strong><br />
<br />
Therefore, <strong>%Increase in area =</strong> {(<strong>New area -Original area) /Original area} * 100 %</strong><br />
= {(1.5 xy - xy) / xy} * 100%<br />
= (0.5 xy / xy) * 100%<br />
= 0.5 * 100%<br />
<strong>= 50 %<br />
<br />
Therefore, Percentage increase in area = 50 %</strong></div>
</div>'''

soup = BeautifulSoup(string,'lxml')

ques = soup.find_all('div',class_="explanation")
for i in ques:
    i = i.find_all('div',class_="exp_text")
    print(i)
    for j in i:
        print(j.text.replace('\n',' '))