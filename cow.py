from cattle.util import Cattle
import cattle.tools as tools

myCattle = Cattle('./movements.csv', './attributes.csv')

output_f = tools.f(myCattle, dir_to_save='./output/')
