# Pelacakan warna kulit

import cv2
import numpy as np

# Objek VideoCapture
objVideo = cv2.VideoCapture(0)
if not objVideo.isOpened()
print('Kamera tidak dapat diakses')
exit()

tombolQDitekan = False
while (tombolQDitekan == False)
# Ambil per kerangka
ret, kerangka = objVideo.read()

# Proses pengambilan warna kulit
if ret == True
hsv = cv2.cvtColor(kerangka, cv2.COLOR_BGR2HSV)

# Peroleh bagian yang berwarna cokelat
batasRendah = np.array([0, 50, 70])
batasAtas = np.array([20, 230, 255])

hasil = cv2.inRange(hsv, batasRendah, batasAtas)

cv2.imshow('Video', hasil)

if cv2.waitKey(1) & 0xFF == ord('q')
tombolQDitekan = True
break

else
break

# Akhiri
objVideo.release()
cv2.destroyAllWindows()
