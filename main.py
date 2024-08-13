import time
import sys

def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

text = """  ___|
\___ \  __ \   _ \   _ \  __ \  
      | |   | (   | (   | |   | 
_____/ _|  _|\___/ \___/  .__/  
                         _|"""

# Запускаем анимацию
type_out(text, delay=0.02)

# Перекрашиваем в зеленый цвет
print("\033[92m" + text + "\033[0m")
