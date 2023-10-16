contacts = {
    'Jabir Panoli': '070120 70955',
    'Sreedev Associates': '09207944455',
    'm-build': '9656783100',
    'mediaspot': '099464 90659',
    'captions': '079072 75267',
    'n-arch': '098461 43771',
    'gst-suvidha': '094477 48003',
    'peevees': '082810 14044',
    'universal network': '096336 64422',
    'image_printing': '080785 29528'
}

contacts.update({
    "baby cry . in": "81368 19192",
    "Hyper happymart": "89438 00150",
    "ALEZHA DESIGN BOUTIQUE": "95622 33355",
    "ELITE AL WAHA TOURISM & TRAVELS": "07947113003",
    "HOME BASE PANDIKKAD": "80867 60709",
    "Malabar Wood Furniture and Home Needs": "97781 09051",
    "kurikkal hardware & sanitary": "094478 44095",
    "Paint Mart": "090482 00033"
})

def format_phone_number(phone_number):
    # Remove spaces and leading zeros
    clean_phone = phone_number.replace(" ", "").lstrip('0')
    return "+91" + clean_phone

def create_vcard(name, phone_number):
    formatted_phone_number = format_phone_number(phone_number)
    return f"""
BEGIN:VCARD
VERSION:3.0
FN:Sales {name}
TEL:{formatted_phone_number}
END:VCARD
"""

with open('contacts.vcf', 'w') as file:
    for name, phone_number in contacts.items():
        file.write(create_vcard(name, phone_number))

print("VCF file has been created as 'contacts.vcf'")
