# from modules import module_2
# print(module_2)

# <module 'modules.module_2'
# from 'G:\\pyton\\lesson_md_4_5\\module_4_1\\modules\\module_2.py'>
# ______________________________________

# from modules.module_2 import  some_func
# print(some_func)

# <function some_func at 0x00000277CA738CC0>

import modules
from modules import module_2

print(module_2)
# Я в ините в пакете модульс
# Я из второго модуля
# Я из второго модуля
#   4           0 RESUME                   0
#
#   5           2 LOAD_CONST               1 ('Я из второго модуля')
#               4 STORE_FAST               0 (a)
#
#   6           6 LOAD_GLOBAL              1 (NULL + print)
#              16 LOAD_CONST               1 ('Я из второго модуля')
#              18 CALL                     1
#              26 POP_TOP
#
#   7          28 LOAD_FAST                0 (a)
#              30 RETURN_VALUE
# <module 'modules.module_2' from 'G:\\pyton\\lesson_md_4_5\\module_4_1\\modules\\module_2.py'>

