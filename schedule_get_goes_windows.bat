REM Schedule Get GOES in Windows
REM https://ss64.com/nt/schtasks.html
SET pyexe='C:\Anaconda3\python.exe'
SET script="C:\Users\blah blah\get_goes\get_goes.py"
SCHTASKS /create /tn "Get GOES" /tr "%pyexe% \%script%" /sc hourly
REM to check scheduled tasks
REM SCHTASKS /Query
REM To delete the scheduled task:
REM SCHTASKS /Delete /TN "Get GOES" /f
