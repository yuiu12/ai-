class bcolors:
    HEADER = '\033[1;95m'
    OKBLUE = '\033[4;94m'
    OKGREEN = '\033[5;92m'
    WARNING = '\033[7;93m'
    FAIL = '\033[8m'
print(bcolors.OKBLUE + "警告的颜色字体?" )
print(bcolors.HEADER + "警告的颜色字体?" )
print(bcolors.OKGREEN + "警告的颜色字体?")
print(bcolors.FAIL + "警告的颜色字体?"+'\033[0m')
print(bcolors.WARNING + "警告的颜色字体?"+'\033[0m')