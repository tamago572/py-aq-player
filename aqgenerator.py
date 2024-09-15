import subprocess

def generate(exePath, text, preset, outputFilePath):
    result = subprocess.run(f"{exePath} /T \"{text}\" /P \"{preset}\" /W \"{outputFilePath}\"")
    print("\nresult: \n" + str(result) + "\n")

def playVoice(exePath, text, preset):
    result = subprocess.run(f"{exePath} /T \"{text}\" /P \"{preset}\"")
    print("\nresult: \n" + str(result) + "\n")