foods = [{
  "chocolate": 7000,
  "strawberry": 7000,
  "cheese": 7000
}, {
  "tiramisu": 7000,
  "matcha": 7000,
  "opera": 7000,
  "vla": 9000
}, {
  "sakura": 12000,
  "dark chocolate": 12000,
  "chocolava": 12000,
  "red velvet": 12000,
  "unicorn": 12000
}]


def menu_list():
  print("\nDodonut's \nMENU \n")
  index = 0
  print("Basic Donuts: ")
  for x, y in foods[0].items():
    print(str(index) + '. ' + str(x) + ' ' + str(y))
    index += 1
  print("\nSignature Donuts: ")
  for x, y in foods[1].items():
    print(str(index) + '. ' + str(x) + ' ' + str(y))
    index += 1
  print("\nQueen Brunch: ")
  for x, y in foods[2].items():
    print(str(index) + '. ' + str(x) + ' ' + str(y))
    index += 1
  main()


def booking_service():
  name = input("Input your name: ")
  table_available = []
  i = 1
  for i in range(20):
    table_available.append(i + 1)
  print("\nList of available seat: ")
  for i in table_available:
    print("Meja", i, "Tersedia")

  choosen_seat = int(input("Choose your seat (1-20):"))
  if choosen_seat in table_available:
    print("Booking Table Success!")
  else:
    print("Table already booked, choose other table")
    booking_service()

  print("\nHello Ms.", name, "\nHere's tables number for you:", choosen_seat)

  print("\nYuk Pesan Menu Sekarang!")
  print("Please choose menu from the menu list")
  print(
    'Pilih Kategori: \n0 = Basic Donuts \n1 = Signature Donuts \n2 = Queen Brunch'
  )
  food_category = int(input('Pilih Kategori:'))

  index = 0
  if food_category == 0:
    print("\nBasic Donuts List: ")
    for x, y in foods[0].items():
      print(str(index) + '. ' + str(x) + ' ' + str(y))
      index += 1
  elif food_category == 1:
    print("\nSignature Donuts List: ")
    for x, y in foods[1].items():
      print(str(index) + '. ' + str(x) + ' ' + str(y))
      index += 1
  elif food_category == 2:
    print("\nQueen Brunch List: ")
    for x, y in foods[2].items():
      print(str(index) + '. ' + str(x) + ' ' + str(y))
      index += 1

  i = 1
  while i != 0:
    print("\ningin memesan?: \n0 = tidak \n1 = ya")
    i = int(input("Answer: "))
    if i == 1:
      food_name = input('masukkan nama makanan: ')
      food_name = food_name.lower()
      qty = input('masukkan jumlah: ')
      food_price = foods[food_category][food_name]
      price = food_price * int(qty)
      print(price)

    else:
      print("\nThis is your booking data: \nBooked tables: Table",
            choosen_seat, "\nBooking name:", name, "\nTotal price:", price)
      pay()


def pay():
  print("\nAre you sure want to pay?")
  answer = input("Answer (Yes/No):")
  answer = answer.lower()
  if answer == 'yes':
    print("Booking Success, Thank You!")
    exit()
  elif answer == 'no':
    pay()
  else:
    print("Invalid Answer, Try Again")
    pay()


def main():
  print("===============")
  print("Welcome! \n1 = View Menu \n2 = Booking Service \n3 = Exit ")
  choose = int(input("Choose a number (1-3): "))

  if choose == 1:
    menu_list()
  elif choose == 2:
    booking_service()
  elif choose == 3:
    print("Thank you!")
    exit()


main()
