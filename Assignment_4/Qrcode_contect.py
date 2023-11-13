import qrcode

name_contact = input("Please enter your name: ")
phone_number_contact = int(input("Please enter your phone number: "))

contact_info = [name_contact, phone_number_contact]

qr_code = qrcode.make(contact_info)

qr_code.save("contact-QRcode.png")