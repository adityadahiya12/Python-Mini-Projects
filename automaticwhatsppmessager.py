import pywhatkit 

print(pywhatkit.sendwhatmsg("+919899688566", "This is a automatic WhatsApp message tutorial",19,2))
# pip install pywhatkit 
# import pywhatkit


# # Setup logging
# logging.basicConfig(filename="whatsapp_message_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

# def is_valid_number(number):
#     return bool(re.fullmatch(r"\+\d{10,13}", number.strip()))

# def get_user_input():
#     number = input("Enter phone number with country code (e.g., +919899688566): ").strip()
#     while not is_valid_number(number):
#         print("Invalid number format. Please try again.")
#         number = input("Enter phone number with country code (e.g., +919899688566): ").strip()
    
#     message = input("Enter your message: ").strip()
    
#     hour = int(input("Enter hour (24-hour format): "))
#     minute = int(input("Enter minute: "))
    
#     return number, message, hour, minute

# def send_whatsapp_message():
#     try:
#         number, message, hour, minute = get_user_input()
#         print(f"Scheduling message to {number} at {hour}:{minute}...")
#         pywhatkit.sendwhatmsg(number, message, hour, minute)
#         logging.info(f"Sent message to {number}: {message}")
#         print("Message successfully scheduled!")
#     except Exception as e:
#         logging.error(f"Failed to send message: {str(e)}")
#         print(f"Something went wrong: {e}")

# if __name__ == "__main__":
#     send_whatsapp_message()
