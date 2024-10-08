#!/usr/bin/env python3
from dev_aberto.dev_aberto import hello
import os

# Defina a variável de ambiente LANGUAGE para en_US.utf8
# os.environ['LANGUAGE'] = 'en_US.utf8'

import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()
    print(_('Último commit feito em:'), date, _(' por'), name)