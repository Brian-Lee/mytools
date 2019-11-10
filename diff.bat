@echo on
cd /d "c:\path"
del file3.txt 2>nul
for /f "delims=" %%a in (file1.txt) do (
   set "flag="
     for /f "delims=" %%b in (file2.txt) do (
       if "%%a"=="%%b" set flag=1
     )
   if not defined flag >>file3.txt echo %%a
)