from PIL import Image

img = Image.open("bits.bmp").convert("L")
pixel = img.tobytes()

bits = []
for p in pixel:
    # pixel nero = 0, pixel chiaro = 1
    bit = 1 if p > 128 else 0
    bits.append(bit)

# creare byte
byte = []
for i in range(0, len(bits), 8):
    val = 0
    for b in bits[i:i+8]:
        val = (val << 1) | b
    byte.append(val)

data = bytes(byte)

with open("recovered.zip", "wb") as f:
    f.write(data)

