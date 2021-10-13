# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:00:56 2021

@author: Максим Лавринов
"""

#Считываем вводные данные из файла

a=open('Zombie_in.txt')
f=[]

for line in a:
    f.append(line.split())

#размер сетки    
N = int(f[0][0])

#исходное положение зомби
START = (int(f[1][0]), int(f[1][1]))

#список начальных позиций существ
CREARURES_START = []
for i in range(len(f[2])-1):
    if i % 2 == 0 : CREARURES_START.append((int(f[2][i]), int(f[2][i+1])))

#список движений зомби    
MOVE = f[3][0]

#заводим перепись зомби по порядку заражения [[начальная координата X][начальная координата Y]]
zombie_list = [[START[1], START[0]]]

#создаем сетку мира
world = [[0] * N for i in range(N)]

#инициализируем зомби
world[zombie_list[0][0]][zombie_list[0][1]] = 1

#инициализируем существ
for i in range(len(CREARURES_START)):
    world[CREARURES_START[i][1]][CREARURES_START[i][0]] = 2
    
#функция движения зомби, на вход подаются:
# step - шаг зомби, определяется увеличением или уменьшением значении координаты в зависимости от направления
# axis - направление движения зомби, где 1 - по горизонтали, 0 - по вертикали
# zombie_list - список зомби
# world - состояние мира
def zombie_move (step, axis, zombie_list, world):
    zombie_list[i][axis] = zombie_list[i][axis] + step
    
    #проверяем перемещение через край мира
    if zombie_list[i][axis] == N : zombie_list[i][axis] = 0 
    if zombie_list[i][axis] == -1 : zombie_list[i][axis] = N - 1
    
    print ('zombie', i, 'moved to X:', zombie_list[i][1], 'Y:', zombie_list[i][0])
    
    #проверяем наличие существа в клетке с зомби и заражем его при обнаружении
    if world[zombie_list[i][0]][zombie_list[i][1]] == 2 :
        zombie_list.append([zombie_list[i][0], zombie_list[i][1]])
        print ('zombie', i, 'infected creature at X:', zombie_list[i][1], 'Y:', zombie_list[i][0])
        world[zombie_list[i][0]][zombie_list[i][1]] = 1
        
i = 0

#двигаем зомби в соответствии с заданным путем
while len(zombie_list) > i :
    for j in range(len(MOVE)):
        if MOVE[j] == 'R' : 
            zombie_move(1, 1, zombie_list, world)
        if MOVE[j] == 'L' : 
            zombie_move(-1, 1, zombie_list, world)
        if MOVE[j] == 'U' : 
            zombie_move(-1, 0, zombie_list, world)
        if MOVE[j] == 'D' : 
            zombie_move(1, 0, zombie_list, world)
    print('\n')
    i = i + 1
    
#выводим позиции зомби
for i in range(len(zombie_list)):
    print('zombie', i, 'stay at X:', zombie_list[i][1], 'Y:', zombie_list[i][0])
    
#ищем выживших существ
k = 0

for i in range(len(CREARURES_START)):
    if world[CREARURES_START[i][1]][CREARURES_START[i][0]] == 2: 
        print('creature stay on X:', CREARURES_START[i][0], 'Y:', CREARURES_START[i][1])
        k = 1

if k == 0 : print('creatures None')