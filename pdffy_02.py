import os
from PIL import Image
from tqdm import tqdm


def merge_all_pngs_to_pdf(output_pdf):
    target_height = 1080
    image_list = [f for f in os.listdir() if f.lower().endswith(".png")]

    if not image_list:
        print("PNG 파일이 없습니다.")
        return

    image_list.sort()
    images = []

    print("이미지 처리 중...")

    for image_path in tqdm(image_list, desc="Resizing images", unit="img"):
        img = Image.open(image_path)

        # 비율 유지한 상태로 1080px 높이에 맞게 리사이즈
        aspect_ratio = img.width / img.height
        new_width = int(target_height * aspect_ratio)
        img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)

        images.append(img.convert("RGB"))

    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"{output_pdf}로 저장 완료! (세로 1080px, 비율 유지)")


merge_all_pngs_to_pdf("merged_pdf.pdf")
