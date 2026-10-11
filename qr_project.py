import qrcode
import cv2


def make_qr():
    link = input("Enter a link: ")
    img = qrcode.make(link)
    img.save("my_qr.png")
    print("QR code saved as my_qr.png")


def read_qr():
    path = input("Enter the QR image file name: ")
    img = cv2.imread(path)
    if img is None:
        print("Could not open that file.")
        return
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)
    if data:
        print("Link:", data)
    else:
        print("No QR code found")


while True:
    print("\n1. Link to QR code")
    print("2. QR code to link")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        make_qr()
    elif choice == "2":
        read_qr()
    elif choice == "3":
        break
    else:
        print("Invalid choice")