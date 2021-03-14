# Dipy - Бот для Discord. Для тех кто хочет оптимизировать работу своего сервера и изучить создание ботов.
#### *Изучайте, улучшайте, создавайте!*
## Бот имеет полностью блочную структуру 
#### *cogs - шестерёнки вашего бота*
### Создавайте новые cogs - подключайте, модифицируйте и улучшайте своего бота.

## Начало работы
### Установка в linux (через терминал)
```bash
wget https://github.com/Beaend/Dipy/archive/0.2.0.tar.gz
tar -cvzf 0.2.0.tar.gz
mv ~/0.2.0 ~/Dipy
sd ~/Dipy
python3 -m venv .
source bin/activate
pip install discord.py
```
Перейти в папку Dipy/json и внести изменения в файл main.json
```json
{
  "token": "Введите токен вашего бота (получается на сайте разработчиков)"
}
```

### Для запуска (через терминал)
```bash
sd ~/Dipy
source bin/activate
python main.py
```

### Для внесения изменений в cogs
!reload - в чате Discord

### Для полного перезапуска
!stop - в чате Discord
```bash
python main.py
```