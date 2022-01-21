@echo off
set arg1=%1

if NOT "%arg1%" == "start" if NOT "%arg1%" == "stop" (goto :no)
if "%arg1%" == "start" (call :start)
if "%arg1%" == "stop" (call :stop)

EXIT /B

:start
"C:\Python39\python.exe" "C:\Users\jakak\Dokumenti\Automation\Time-Tracker\start.py"
EXIT /B

:stop
"C:\Python39\python.exe" "C:\Users\jakak\Dokumenti\Automation\Time-Tracker\end.py"
EXIT /B

:no
echo "Argument %arg1% non existened!"
EXIT /B