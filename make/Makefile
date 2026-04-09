APP = ../main.py
PYTHON = python
INSTALL_DIR = install
DOXYGEN = doxygen

.PHONY: run build install dist docs clean distclean help wc

run:
	@echo "Запуск программы"
	$(PYTHON) $(APP)


build:
	@echo "Python — интерпретируемый язык программирования, то есть исходный код выполняется напрямую интерпретатором."
	@echo "При обычном запуске проекта Python автоматически компилирует .py файлы в байткод (.pyc) и выполняет его."
	@echo "Команда make build делает это явно: преобразует исходный код (.py) в байткод (.pyc), который выполняется виртуальной машиной Python."
	@echo "Байткод ускоряет запуск программы, так как исключает повторный разбор исходного кода, но язык остаётся интерпретируемым."
	$(PYTHON) -m py_compile $(APP)


install:
	@echo "Установка проекта (копирование в папку $(INSTALL_DIR))"
	mkdir -p $(INSTALL_DIR)
	cp $(APP) $(INSTALL_DIR)


dist:
	@echo "Создание архива проекта"
	tar -czf project.tar.gz -C .. main.py README.md screenshots


docs:
	@echo "Создание документации с помощью Doxygen"
	@mkdir -p .. docs
	$(DOXYGEN) Doxyfile


clean:
	@echo "Частичная очистка проекта (удаление временных файлов)"
	rm -rf ../__pycache__


distclean: clean
	@echo "Полная очистка проекта (возвращаение проекта к исходному состоянию)"
	rm -rf $(INSTALL_DIR) docs install *.tar.gz


wc:
	@echo "Подсчет строк кода в $(APP) (запуск внешней утилиты)"
	wc -l $(APP)


help:
	@echo "Справка по Makefile:"
	@echo ""
	@echo " make build      - создание байткода (.pyc) для ускорения выполнения"
	@echo " make run        - запуск проекта"
	@echo " make install    - установка проекта (копирование в install/)"
	@echo " make dist       - создание архива проекта"
	@echo " make docs       - создание документации с помощью Doxygen"
	@echo " make clean      - частичная очистка проекта (удаление временных файлов)"
	@echo " make distclean  - полная очистка проекта (возвращаение проекта к исходному состоянию)"
	@echo " make wc         - подсчёт строк кода (запуск внешней утилиты)"
	@echo " make help       - справка по Makefile"


.DEFAULT:
	@echo "Ошибка: неизвестная команда"
	@echo "Введите 'make help' для списка доступных команд"