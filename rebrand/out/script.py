import os
import glob

from PIL import Image
from config import sizes, names

CHROMIUM_PATH = "H:/ungoogled-chromium-windows/build/src/chromium-113.0.5672.127"
BROWSER_NAME = "0xGingi-Browser"
EXTENSIONS = ['grd', 'grdp']

def replace_file_with_text(name, str_a, str_b):
    txt = ""
    with open(name, "r", encoding="utf8") as f:
        txt = f.read()
        txt = txt.replace(str_a, str_b)
    with open(name, "w", encoding="utf8") as f:
        f.write(txt)

if not os.path.isdir('out'):
    os.mkdir('out')

image = Image.open('logo.png')

for size in sizes:
    temp = image.copy()
    temp.thumbnail((size['res'],size['res']))
    temp.save(f"out/{size['name']}")
    os.replace(f"{os.getcwd()}/out/{size['name']}", f"{CHROMIUM_PATH}/{size['parent']}{size['name']}")

for name in names:
    replace_file_with_text(f"{CHROMIUM_PATH}/{name['file']}", "Chromium", BROWSER_NAME)

for ext in EXTENSIONS:
    for name in glob.glob(f"{CHROMIUM_PATH}/chrome/app/*.{ext}"):
        replace_file_with_text(name, "Chromium", BROWSER_NAME)
    
    for name in glob.glob(f"{CHROMIUM_PATH}/components/*.{ext}"):
        replace_file_with_text(name, "Chromium", BROWSER_NAME)
