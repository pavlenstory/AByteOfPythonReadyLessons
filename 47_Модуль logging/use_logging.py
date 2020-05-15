import  os, platform, logging

if platform.platform().startswith('Windows'): #узнаем какая операционная система
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \#мы объединяем три части пути к файлу вместе
                                os.getenv('HOMEPATH'),\
                                'test,log')#название программы
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log') # мы конфигурируем модуль logging таким образом, чтобы он записывал все сообщения в определённом формате в указанный файл.

print("Сохраням лог в", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)
logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")

