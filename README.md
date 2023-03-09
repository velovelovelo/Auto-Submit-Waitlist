# Auto-Submit-Waitlist

### 1. Open Vscode,  before running this script make sure your pc install git and phyton

```
pip install pandas selenium time
```

```
git clone https://github.com/velovelovelo/Auto-Submit-Waitlist
```
```
cd Auto-Submit-Waitlist
```
```
ls
nano emaildata.csv
```
input your email `CTRL` + `X` `Y` `ENTER` and save


```
ls
nano main.py
```
- change this to your local path `fill with the path directory your chrome path`
- example : C:/Users/velovelovelo/Downloads/chromedriver_win32/chromedriver.exe
- if you dont have chrome driver , you can download here : https://chromedriver.chromium.org/downloads
- select the  version of Google Chrome that you are using, then 'Extract' and see where the file is located
- fill the path and then `CTRL` + `X` `Y` `ENTER` for save


### 2.start the script

```
python main.py
or
python3 main.py
```

- Enter the Waitlist Website Link `ENTER`
- Enter the XPATH Email (Please Inspect Element in the Section where the contents of the Email and Copy XPATH) Enter into the Terminal
- Enter the XPATH Button (Please Inspect Element in the Button Section Join Waitlist Button and Copy XPATH) Enter into Terminal
- `ENTER` script will be running
- Done, finished

Note :This script runs on a website that only fills in email and clicks on Join Waitlist (without email verification) if you have to confirm the email, you have do it manually
