import model_selenium
import model_appium
import time

selenium = model_selenium.ModelSelenium(
    "file:///D:/xampp/htdocs/音声リアルタイムボイスロイド変換/index.html"
)
appium = model_appium.ModelAppium(
    "http://127.0.0.1:4723", 
    "C:\Program Files (x86)\AHS\VOICEROID2\VoiceroidEditor.exe"
)

old_text = "入力待ち"
while True:
    time.sleep(0.1)
    text = selenium.get_text_by_id("msg")
    if text == "終了":
        break
    if text != old_text:
        old_text = text
        print(text)
        appium.play(text)
selenium.quit()
appium.quit()