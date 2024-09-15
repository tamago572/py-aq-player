import aqgenerator

exePath = input("AquesTalkPlayer.exeのパスを入力: ")

saveFolder = ""

def generate():
    global saveFolder
    text = input("\nセリフを入力: ")
    preset = input("プリセットを入力: ")
    

    aqgenerator.playVoice(exePath, text, preset)

    shouldSave = input("音声を保存しますか？ (Y / n) ")

    if shouldSave != "n":
        # ファイル名になるセリフが長すぎる場合、短くする
        fileName = ""
        if preset == "":
            if len(text) > 14:
                fileName = f"{text[:14]}"
            else:
                fileName = f"{text}"
        else:
            if len(text) > 14:
                fileName = f"{preset}_{text[:14]}"
            else:
                fileName = f"{preset}_{text}"
            

        # 保存先が保存されていなかった場合、もう一度聞く
        if saveFolder == "":
            saveFolder = input("保存先のフォルダパスを入力してください: ")
            save_voice(exePath, text, preset, f"{saveFolder}\\{fileName}.wav")

        else:
            shouldSaveCurrentFolder = input("以前保存したフォルダに保存しますか？ (Y / n) ")

            if shouldSaveCurrentFolder != "n":
                save_voice(exePath, text, preset, f"{saveFolder}\\{fileName}.wav")

            else:
                saveFolder = ""
                saveFolder = input("保存先のフォルダパスを入力してください: ")


        f = open(f"{saveFolder}\\{fileName}.txt", "w", encoding="utf-8")
        f.write(text)

        return 2
    else:
        return 0

def save_voice(exePath, text, preset, filePath):
    aqgenerator.generate(exePath, text, preset, filePath)   
    print(f"音声ファイルを保存しました {filePath}")


try:
    while True:
        if generate() == 0:
            break

except KeyboardInterrupt:
    print("\n終了しています・・・")