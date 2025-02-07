import subprocess


def run(prompt: str, items: set):
    return subprocess.run(["rofi", "-dmenu", "-i", "-p", prompt], input="\n".join(items).encode(), capture_output=True).stdout.decode()[:-1]
