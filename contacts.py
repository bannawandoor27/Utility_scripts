contacts = {
  "Grillkith resto &cafe": "89433 11777",
  "foneworld_futurepoint": "9072649992",
  "Olala- Designer Fashion Boutique": "07947138503",
  "Jr.ROCKS": "081139 55582",
  "Safa Tiles & Granites": "096455 11112",
  "Namia Glass Palace plywoods & Hardwares": "099619 02945",
  "VARIKODAN INTERNATIONAL TRAVEL SERVICE": "07947416313",
  "BEST Computers": "075930 61111",
  "DIYA ABAYAS": "094975 54364",
  "Vouxoriginals": "09778215466",
  "CAPITOL THEATRE": "097452 02309",
  "Rose Studio vavasrose": "090481 62175",
  "Shoezo": "080891 20100",
  "Hi Food Restaurant": "89433 37751",
  "Yakka Sports": "099464 58999",
  "Aerius ABS Doors and uPVC Windows": "062387 75112",
  "Infinite Desk Architects & Planners": "07947133766",
  "Dr Sunils Homeopathic Clinic":"098461 16190",
  "GOOD SIGHT OPTICALS":"073061 27167",
  "Evoca Fashion Store":"070345 05147",
  "Steller Camera Rental Store":"062829 51314",
  "Red Sea Bakery":"086063 57012",
  "PRO TECH Academy Perinthalmanna":"091886 44268",
  "Dr. Salims Centre For Neuro Psychiatry":"098466 98338",
  "Moto Craft":"096050 08008",
  "Universal Tiles And Sanitary":"095626 00093",
  "Asian Tiles & Sanitary":"07947149238",
  "Brilliance College Perinthalmanna":"091691 61184",
  "Srishti group builders & developers":"062384 51281",
  "7Days Supermarket":"079940 04701"

}

  

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

with open('contacts_pmna_2.vcf', 'w') as file:
    for name, phone_number in contacts.items():
        file.write(create_vcard(name, phone_number))

print("VCF file has been created as 'contacts.vcf'")
