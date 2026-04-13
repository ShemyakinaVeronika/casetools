# Отчет по автоматическому тестированию программы

---

## Цель работы

Цель работы — разработка набора автоматических тестов для функции решения квадратного уравнения и проверка корректности её работы с использованием тестирования.

---

## Тестируемый объект

Тестируется функция:

```
quadratic_equation(a, b, c)
```

Уравнение вида:

```
a*x² + b*x + c = 0
```

---

## Средства тестирования

* Язык программирования: Python
* Фреймворк тестирования: pytest
* Среда разработки: PyCharm

---

## Классификация тестов

Разработано 10 тестов, которые включают:

* общие
* краевые
* негативные


### Общие тесты

Проверка стандартных корректных входных данных:

* два корня
* один корень
* отсутствие действительных корней

---

### Краевые тесты

Проверка граничных случаев:

* коэффициент b = 0
* коэффициент c = 0
* большие и малые значения

---

### Негативные тесты

Проверка обработки ошибок:

* a = 0 (не квадратное уравнение)
* некорректные типы данных (str, None)

---

---

## Таблица тестовых данных

|  № | Тип теста  | Входные данные (a, b, c)     | Ожидаемый результат            |
| -: | ---------- | ---------------------------- | ------------------------------ |
|  1 | Общий      | (1, -3, 2)                   | [1.0, 2.0]                     |
|  2 | Общий      | (1, 2, 1)                    | [-1.0]                         |
|  3 | Общий      | (1, 0, 1)                    | "Действительных корней нет."   |
|  4 | Краевой    | (1, 0, -4)                   | [-2.0, 2.0]                    |
|  5 | Краевой    | (1, -5, 0)                   | [0.0, 5.0]                     |
|  6 | Краевой    | (1000000, -3000000, 2000000) | [1.0, 2.0]                     |
|  7 | Краевой    | (0.001, -0.003, 0.002)       | [1.0, 2.0]                     |
|  8 | Негативный | (0, 2, 1)                    | "Это не квадратное уравнение." |
|  9 | Негативный | ("a", 2, 1)                  | "Неверный тип коэффициентов."  |
| 10 | Негативный | (None, 2, 1)                 | "Неверный тип коэффициентов."  |

---

```
## Реализация тестов

import pytest
from main_after import quadratic_equation


# Общие случаи

def test_two_roots():
    assert quadratic_equation(1, -3, 2) == [1.0, 2.0]

def test_one_root():
    assert quadratic_equation(1, 2, 1) == [-1.0]


def test_negative_discriminant():
    assert quadratic_equation(1, 0, 1) == "Действительных корней нет."


# Краевые случаи

def test_zero_b():
    assert quadratic_equation(1, 0, -4) == [-2.0, 2.0]


def test_zero_c():
    assert quadratic_equation(1, -5, 0) == [0.0, 5.0]


def test_large_numbers():
    result = quadratic_equation(1e6, -3e6, 2e6)
    assert result == [1.0, 2.0]


def test_small_numbers():
    result = quadratic_equation(0.001, -0.003, 0.002)
    assert result == [1.0, 2.0]


# Негативные случаи

def test_a_is_zero():
    assert quadratic_equation(0, 2, 1) == "Это не квадратное уравнение."


def test_invalid_type_string():
    assert quadratic_equation("a", 2, 1) == "Неверный тип коэффициентов."


def test_invalid_type_none():
    assert quadratic_equation(None, 2, 1) == "Неверный тип коэффициентов."
```

---

## Результаты тестирования

Запуск:

```bash
pytest -v
```

Результат:

```
collected 10 items

test_quadratic.py::test_two_roots PASSED
test_quadratic.py::test_one_root PASSED
test_quadratic.py::test_negative_discriminant PASSED
test_quadratic.py::test_zero_b PASSED
test_quadratic.py::test_zero_c PASSED
test_quadratic.py::test_large_numbers PASSED
test_quadratic.py::test_small_numbers PASSED
test_quadratic.py::test_a_is_zero PASSED
test_quadratic.py::test_invalid_type_string PASSED
test_quadratic.py::test_invalid_type_none PASSED

====================== 10 passed in 9.31s ======================
```

---

## Анализ результатов

* Все 10 тестов пройдены успешно
* Ошибок не выявлено
* Функция корректно обрабатывает:

  * стандартные случаи
  * граничные значения
  * некорректные входные данные

---

## Вывод

Использование pytest позволило автоматизировать проверку функции и подтвердить её корректную работу.

Программа считается стабильной и корректной.
