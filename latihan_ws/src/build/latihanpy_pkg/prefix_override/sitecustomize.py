import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/phasya/LW/latihan_ws/src/install/latihanpy_pkg'
