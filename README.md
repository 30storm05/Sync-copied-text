# Sync-copied-text
copy and paste text from iPhone to a windows pc using iPhone shortcuts
STEP1: download python on your computer from:  https://www.python.org/downloads/ or microsoft store
Step2: open command prompt by searching in the search bar
type " pip install flask pyperclip " and enter 
copy and paste the code in the "clipboard_sync_server" file attached into a code editor(notepad or VScode) and save it as a python file as clipboard_sync_server.py .
Then open command prompt and navigate to the folder where you saved your file and run this command " python clipboard_sync_server.py ".
Step3: find your pc ip adress by " ipconfig " on the command interface
Step4: go to your Iphone Shortcut app and click the '+' sign on the top right corner 
>>> search for "Get Clipboard" in the search action bar
>>> in the same shortcut add another action that is "Get Text From Input"
>>> change the input source to clipboard
>>> add another action " get contents of URL"
>>> here enter http://youripadress:5000/copy and then change the method to 'POST' and request bosy to JSON. Then add new field under the Body. Select its type as Dictionary.
set the key value to "content" and then the item to 'clipboard'
>>> add the last action "Show Result" and set result as "sent to pc"
>>> and done! 
