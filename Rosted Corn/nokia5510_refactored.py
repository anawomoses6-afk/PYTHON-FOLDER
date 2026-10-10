def nokia_5510_main():
    print("MY NOKIA 5510")
    while(True):
        menu_functionality = """
        1. Phone book 
        2. Message
        3. Chat
        4. Call register
        5. Tones
        6. Settings
        7. Call divert
        8. Music
        9. Games
        10. Calculator
        11. Reminder
        12. Clock
        13. Profile
        14. Service
        15. SIM service
        0.  Exit
        """ 
        print(menu_functionality)
        user_input = int(input("Enter number: "))
        
        match(user_input):
            case 1:
                phone_book()
            case 2:
                message()
            case 3:
                chat()
            case 4:
                call_register()
            case 5:
                tones()
            case 6:
                settings()
            case 7:
                call_divert()
            case 8:
                music()
            case 9:
                game()
            case 10:
                calculator()
            case 11:
                reminder()
            case 12:
                clock()
            case 13:
                profile()
            case 14:
                service()
            case 15:
                sim_service()
            case 0:
                print("Exiting...")
                break
            case _:
                print("Invalid selection")
                user_input = int(input("Enter valid option: "))
            
# COMPONENT FUNCTIONS

# Phone book function...
def phone_book():
    print("Phone book")
    while(True):
        phone_book_guard = """ 
        1. Search
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Copy
        7. Assign tone
        8. Send b’card 
        9. Options
        10. Speed Dials
        11. Voice tags 
        0. Exit
        """
        print(phone_book_guard)
        phone_number = int(input("Enter number: "))

        match(phone_number):
            case 1:  
                print("Search")
            case 2:  
                print("Service Nos")
            case 3:  
                print("Add name")
            case 4:  
                print("Erase")
            case 5:  
                print("Edit")
            case 6:  
                print("Copy")
            case 7:  
                print("Assign tone")
            case 8:  
                print("Send b'card")
            case 9:  
                print("Options") 
            case 10: 
                print("Speed dials")
            case 11: 
                print("Voice tags")
            case 0:
                print("Exiting...")
                break
            case _:  
                print("invalid selection")
  
# Message function... 
def message():
    print("Message")
    while(True):
        message_book_guard = """
        1. Write messages
        2. Inbox
        3. Outbox
        4. Picture messages
        5. Templates
        6. Smileys
        7. Message settings
        8. Info Service
        9. Voice mailbox number
        10. Service command editor
        0. Exit
        """       
        print(message_book_guard)
        message_input = int(input("Enter Option: "))

        match(message_input):
            case 1: 
                print("Write messages")
            case 2: 
                print("Inbox")
            case 3: 
                print("Outbox")
            case 4: 
                print("Picture")
            case 5: 
                print("Templates")
            case 6: 
                print("Smileys") 
            case 7: 
                print("Message settings")
            case 8:
                print("Info Service")
            case 9: 
                print("Voice mailbox number")
            case 10: 
                print("Service command editor")
            case 0:
                print("Exiting...")
                break
            case _:  
                print("invalid selection")
        
# Chat function...        
def chat():
    print("Chat")
    while(True):
        chat_call_guard = """
        1. Last call duration
        2. All calls’ duration
        3. Received calls’ duration
        4. Dialed calls’ duration
        5. Clear timers
        0. Exit
        """
        print(chat_call_guard)
        chat_input = int(input("Enter input: "))
        match(chat_input):
            case 1: 
                print("Last call duration")
            case 2: 
                print("All calls’ duration")
            case 3: 
                print("Received calls’ duration")
            case 4: 
                print("Erase recent call lists")
            case 5: 
                print("Clear timers")
            case 0:
                print("Exiting...")
                break
            case _:
                print("Invalid selection")
                
         
# Call register function...
def call_register():
    print("Call register")
    while(True):
        chat_book_guard = """
        1. Missed Calls
        2. Received calls
        3. Dialed numbers
        4. Erase recent call lists
        5. Show call costs
        6. Call cost settings
        7. Prepaid credit
        0. Exit
        """   
        print(chat_book_guard)
        chat_input = int(input("Enter Option: "))
        match(chat_input):
            case 1: 
                print("Missed Calls")
            case 2: 
                print("Received call")
            case 3: 
                print("Dialed numbers")
            case 4: 
                print("Erase recent call lists")
            case 5: 
                print("Show call duration")
                show_call_duration = """              
                1. Last call cost
                2. All calls’ cost
                3. Clear counters
                0. Exit
                """
                print(show_call_duration)
                show_input = int(input("Enter Option: "))
                match(show_input):
                    case 1: 
                        print("Last call cost")
                    case 2:
                        print("All calls cost")
                    case 3:
                        print("Clear counters")
                    case 0: 
                        print("Exiting...")
                        break
            case 6: 
                print("Call cost settings")
                call_set_duration = """
                1. Call cost limit
                2. Show costs in
                0. Exist
                """
                call_set_input = int(input("Enter Option: "))
                match(call_set_input):
                    case 1: 
                        print("Call cost limit")
                    case 2: 
                        print("Show costs in")
                    case 0: 
                        print("Exiting...")
                        break
            case 7: 
                print("Prepaid credit")                        
            case 0: 
                print("Exiting...")
                break
            case _:
                print("Invalid selection")
    
    
#Tones function...
def tones():
    print("Tones")
    while(True):
        tones_book_guard = """
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Message alert tone
        5. Keypad tones
        6. Warning tones
        7. Vibrating alert
        8. Screen saver
        0. Exit
        """
        print(tones_book_guard)
        tones_input = int(input("Enter Option: "))
        match(tones_input):
            case 1: 
                print("Ringing tone")
            case 2: 
                print("Ringing volume")
            case 3: 
                print("Incoming call alert")
            case 4: 
                print("Message alert tone")
            case 5: 
                print("Keypad tones")
            case 6: 
                print("Warning tones")
            case 7: 
                print("Vibrating alert")
            case 8:
                print("Screen saver")
            case 0:
                print("Exiting...")
                break
            case _: 
                print("invalid selection")
  
  
# Settings function...
def settings():
    print("Settings") 
    while(True): 
        settings_menu = """
        1. Call Settings
        2. Phone Settings
        3. Security Settings
        4. Restore factory settings
        0. Exit
        """
        print(settings_menu)
        settings_input = int(input("Enter Option: "))

        match(settings_input):
            case 1: 
                print("Call Settings")
                call_settings_book_guard = """
                1. Automatic redial
                2. Speed dialing
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Automatic answers
                0. Exit
                """     
                print(call_settings_book_guard )
                call_setting_input = int(input("Enter Option: "))
                match(call_setting_input):
                    case 1: 
                          print("Automatic redial")       
                    case 2: 
                        print("Speed dialing")
                    case 3:
                        print("Call waiting options")
                    case 4:
                        print("Own numbers sending")
                    case 5: 
                        print("Phone line in use")
                    case 6:
                        print("Automatic answer")
                    case 0:
                        print("Exiting")
                        break
            case 2: 
                print("phone_settings")
                phone_setting = """
                1. Language
                2. Call info display
                3. Welcome note
                4. Network selection
                5. Confirm SIM service actions
                0. Exit
                """
                print(phone_setting )
                phone_input = int(input("Enter Option"))
                match(phone_input):
                    case 1: 
                          print("Language")       
                    case 2: 
                        print("Call info display")                                                
                    case 3: 
                        print("Welcome note")       
                    case 4: 
                        print("Network selection")    
                    case 5: 
                        print("Confirm SIM service actions")                                     
                    case 0: 
                        print("Exiting")
                        break
            case 3:
                print("Security_settings")
                Security_setting_guard = """
                1. PIN code request
                2. Call barring service
                3. Fixed dialing
                4. Closed user group
                5. Security level
                6. Change access codes
                0. Exit
                """
                print(Security_setting_guard)
                security_input = int(input("Enter Option"))
                match(security_input):          
                    case 1: 
                          print("PIN code request")       
                    case 2: 
                        print("Cell info display")                                                
                    case 3: 
                        print("Fixed dialing")       
                    case 4: 
                        print("Closed user group")    
                    case 5: 
                        print("Security level")  
                    case 6: 
                        print("Change access codes")     
                    case 0: 
                        print("Exiting...")
                        break
            case 4:
                print("Restore factory settings")
            case 5:
                print("Confirm SIM service actions")
            case 0:
                print("Exiting...")
                break
            case _:
                print("Invalid selection")
                
# Call divert function
def call_divert():
    print("Call divert\n")
    while(True):
        # Todo
        print("Exiting...")
        break
        
# Music function
def music():
    print("Music")
    while(True):
        music_setting_guard = """
        1. Music player
        2. Radio
        3. Recorder
        4. Track list
        0. Exit
        """
        print(music_setting_guard)
        print()
        music_input = int(input("Enter Option"))
        match(music_input):

          case 1: 
               print("Music player")
          case 2: 
               print("Radio")
          case 3: 
               print("Recorder")
          case 4:
                print("Track list")
          case 0:
               print("Exist")
               break
          case _: 
               print("Invalid selection")

# Games function
def games():
    print("Games\n")
    while(True):
        # Todo
        print("Exiting...")
        break

# Calculator function    
def calculator():
    print("Calculator\n")
    while(True):
        # Todo
        print("Exiting...")
        break

# Reminder function        
def reminder():
    print("Reminder\n")
    while(True):
        # Todo
        print("Exiting...")
        break      
  
# Clock function
def clock():
    print("Clock")
    while(True):
        phone_setting_guard = """
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        0. Exit
        """
        print(phone_setting_guard)
        print()
        clock_input = int(input("Enter Option"))
        match(clock_input):
               
          case 1: 
               print("Alarm clock")
          case 2: 
               print("Clock settings")
          case 3: 
               print("Date setting")
          case 4: 
               print("Stopwatch")  
          case 5: 
               print("Date setting")
          case 6: 
               print("Stopwatch")
          case 7: 
               print("Countdown timer")  
          case 8: 
               print("Date setting")
          case 9: 
               print("Auto update of date and time")
          case 0:
               print("Exiting...")
               break
          case _: 
               print("Invalid selection")
               
# Profile function        
def profile():
    print("Profile\n")
    while(True):
        # Todo
        print("Exiting...")
        break    

# Service function        
def service():
    print("Service\n")
    while(True):
        # Todo
        print("Exiting...")
        break

# SIM Service function        
def sim_service():
    print("SIM Services\n")
    while(True):
        # Todo
        print("Exiting...")
        break
        
# RUN FUNCTION
nokia_5510_main()
