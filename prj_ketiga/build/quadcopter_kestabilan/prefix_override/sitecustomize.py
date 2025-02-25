import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/phasya/quadcopter/prj_ketiga/install/quadcopter_kestabilan'
