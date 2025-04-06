# QuickSum
Quickly summarize anything on the screen with a single click of the alt key.

**How it works**

When you press the *alt key, it uses the `pyautogui` to take a screenshot, passes it to Google Gemini (`google-genai`) with a
prompt instructing it to explain the content of the screenshot. After getting the response, it uses `pyttsx3` to speak the
response without the need for a GUI.

**Installation**

After downloading the latest release, create a shortcut to the .bat file (`QuickSum.bat`) and move it to the autorun folder.
To access the autorun folder, press the windows key and R at the same time. In the run dialogue box that pops up in the bottom
left hand corner of the screen, type `shell:autorun` and press enter. Darg the shortcut in and restart your PC or just run the
file. When it's in the autorun folder, it will run whenever you power on your PC.
