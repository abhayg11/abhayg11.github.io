
if "%1"=="" (
	echo Usage:
	echo gen.bat ^<bookname^> ^<chapter/section^> ^<problem_end^>
	echo Example:
	echo gen.bat bump 4/1 16
	exit /b
)

set dir=%2
set pre=%dir:/=.%
set file=%1/Chapters/%dir%/%%p.tex

FOR /L %%p IN (1, 1, %3) DO (
	echo ^\mtexe{%pre%.%%p}>>%file%
	echo ^\begin{proof}>>%file%
	echo,	>>%file%
	echo ^\end{proof}>>%file%
)