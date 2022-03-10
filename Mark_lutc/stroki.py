"""
Методы строк
"""

s = 'abcd'
# Поиск потстроки "b"  start with 1  finish 4, if not find return -1
s.find('b', 1, 4)

"""
Замена символа "b" -> XUZ
s.replace('b', 'XUZ')
Out[35]: 'aXUZcd'

"""

"""
Разбивает строку на по разделителю
s.split('b')
Out[41]: ['a', 'cd']
"""

"""
Преобразовывает в верхний регистр
In [43]: s.upper()
Out[43]: 'ABCD'

"""

"""
удаляет завершающие пробелы
s1
Out[49]: 'abcd\n'

In [50]: s1.rstrip()
Out[50]: 'abcd'


"""

"""
Форматирование строк
In [53]: " %s first %s second" %(5, 'qqqqqqqq')
Out[53]: ' 5 first qqqqqqqq second'

"""

"""
Форматирование строк
In [56]: "{0} formatter{1}".format('first', 5)
Out[56]: 'first formatter5'

"""
"""
'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isascii',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill'
"""


