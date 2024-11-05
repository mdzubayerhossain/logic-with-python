# import barcode
# from barcode.writer import ImageWriter
# from openpyxl import Workbook
# from openpyxl.drawing.image import Image

# # Function to generate barcode images
# def generate_barcodes(start_value, end_value):
#     barcodes = []
#     for value in range(start_value, end_value + 1):
#         barcode_value = str(value).zfill(5)  # Zero-fill to make it 5 digits
#         code128 = barcode.get_barcode_class('code128')
#         barcode_instance = code128(barcode_value, writer=ImageWriter())
#         filename = f'barcode_{barcode_value}'
#         barcode_instance.save(filename)
#         barcodes.append((barcode_value, f'{filename}.png'))
#     return barcodes

# # Generate barcodes from 10000 to 10020
# start_value = 10000
# end_value = 10020
# barcodes = generate_barcodes(start_value, end_value)

# # Write barcodes to an Excel file
# wb = Workbook()
# ws = wb.active
# ws.append(["Barcode Value", "Barcode Image"])

# for barcode_value, image_filename in barcodes:
#     img = Image(image_filename)
#     ws.append([barcode_value, barcode_value])
#     ws.add_image(img, f'B2')

# output_file = "barcodes.xlsx"
# wb.save(output_file)
# print(f"Barcodes exported to {output_file}")



import os
import barcode
from barcode.writer import ImageWriter
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Function to generate barcode images
def generate_barcodes(start_value, end_value):
    barcodes = []
    barcode_folder = "barcodes"
    if not os.path.exists(barcode_folder):
        os.makedirs(barcode_folder)
    
    for value in range(start_value, end_value + 1):
        barcode_value = str(value).zfill(5)  # Zero-fill to make it 5 digits
        code128 = barcode.get_barcode_class('code128')
        barcode_instance = code128(barcode_value, writer=ImageWriter())
        filename = os.path.join(barcode_folder, f'barcode_{barcode_value}')
        barcode_instance.save(filename)
        barcodes.append((barcode_value, f'{filename}.png'))
    return barcodes

# Generate barcodes from 10000 to 10020
start_value = 10000
end_value = 20000
barcodes = generate_barcodes(start_value, end_value)

# Write barcodes to an Excel file
wb = Workbook()
ws = wb.active
ws.append(["Barcode Value", "Barcode Image"])

for i, (barcode_value, image_filename) in enumerate(barcodes, start=2):
    img = Image(image_filename)
    ws.append([barcode_value, barcode_value])
    ws.add_image(img, f'B{i}')

output_file = "barcodes.xlsx"
wb.save(output_file)
print(f"Barcodes exported to {output_file}")
