import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess


def bt_refernce_clicked():
    file_type = [('mov', "*mov")]
    input_Dir = "./Desktop"
    file_path = filedialog.askopenfilename(filetypes=file_type, initialdir=input_Dir)
    print(file_path)
    input_file.set(file_path)


def bt_execution_clicked():
    gif = re.sub(".mov",".gif",input_file.get())

    args = ["ffmpeg","-i",input_file.get(), "-r","24", gif , "-y"]
    print(args)
    res = subprocess.call(args)
    if res == 0:
        messagebox.showinfo("変換成功","変換に成功しました.　出力先:\n"+gif)


def confirming_ffmpeg():
    res = subprocess.call(["ffmpeg", "-version"])
    if res != 0:
        messagebox.showwarning("エラー", "ffmpegがインストールされていません")
        exit()
if __name__ == '__main__':



    root = Tk()
    root.title("MOV to GIF Tool")
    root.geometry()
    frame0 = ttk.Frame(root,padding=1)
    frame0.grid(row=0,column=1)
    frame1 = ttk.Frame(frame0,padding=10)
    frame1.grid()
    bt_refernce = ttk.Button(frame0,text = "参照",command = bt_refernce_clicked)
    bt_refernce.grid(row=0,column=2)


    s1 = StringVar()
    s1.set('入力ファイル名:')
    label1 = ttk.Label(frame1, textvariable=s1)
    label1.grid(row=0, column=0)
    s2 = StringVar()
    # s2.set('出力ファイル名:')
    # label1 = ttk.Label(frame1, textvariable=s2)
    # label1.grid(row=1, column=0)


    frame2 = ttk.Frame(frame0, padding=(0,5))
    frame2.grid(row=1)


    input_file = StringVar()
    file_entry = ttk.Entry(frame1, textvariable=input_file, width=40)
    file_entry.grid(row=0, column=2)

    # output_file = StringVar()
    # file_output = ttk.Entry(frame1, textvariable=output_file, width=40)
    # file_output.grid(row =1,column=2)

    # Startボタンの作成
    bt_execution = ttk.Button(frame2, text='変換', command=bt_execution_clicked)
    bt_execution.pack(side=LEFT)

    # Cancelボタンの作成
    bt_cannel = ttk.Button(frame2, text='終了', command=quit)
    bt_cannel.pack(side=LEFT)

    confirming_ffmpeg()
    root.mainloop()