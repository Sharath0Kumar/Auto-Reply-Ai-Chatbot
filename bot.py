import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="Write your api key",
)

def is_last_message_from(sender: str, chat_text: str) -> bool:
    """
    Check if the last message in a WhatsApp chat is from the given sender.
    
    :param sender: The sender name (e.g., "XYZ")
    :param chat_text: The copied chat text
    :return: True if last message is from sender, else False
    """
    # Split into lines
    lines = chat_text.strip().splitlines()
    if not lines:
        return False

    # Get the last line
    last_line = lines[-1]

    # WhatsApp format: "date, time - sender: message"
    try:
        sender_part = last_line.split(" - ", 1)[1].split(":", 1)[0].strip()
    except IndexError:
        return False

    return sender_part == sender


pyautogui.click(984, 747)
time.sleep(3)
while True :
    # Give yourself a little time to switch windows before it runs

    # Step 1: Click on the icon at (984, 747)
    time.sleep(2)  # wait for the app to open/respond

    # Step 2: Drag to select text from (422, 171) to (1341, 649)
    pyautogui.moveTo(422, 171)
    pyautogui.dragTo(1341, 649, duration=1, button='left')

    time.sleep(0.5)

    # Step 3: Copy (CTRL + C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(0.5)

    # Step 4: Get from clipboard into variable
    chatHistory = pyperclip.paste()

    print("Captured text:")
    print(chatHistory)


    if is_last_message_from(chatHistory):

        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            message = [
                {"role" : "system", "content": "You are a person named Sharath who speaks kannada as well as english , You are from india and you are coder. You analyze chat history and respond like Sharath. output shoulde be the next chat response (text message only)"},
                {"role" : "user", "content": chatHistory },
            ]
        )

        response = completion.choice[0].message.content
        pyperclip.copy(response) 

        # Step 5: Click at (580, 680), paste text and press Enter
        pyautogui.click(580, 680)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.press('enter')