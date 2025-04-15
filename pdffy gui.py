import os
from tkinter import *
from tkinter import filedialog, messagebox, Listbox
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

# 이미지 파일 리스트
image_paths = []


def add_files_dialog():
    files = filedialog.askopenfilenames(
        title="이미지 파일 선택",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],
    )
    add_files(files)


def add_files(file_list):
    global image_paths

    # 새로 추가된 파일 중 중복되지 않는 것만 추가
    for path in file_list:
        if (
            path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
            and path not in image_paths
        ):
            image_paths.append(path)

    # 이름순 정렬
    image_paths.sort(key=lambda x: os.path.basename(x).lower())

    # 리스트박스 초기화 후 다시 채우기
    listbox.delete(0, END)
    for path in image_paths:
        listbox.insert(END, os.path.basename(path))


def convert_to_pdf():
    if not image_paths:
        messagebox.showwarning("알림", "변환할 이미지가 없습니다.")
        return

    target_height = 1080
    images = []

    for path in image_paths:
        img = Image.open(path)
        if img.width < img.height:
            img = img.rotate(90, expand=True)

        aspect = img.width / img.height
        new_width = int(target_height * aspect)
        img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
        images.append(img.convert("RGB"))

    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF 파일", "*.pdf")]
    )
    if save_path:
        images[0].save(save_path, save_all=True, append_images=images[1:])
        messagebox.showinfo("완료", f"PDF로 저장 완료!\n{save_path}")


def on_drop(event):
    files = root.tk.splitlist(event.data)
    add_files(files)


# GUI 시작
root = TkinterDnD.Tk()
root.title("🖼 이미지 → 📄 PDF 변환기")
root.geometry("500x450")

Label(root, text="이미지 파일을 드래그하거나 버튼으로 추가하세요").pack(pady=10)

# 리스트박스: 추가된 파일 보여주기
listbox = Listbox(root, width=60, height=10)
listbox.pack(pady=5)

# 드래그 앤 드롭 지원
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind("<<Drop>>", on_drop)

# 버튼
frame = Frame(root)
frame.pack(pady=10)

btn_add = Button(frame, text="이미지 파일 추가", command=add_files_dialog)
btn_add.grid(row=0, column=0, padx=10)

btn_convert = Button(frame, text="PDF로 저장", command=convert_to_pdf)
btn_convert.grid(row=0, column=1, padx=10)

root.mainloop()
