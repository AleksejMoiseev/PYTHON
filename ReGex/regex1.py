import re
"""
Сервисы для проерки регулярных выражений
"""
s = r'[0-9]'

f = 6
"""
Поместите курсор на регулярное выражение ([0-9]) и нажмите . Появится список предлагаемых намеренных действий,
 доступных в этом контексте:AltEnter
"""
# p = re.compile(r'(?<=[^ё$MuUSТCГя50ЦnДE;9АJ])(?:\**?)(?=[ШП9В9фвфЛ]*/)')
# print(p)
p = re.compile(r'.....')
print(p.findall('Этот текст был разделён на последовательности из 5 символов, и каждая последовательность была выведена в консоль через пробел.'))
# ['Этот ', 'текст', ' был ', 'разде', 'лён н', 'а пос', 'ледов', 'атель', 'ности', ' из 5', ' симв', 'олов,', ' и ка', 'ждая ', 'после', 'доват', 'ельно', 'сть б', 'ыла в', 'ыведе', 'на в ', 'консо', 'ль че', 'рез п', 'робел']

p = re.compile(r'\W\b[а-яА-ЯёЁa-zA-Z]{3}\b ')
print(p.findall('чuЦ  СXI  хЦ[  цМф  D\М  зЗЩ  hNR  ulW  SШН  ЧZЙ  O1Л  у9D  ч7М  |э:  СcT  }9A  Лw?  Yц|  [_Z  IbБ  б ж  GRI  HУН  Йjп  <н_  *O2  oПP  ХgЗ  П$v  ;щ|  [М|  эGР  х^!  +пэ  ЬZ+  ЛЩЫ  iIX  0xР  KЧD  ёыW  О/g  ,CЪ  шБб  и]s  г^О  ^ТY  #х6  z@П  e-ш  Tяз  1tБ  GШz  \хБ  Tци  %ОЭ  5=b  пdО  тъы  Dw*  дПб  уrэ  ХФб  к|Ч  bix  bсщ  Щ\л  /Ё3  MЪZ  +и2  >kЁ  фЬH  #%=  ТОс  0Jз  х/А  D!Q  aA\  Z&П  ;Dg  ЖiД  bцa  jуa  G}о  g)Т  ?ЧQ  ~Гп  ?J"  {xН  нzь  Ш+ч  W\[  cХ7  кJ|  =хM  PKр  .fN  Иfт  <a?  5$U  Е(. '))

p = re.compile(r'\W\b[а-яА-ЯёЁa-zA-Z]{3}\b ')
"""Поиск года"""
p = re.compile(r'\d{3,4}-\d{2}-\d+')

print(p.findall('900-12-'))

"""

"""

p = re.compile(r'[А-Я а-я]{4,}!?')

print(p.findall('Я забыл использовать восклицательный знак в предложении'))
print(p.findall('Нет!')) # Не пройдет 3 буквы только, должно быть не менее 4
print(p.findall('Ждёшь мотивации чтобы начать действовать? Жди дальше.')) # Не пройдет присутсвует буква Ё

p = re.compile(r'^[A-Za-z]+\d*$')
print(p.findall('consid3f')) # Не пройдкт так как после цифры находится буква

#p = re.compile(r'use\Wstrict;?')

p = re.compile(r'[А-ЯA-Z]{2,}?')

p = p.findall(r'АООТ - акционерное общество открытого типа. ЗАО - закрытое акционерное общество. ОАО - открытое акционерное общество.')

# Ленивый квантификатор вернет ['АО1', 'АО1']
p = re.compile(r'[А-Я]{2}\d{1,2}?')
p = p.findall(r'АО13  АО13')

# Жадный квантификатор вернет ['АО1', 'АО1']
p = re.compile(r'[А-Я]{2}\d?')
print(p.findall(r'АО13  АО13'))

# Жадный квантификатор вернет ['АО13', 'АО13']
p = re.compile(r'[А-Я]{2}\d{1,2}')
p = p.findall(r'АО13  АО13')

# Пример для поиска проверки почтового адреса
p = re.compile(r"\w+@\w+\.\w{2,3}")
p = p.findall(r'test@mail.ru')

"""
для тестирования регулярных выражений вам понадобится английский/русский алфавит, цифры, или символы
"""
from string import printable

"""
Группировка шаблонов
"""
# (?#) - скобочное выражение, позволяющее написать комментарий в регулярном выражении:
p = re.compile(r"(?#\w+@\w+\.\w{2,3})")
p = p.findall(r'test@mail.ru')

# (?:) - скобочное выражение, которое группирует регулярное выражение, но не захватывает в его группу.
# (?:\d\w){2} равносильно \d\w\d\w

p = re.compile(r"Tekst(?:\d\w){2}")
p = p.findall(r'Tekst2a3b')
print('группа без захвата захватила только только последние цифры', p)

p = re.compile(r"Tekst(\d\w){2}")
p = p.findall(r'Tekst2222')
print('группа захватила только только последние цифры', p)


# (?=) -Проверяет стоит ли переданное выражение после шаблона. Не захватывает никаких символов.

p = re.compile(r"1(?=92)")
p = p.findall(r'192 3')

print('Проверяем стоит ли единица перед 92', p)

# (?!) -Проверяет НЕ стоит ли переданное выражение перед шаблоном. Не захватывает никаких символов.

p = re.compile(r"1(?!92)")
p = p.findall(r'19 3')
print('Проверяем НЕ стоит ли единица перед 92', p)

# (?<=) -Проверяет стоит ли переданное выражение перед шаблоном. Не захватывает никаких символов.

p = re.compile(r"(?<=92)3")
p = p.findall(r'1923')
print('Проверяем стоит ли цифра после шаблона 92', p)

# (?<!) -Проверяет НЕ стоит ли переданное выражение после шаблона. Не захватывает никаких символов.

p = re.compile(r"(?!=92)3")
p = p.findall(r'193')
print('Проверяем стоит ли цифра после шаблона 92', p)


#  регулярное выражение, которое ищет слово test среди двух цифр, но не захватывает их

p = re.compile(r"(?<=\d)test(?=\d)")
p = p.findall(r'3test8')
print('Проверим, что test между 2 мя цифрами', p)


"""2000
Сервисы для сравнения текстов: https://textcompare.ru/app
"""

"""

Шаблон	Соответствие
\n
Новая строка

.	Любой символ, кроме символа новой строки. Если flags=re.DOTALL - любой символ.
\s	Любой символ пробела, табуляции или новой строки.
\S	Любой символ, кроме пробела, табуляции или новой строки.
\d	Любая цифра. Ищет все цифры: арабские, персидские, индийские, и так далее. Не эквивалентен [0-9]
\D	Любой символ, кроме цифр.
\w	Любая буква, цифра, или _. Шаблон не соответствует выражению [a-zA-Z0-9_]! Буквы используются не только латинские, туда входит множество языков.
\W	Любой символ, кроме букв, цифр, и _.
\b	Промежуток между символом, совпадающим с \w, и символом, не совпадающим с \w в любом порядке.
\B	Промежуток между двумя символами,совпадающими с \w или \W.
\A	Начало всего текста
\Z	Конец всего текста
^	Начало всего текста или начало строчки текста, если flags=re.MULTILINE
$	Конец всего текста или конец строчки текста, если flags=re.MULTILINE
"""

"""
$
r'[A$Z]'  # Ищет символы A,$,Z
r'^text$' # Ищет text между началом и концом строки
r'100\$'  # Ищет 100$
^
r"[^abc]"      # Ищет любой символ, кроме a,b,c
r"^Some text$" # Ищет Some text между началом и концом строки
r"\^"          # Ищет символ ^ 
r"[a^bc]"      # Символ ^ не стоит первым в скобках, поэтому выражение ищет символы a,b,c,^
.
r'[A.Z]'     # Ищет символы A,.,Z
r'text.'     # Ищет text с любым символом, кроме перехода на новую строку
r'1\.000\$'  # Ищет 1.000$
-
r'Как-то так' # Ищет Как-то так
r'[+-]'       # Ищет символы +,-
r'[^-+]'      # Ищет любой символ, кроме +, -
r'[a-z]'      # Ищет все буквы латинского алфавита в нижнем регистре
r'[a\-z]'     # Ищет символы a,-,z
[]
r'[abc]'   # Ищет символы a,b,c
r'\[abc\]' # Ищет [abc]
r'[\[abc\]]' # Ищет символы [,a,b,c,]
Таких уникальных способов применения шаблонов много, сгруппировать их по какому-то признаку сложно, поэтому придётся просто запомнить каждый случай отдельно.

Шаблоны и квадратные скобки
Не все шаблоны в квадратных скобках используются как текстовые символы: 

r'[.]'  # Находит точку

r'[\d]' # То же самое, что и \d
"""


