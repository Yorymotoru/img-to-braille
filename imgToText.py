import PIL
from PIL import Image, ImageDraw
import os

# Таблица символов шрифта Брайля
alf = [
u'\u2800', u'\u2801', u'\u2802', u'\u2803', u'\u2804', u'\u2805', u'\u2806', u'\u2807', 
u'\u2808', u'\u2809', u'\u280A', u'\u280B', u'\u280C', u'\u280D', u'\u280E', u'\u280F', 
u'\u2810', u'\u2811', u'\u2812', u'\u2813', u'\u2814', u'\u2815', u'\u2816', u'\u2817', 
u'\u2818', u'\u2819', u'\u281A', u'\u281B', u'\u281C', u'\u281D', u'\u281E', u'\u281F', 
u'\u2820', u'\u2821', u'\u2822', u'\u2823', u'\u2824', u'\u2825', u'\u2826', u'\u2827', 
u'\u2828', u'\u2829', u'\u282A', u'\u282B', u'\u282C', u'\u282D', u'\u282E', u'\u282F', 
u'\u2830', u'\u2831', u'\u2832', u'\u2833', u'\u2834', u'\u2835', u'\u2836', u'\u2837', 
u'\u2838', u'\u2839', u'\u283A', u'\u283B', u'\u283C', u'\u283D', u'\u283E', u'\u283F', 
u'\u2840', u'\u2841', u'\u2842', u'\u2843', u'\u2844', u'\u2845', u'\u2846', u'\u2847', 
u'\u2848', u'\u2849', u'\u284A', u'\u284B', u'\u284C', u'\u284D', u'\u284E', u'\u284F', 
u'\u2850', u'\u2851', u'\u2852', u'\u2853', u'\u2854', u'\u2855', u'\u2856', u'\u2857', 
u'\u2858', u'\u2859', u'\u285A', u'\u285B', u'\u285C', u'\u285D', u'\u285E', u'\u285F', 
u'\u2860', u'\u2861', u'\u2862', u'\u2863', u'\u2864', u'\u2865', u'\u2866', u'\u2867', 
u'\u2868', u'\u2869', u'\u286A', u'\u286B', u'\u286C', u'\u286D', u'\u286E', u'\u286F', 
u'\u2870', u'\u2871', u'\u2872', u'\u2873', u'\u2874', u'\u2875', u'\u2876', u'\u2877', 
u'\u2878', u'\u2879', u'\u287A', u'\u287B', u'\u287C', u'\u287D', u'\u287E', u'\u287F', 
u'\u2880', u'\u2881', u'\u2882', u'\u2883', u'\u2884', u'\u2885', u'\u2886', u'\u2887', 
u'\u2888', u'\u2889', u'\u288A', u'\u288B', u'\u288C', u'\u288D', u'\u288E', u'\u288F', 
u'\u2890', u'\u2891', u'\u2892', u'\u2893', u'\u2894', u'\u2895', u'\u2896', u'\u2897', 
u'\u2898', u'\u2899', u'\u289A', u'\u289B', u'\u289C', u'\u289D', u'\u289E', u'\u289F', 
u'\u28A0', u'\u28A1', u'\u28A2', u'\u28A3', u'\u28A4', u'\u28A5', u'\u28A6', u'\u28A7', 
u'\u28A8', u'\u28A9', u'\u28AA', u'\u28AB', u'\u28AC', u'\u28AD', u'\u28AE', u'\u28AF', 
u'\u28B0', u'\u28B1', u'\u28B2', u'\u28B3', u'\u28B4', u'\u28B5', u'\u28B6', u'\u28B7', 
u'\u28B8', u'\u28B9', u'\u28BA', u'\u28BB', u'\u28BC', u'\u28BD', u'\u28BE', u'\u28BF', 
u'\u28C0', u'\u28C1', u'\u28C2', u'\u28C3', u'\u28C4', u'\u28C5', u'\u28C6', u'\u28C7', 
u'\u28C8', u'\u28C9', u'\u28CA', u'\u28CB', u'\u28CC', u'\u28CD', u'\u28CE', u'\u28CF', 
u'\u28D0', u'\u28D1', u'\u28D2', u'\u28D3', u'\u28D4', u'\u28D5', u'\u28D6', u'\u28D7', 
u'\u28D8', u'\u28D9', u'\u28DA', u'\u28DB', u'\u28DC', u'\u28DD', u'\u28DE', u'\u28DF', 
u'\u28E0', u'\u28E1', u'\u28E2', u'\u28E3', u'\u28E4', u'\u28E5', u'\u28E6', u'\u28E7', 
u'\u28E8', u'\u28E9', u'\u28EA', u'\u28EB', u'\u28EC', u'\u28ED', u'\u28EE', u'\u28EF', 
u'\u28F0', u'\u28F1', u'\u28F2', u'\u28F3', u'\u28F4', u'\u28F5', u'\u28F6', u'\u28F7', 
u'\u28F8', u'\u28F9', u'\u28FA', u'\u28FB', u'\u28FC', u'\u28FD', u'\u28FE', u'\u28FF'
]

# Степени двойки для корректной подстановки символов
deg = [[0, 1, 2, 6], [3, 4, 5, 7]]

# Пользовательское меню
    # Ввод имени файла и смена размера
flag = True
name = ""
while flag:
    name = input('File name: ')
    if os.path.exists(name):
        flag = False
    else:
        if name == "help":
            print("Enter the file name or its full path.\nSupported files: .jpg, .png, maybe more")
        else:
            print("ERROR: File not found, try again")

    # Установка уровня чёрного
flag = True
while flag:
    fct = input('Set threshold of black (default - 127): ')
    if fct == '':
        factor = 127
        flag = False
    else:
        factor = int(fct)
        if factor > 255 or factor < 0:
            print("ERROR: Threshold must be in range [0..255]")
        else:
            flag = False

# Инициализация картинки
image = Image.open(name)
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]

# Warn если картинка слишком большая
if width > 256 or height > 256:
    print("WARNING: The picture is too big ({w}x{h}). Recommended size: 256x256 or less".format(w = width, h = height))
    answer = input("Do you want to resize the picture? [Y/N] ")
    if answer == "Y" or answer == "y":
        nw = width
        nh = height
        i = 2
        while nw > 256 or nh > 256:
            nw = width // i
            nh = width // i
            i += 1
        nsize = (nw, nh)
        image.thumbnail(nsize, Image.ANTIALIAS)
        width, height = image.size
        print("New size: {w}x{h}".format(w = width, h = height))
pix = image.load()

# Создание двумерного массива символов
n = (width + 1) // 2
m = (height + 3) // 4
A = [] * n
for i in range(n):
    A.append([0] * m)
for i in range (n):
    for j in range (m):
        A[i][j] = 0

# Заполнение массива символов
for i in range(width):
    for j in range(height):
        S = pix[i, j][0] + pix[i, j][1] + pix[i, j][2]
        some = deg[i % 2][j % 4]  
        if (S <= factor * 3):
            A[i // 2][j // 4] += 2 ** some

# Создание папки с результатами, создание нового файла
if os.path.exists("results") == False:
    os.mkdir("results")
outName = "results/" + name.split(".")[0] + ".txt"
f = open(outName, 'w', encoding='utf-8')

# Заполнение итогового документа
for j in range(m):
    for i in range(n):
        it = int(A[i][j])
        f.write(str(alf[it]))
    f.write("\n")

print("Successful!")
f.close()
