@echo off
CD /d"%~dp0"
start /d"%cd%\server\dist\app\" app -p 
pause 
echo.