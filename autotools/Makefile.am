AUTOMAKE_OPTIONS = foreign

# Файлы и каталоги, которые попадут в дистрибутив
EXTRA_DIST = main.py README.md screenshots docs

all: run

# Установка проекта (копирование main.py в install/)
install-data-local:
	@mkdir -p install
	@cp main.py install/

# Запуск проекта
run:
	@$(PYTHON) main.py

# Компиляция Python файлов в байткод
build:
	@$(PYTHON) -m py_compile main.py

# Генерация документации
docs:
	@if [ -f Doxyfile ]; then \
		echo "Генерация документации с помощью Doxygen"; \
		mkdir -p docs; \
		$(DOXYGEN) Doxyfile; \
	else \
		echo "Doxyfile не найден"; \
	fi

# Очистка временных файлов
clean-local:
	@rm -rf __pycache__ *.pyc

# Полная очистка проекта
distclean-local: clean-local
	@echo "Удаляем все сгенерированные файлы..."
	@rm -rf install docs autom4te.cache build-aux
	@rm -f Makefile Makefile.in aclocal.m4 configure config.log config.status config.cache \
	       install-sh missing depcomp
	@rm -f config.status.lineno configure.lineno
	@rm -f *.tar.gz

# Подсчет строк кода
wc:
	@wc -l main.py

# Справка по целям
help:
	@echo "Использование Makefile:"
	@echo " make build      - компиляция Python файлов в байткод"
	@echo " make run        - запуск проекта"
	@echo " make install    - установка проекта в install/"
	@echo " make dist       - создание архива проекта"
	@echo " make docs       - генерация документации Doxygen"
	@echo " make clean      - удаление временных файлов"
	@echo " make distclean  - полная очистка проекта"
	@echo " make wc         - подсчет строк кода"
	@echo " make help       - справка по Makefile"

# Обработка неизвестных команд
%:
	@if echo "$@" | grep -Eq "(-am$$|dist|distdir|all|install)"; then \
		exit 0; \
	else \
		echo "Ошибка: неизвестная команда '$@'"; \
		echo "Введите 'make help' для списка доступных команд"; \
	fi