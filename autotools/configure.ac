AC_PREREQ([2.69])
AC_INIT([QuadraticSolver], [1.0], [veronika.sh@mail.ru])

AM_INIT_AUTOMAKE([foreign -Wall -Werror])

AC_PROG_INSTALL
AC_PROG_MAKE_SET

AC_CHECK_PROGS(PYTHON, [python3 python], no)
if test "$PYTHON" = "no"; then
    AC_MSG_ERROR([Python не найден])
fi

AC_CHECK_PROG(DOXYGEN, doxygen, doxygen, no)
if test "$DOXYGEN" = "no"; then
    AC_MSG_WARN([Doxygen не найден])
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT