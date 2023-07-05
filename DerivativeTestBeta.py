import numpy as np
import originpro as op
import sys


# properly origin exit script
def origin_shutdown_exception_hook(exctype, value, traceback):
    op.exit()
    sys.__excepthook__(exctype, value, traceback)


if op and op.oext:
    sys.excepthook = origin_shutdown_exception_hook

# code
x = [i for i in range(-2000, 2001)]
y = [i ** 2 for i in x]

dydx = np.gradient(y, x)

op.new()
wks = op.new_sheet('w')
wks.from_list(0, x, '', '', '', 'X')
wks.from_list(1, y, '', '', '', 'Y')
wks.from_list(2, x, 'derivative x', '', '', 'X')
wks.from_list(3, dydx, 'derivative y', '', '', 'Y')

# edit it
op.save('D:\Develop\Pyscript\example.opju')


# origin exit
if op.oext:
    op.exit()
