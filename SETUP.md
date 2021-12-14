домашний каталог для проекта Django

mkdir django-app
cd django-app

создадим виртуальную среду и назовем ее django_env :

virtualenv django_env
Затем нужно активировать окружение:
source django_env/bin/activate

sudo apt install git
клонируем  проект:

https://github.com/savvit/VitaliiSavchuk_Yalantis_Python_School.git
После клонирования вам необходимо установить. requirements.txt Этот файл используется для указания, какие пакеты python необходимы для запуска проекта.

pip install -r requirements.txt
И теперь вы можете смело запускать проект командой:

./manage.py runserver