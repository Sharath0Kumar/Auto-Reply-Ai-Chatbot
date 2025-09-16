from openai import OpenAI

# pip install openai 

client = OpenAI(
    api_key="Write your api key",
)

command = '''
Here’s the script:

import pyautogui
import time
import pyperclip

# Give yourself a little time to switch windows before it runs
time.sleep(3)

# Step 1: Click on the icon at (984, 747)
pyautogui.click(984, 747)
time.sleep(1)  # wait for the app to open/respond

# Step 2: Drag to select text from (422, 171) to (1341, 649)
pyautogui.moveTo(422, 171)
pyautogui.dragTo(1341, 649, duration=1, button='left')
'''
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    message = [
        {"role" : "system", "content": "You are a person named Sharath who speaks kannada as well as english , He is from india and is a coder. You analyze chat history and respond like Sharath"},
        {"role" : "user", "content": command },
    ]
)

print(completion.choice[0].message.content)