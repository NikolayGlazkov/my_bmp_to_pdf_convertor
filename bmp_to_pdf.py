import os

def bmp_to_pdf(bmp_file, pdf_file):
    from PIL import Image
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    # Открыть изображение BMP с помощью Pillow
    image = Image.open(bmp_file)

    # Создание нового файла PDF с размером страницы A4
    c = canvas.Canvas(pdf_file, pagesize=A4)

    # Получение размеров изображения BMP
    width, height = image.size

    # Определение размеров для вставки изображения в PDF
    aspect_ratio = height / float(width)
    pdf_width = A4[0] - 100  # Используем ширину страницы A4 с небольшим отступом
    pdf_height = pdf_width * aspect_ratio

    # Вставка изображения в PDF по центру страницы
    x_offset = (A4[0] - pdf_width) / 2
    y_offset = (A4[1] - pdf_height) / 2
    c.drawImage(bmp_file, x_offset, y_offset, width=pdf_width, height=pdf_height)

    # Сохранение изменений и закрытие файла PDF
    c.save()

# Путь к папке с файлами BMP
folder_path = '/Users/nikolay/Documents/my_bmp_to_pdf_convertor/bmp_temp_file'

# Проверка всех файлов в папке
for filename in os.listdir(folder_path):
    if filename.endswith(".bmp"):
        bmp_file_path = os.path.join(folder_path, filename)
        pdf_file_path = os.path.splitext(bmp_file_path)[0] + ".pdf"
        bmp_to_pdf(bmp_file_path, pdf_file_path)
