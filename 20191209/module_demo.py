"""

简单使用module

Version:1.0
Author:chaishuai

"""

from module1 import say
say()

from module2 import say
say()

import module1
module1.say()

import module2
module2.say()

from module1 import say
from module2 import say
# 注意后面的会覆盖前面的
say()