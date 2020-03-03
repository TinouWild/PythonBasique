import re

string = "5e1f11522a0ebb00238d4095win64"
if re.search("win32", string):
    is_win32 = True
    kit_id = re.split("win32", string)[0]
else:
    is_win32 = False
    kit_id = re.split("win64", string)[0]

print("Win32 : {0}, KitId : {1}".format(is_win32, kit_id))
