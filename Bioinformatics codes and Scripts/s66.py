strA = '''BCL2A1
CCL20
CD274
ENO3
BCL2A1
F2RL1
FABP5
KLHL29
NAMPT
BCL2A1
S100A12
SGMS2
TM4SF1
XIST'''
listA = strA.splitlines(); print(listA); print(len(listA))
listF = list(set(listA)); listF.sort(); print(listF); print(len(listF))