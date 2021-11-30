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
try:
    #размер сетки  
    if int(f[0][0]) > 0 : N = int(f[0][0])

    #исходное положение зомби
    if ((int(f[1][0]) < N) and int(f[1][1]) < N) : 
        START = (int(f[1][0]), int(f[1][1]))
    
    #список начальных позиций существ
    CREARURES_START = {}
    for i in range(len(f[2])-1):
        if ((int(f[2][i]) < N) and (int(f[2][i+1]) < N) and (int(f[2][i]) >=0) and (int(f[2][i+1]) >= 0)) :
            if i % 2 == 0 : CREARURES_START.update({(int(f[2][i]), int(f[2][i+1])): 'creature'})
        else : 
            if i % 2 == 0 : print('существо', int(i/2 + 1), 'исключено, так как находится за пределами мира')
    
    #список движений зомби    
    MOVE = f[3][0]
    for h in range(len(MOVE)) :
        if MOVE[h] != 'R' and MOVE[h] != 'D' and MOVE[h] != 'U' : 
            print ('Обнаружено некорректное значение в пути зомби')
            MOVE = MOVE.replace(MOVE[h], '')
    
    #заводим перепись зомби по порядку заражения [[начальная координата X][начальная координата Y][шаг]]
    zombie_list = {0 : [START[1], START[0], 0]}
    creatures_list = CREARURES_START.copy()
        
    #функция движения зомби        
    def zombie_move (step, axis, zombie, number):
        
        zombie[axis] = zombie[axis] + step
        zombie[2] = zombie[2] + 1
        
        if zombie[axis] == N : zombie[axis] = 0
        if zombie[axis] == -1 : zombie[axis] = N - 1
        
        print ('zombie', number, 'moved to X:', zombie[1], 'Y:', zombie[0])
        
        return zombie
    
    #функция заражения существа    
    def creature_to_zombie ():
        if creatures_list.get((zombie_list[zombie_number][1], zombie_list[zombie_number][0])) != None :
            creatures_list.pop((zombie_list[zombie_number][1], zombie_list[zombie_number][0]))
            zombie_list.update({len(zombie_list) : [zombie_list[zombie_number][0], zombie_list[zombie_number][1], 0]})
            print ('zombie', zombie_number, 'infected creature at X:', zombie_list[zombie_number][1], 'Y:', zombie_list[zombie_number][0])
        return
        
    count_of_ended = 0
    
    # Цикл для последовательного движения зомби
    #zombie_number = 0
    #while len(zombie_list) > zombie_number :
    #    for j in range(len(MOVE)):
    # Для акцивации нужно раскомментировать в том числе конец цикла
    
    # Цикл для параллельного движения зомби
    while len(zombie_list) > count_of_ended :
        for zombie_number in range(len(zombie_list)):
    # Конец цикла для параллельного движения зомби
            if zombie_list[zombie_number][2] < 4 :
                target = MOVE[zombie_list[zombie_number][2]]
                if target == 'R' : 
                    zombie_list[zombie_number] = zombie_move(1, 1, zombie_list[zombie_number], zombie_number)
                    creature_to_zombie()
                                    
                if target == 'L' : 
                    zombie_list[zombie_number] = zombie_move(-1, 1, zombie_list[zombie_number], zombie_number)
                    creature_to_zombie()
                        
                if target == 'U' : 
                    zombie_list[zombie_number] = zombie_move(-1, 0, zombie_list[zombie_number], zombie_number)
                    creature_to_zombie()
                        
                if target == 'D' : 
                    zombie_list[zombie_number] = zombie_move(1, 0, zombie_list[zombie_number], zombie_number)
                    creature_to_zombie()
            else : count_of_ended = count_of_ended + 1
     
    # Конец цикла для последовательного движения зомби
    #    zombie_number = zombie_number + 1
    
    #выводим позиции зомби
    
    print('\n')
    for j in range(len(zombie_list)):
        print('zombie', j, 'stay at X:', zombie_list[j][1], 'Y:', zombie_list[j][0])
        
    #ищем выживших существ
    
    print('\n')
    live_creatures = list(creatures_list.keys())
    for k in range(len(live_creatures)) :
        print('creatures stay on X:', live_creatures[k][0], 'Y:', live_creatures[k][1])
        
    if live_creatures == [] : print('creatures None')

except ValueError:
    print('N, START или CREARURES_START не является числом')
    
except IndexError:
    print('Недостаточно данных в файле входных данных')
    
except NameError:
    print('Ошибка вводных данных')
    
finally: 
    a.close()
