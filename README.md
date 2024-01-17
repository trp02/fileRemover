**Background**
Application to find and remove files from my downloads folder because search feature in file explorer is slow

**To use yourself:**
1) Replace **path** in **delete.py** to your own downloads folder or wherever you want app to search
2) Declare any preset files line 9 in **delete.py** if you don't want to keep entering the name


**To create executable:**
pip install pyinstaller
python -m PyInstaller delete.py --onefile

Executable is dist/delete.exe
