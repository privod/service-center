@echo off

pushd
cd ..

call :delete env
REM call :delete build
REM call :delete dist
REM call :delete logmon.egg-info

echo Создаю новое виртуальное окуржение "env" ...
python35 -m venv env
if %errorlevel% neq 0 goto error

call env\Scripts\activate
if %errorlevel% neq 0 goto error

python -m pip install --upgrade pip
if %errorlevel% neq 0 goto error

pip install --upgrade setuptools
if %errorlevel% neq 0 goto error

pip install django
if %errorlevel% neq 0 goto error

goto exit

:error
pause
goto exit

:delete
if exist %1 (
  echo Удаляю папку "%1" ...
  rmdir %1 /S /Q
)

:exit
popd