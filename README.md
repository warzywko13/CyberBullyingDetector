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