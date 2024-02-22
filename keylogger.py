from os import system
try:from pynput.keyboard import Key,Listener
except:
    system("pip install pynput")
    system("cls")
    from pynput.keyboard import Key,Listener

system("cls")
print("Press any key to start ....")

count = 0
keys = []

def on_press(key):
    global count,keys
    count += 1
    if "<" in format(key) and ">" in format(key):print("'%d' pressed  '%s'" % (int(format(key).replace("<","").replace(">",""))-96, format(key)))

    else :print(f"{format(key)} pressed")
    keys.append(key)
    write_file(key)


def write_file(key):
    with open("log.txt" , "a" , encoding="utf-8") as file:


        k = str(key).replace("'", "")
        file.write((("\n"+k).replace("cmd","win")).replace("Key",""))


def on_release(key):
    if key == Key.esc:
        print("exit")
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

