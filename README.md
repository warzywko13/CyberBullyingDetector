# CyberBullyingDetector

## Jak wyngenerować model?

#### 1. Preprocessing modelu.
```
    python main.py --preprocessing
```

#### 2. Trenowanie modelu.
```
    python main.py --train
```

## Jak uruchomić aplikację?

#### 1. Utworzenie pliku .env poprzez skopiowanie .env.example oraz nadanie klucza secret.

#### 2. Utworzenie bazy danych db.sqlite3.
```
    python manage.py migrate
```

#### 2. Uruchomienie serwera.
```
    python manage.py runserver
```

### Link do wytrenowanego modelu

1. Należy pobrać model można używając linku:
- https://drive.google.com/file/d/1R0zYdtKwA_M0jgN5v65E8AmpPnWqkxyb/view?usp=sharing

2. Plik ".zip" należy wypakować do głównego folder aplikacji. Po wypadkowaniu pliki powinny znajdować się w folderze ```./data/results```