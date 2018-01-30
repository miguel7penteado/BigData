@echo off
cls

set titl=RANDOMTITLE%RANDOM%
title %titl%
for /f tokens^=3^ delims^=^" %%a in ('tasklist /nh /v /fi "WINDOWTITLE eq %titl%" /fo csv') do (
set PID=%%a
)
echo %PID% >> %TMP%\processo.pid
