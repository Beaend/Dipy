# Dipy - Бот для Discord. Для тех кто хочет оптимизировать работу своего сервера и изучить создание ботов.
#### *Изучайте, улучшайте, создавайте!*
## Бот имеет полностью блочную структуру 
#### *cogs - шестерёнки вашего бота*
### Создавайте новые cogs - подключайте, модифицируйте и улучшайте своего бота.

##Начало работы
###Установка linux
```bash
wget https://github.com/Beaend/Dipy/archive/0.1.0.tar.gz
tar -cvzf 0.1.0.tar.gz
mv ~/0.1.0 ~/Dipy
sd ~/Dipy
python3 -m venv .
source bin/activate
pip install discord.py
python main.py
```
###После перезагрузки
```bash
sd ~/Dipy
source bin/activate
python main.py
```
###Для внесения изменений в cogs
!reload - в чате Discord

###Для полного перезапуска
!stop - в чате Discord
```bash
python main.py
```