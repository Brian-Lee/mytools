@echo off
:main
::set "file1= C:\Users\Brian\PycharmProjects\autodrive\preds\last\preds_094_plus_logits_td_b_var.csv"
::set "file2=C:\Users\Brian\PycharmProjects\autodrive\preds\last\preds_094_plus_logits_lt_-0p3_toned_down.csv"
set "file1=file1.txt"
set "file2=file2.txt"


fc %file1% %file2% > nul
if errorlevel 1 goto error

:next
echo identical
pause
exit

:error
echo different
pause