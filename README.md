# Opis aplikacji

## 1. Wymagania

- python 3.10+
- django 5.0 +
- paczka Pillow
- silnik bazy sqlite3

## 2. Postawienie i uruchomienie projektu

Wykonanie polecenia
Dla windows

```sh
python -m venv venv
```

Dla linux

```sh
python3 -m venv venv
```

Uruchomienie wirtualnej zmiennej środowikowej (venv)  
Dla windows

PowerShell

```sh
.\venv\Scripts\activate
```

lub (Git bash)

```sh
source venv/Scripts/activate
```

Instalacja Django

```sh
pip install django
```

Instalacja Pillow

```sh
pip install Pillow
```

(Opcionalnie jeżeli jest pusta baza to)

```sh
python manage.py migrate
```

Oraz stworzenie superuser

```sh
python manage.py createsuperuser
```

Wprzypadku używania silnika sqlite3 z repo dane do logowania

```sh
login: Bartłomiej
password:
```

Uruchomienie servera

```sh
python manage.py runserver
```

Dołączenie secert key:
AIprojekt/settings/"Secert Key"

```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
