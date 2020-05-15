import  sys, warnings
if sys.version_info[0] <3:
    warnings.warn("Для выполнения этой пронраммы необходима как минимум\
                  версия пайтон 3.0",
            RuntimeWarning) #предупреждение о времени пробежки
else:
    print('Эта версия полностью подходит')
    