from win32api import GetSystemMetrics
import win32gui, time, tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

print(width/2, height/2)


while True:

    x = int(width/2)
    y = int(height/2)
    #x=int(960)    # 1920 / 2 = 960 for X position on screen.
    #y=int(600)    # 1200 / 2 = 600 for Y position on screen.
    color=int(255)   # Pixel color, 255 = Red
    
    hwnd=win32gui.WindowFromPoint((x,y))
    hdc=win32gui.GetDC(hwnd)
    x1,y1=win32gui.ScreenToClient(hwnd,(x,y))
    win32gui.SetPixel(hdc,x1,y1,color)
    win32gui.SetPixel(hdc,x1-1,y1,color)
    win32gui.SetPixel(hdc,x1+1,y1,color)
    win32gui.SetPixel(hdc,x1,y1-1,color)
    win32gui.SetPixel(hdc,x1,y1+1,color)
    win32gui.SetPixel(hdc,x1-1,y1-1,color)
    win32gui.SetPixel(hdc,x1+1,y1+1,color)
    win32gui.SetPixel(hdc,x1-1,y1+1,color)
    win32gui.SetPixel(hdc,x1+1,y1-1,color)
 
    win32gui.SetPixel(hdc,x1-2,y1,color)
    win32gui.SetPixel(hdc,x1+2,y1,color)
    win32gui.SetPixel(hdc,x1,y1-2,color)
    win32gui.SetPixel(hdc,x1,y1+2,color)
    win32gui.SetPixel(hdc,x1-2,y1-2,color)
    win32gui.SetPixel(hdc,x1+2,y1+2,color)
    win32gui.SetPixel(hdc,x1-2,y1+2,color)
    win32gui.SetPixel(hdc,x1+2,y1-2,color)
 
    win32gui.ReleaseDC(hwnd,hdc)
 
    time.sleep(0.1)
