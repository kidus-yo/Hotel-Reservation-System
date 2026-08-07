#Main Function
from menu import *


def main():
   running = True
   while running:
      choice = main_menu()
      if choice == 1:
         add_room()
      elif choice == 2:
         view_room()
      elif choice == 3:
         remove_room()
      elif choice == 4:
         book_room()
      elif choice == 5:
         cancel_reservation()
      elif choice == 6:
         view_reservation()
      elif choice == 9:
         running = False
         print("Thanks! for choosing us💐🎴")
if __name__ == "__main__":
   main()