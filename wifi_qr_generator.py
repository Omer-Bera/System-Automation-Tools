import qrcode
from PIL import Image

ssid = input("Wi-Fi Name (SSID): ")
password = input("Password: ")
logo_path = "logo.png"

wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(wifi_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

try:
    logo = Image.open(logo_path)
    
    width, height = img.size
    logo_size = int(width * 0.25)
    
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    
    pos = ((width - logo_size) // 2, (height - logo_size) // 2)
    img.paste(logo, pos, mask=logo)

except FileNotFoundError:
    print("Logo not found. Generating standard QR code.")

img.save("wifi_qr.png")
print("QR code saved as wifi_qr.png")