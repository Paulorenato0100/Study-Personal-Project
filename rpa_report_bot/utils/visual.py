import sys
import time

def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar():
    for i in range(0, 101, 10):
        print(f"\r🔄 Processando: {i}%", end="")
        time.sleep(0.15)
    print()