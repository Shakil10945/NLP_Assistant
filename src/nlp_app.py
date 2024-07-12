import logging
from .nlp_model import NLPModel

class NLPApp(NLPModel):
    def __init__(self):
        try:
            self.__database = {}
            self.__first_menu()
        except Exception as e:
            logging.error("Error initializing NLPApp: %s", e)

    def __first_menu(self):
        try:
            first_input = input("""
            Hi! How would you like to proceed?
            
            1. Not a member? Register
            2. Already a member? Login
            3. Otherwise, Exit
            """)

            logging.info("User selected option: %s", first_input)

            if first_input == '1':
                # Register
                self.__register()
            elif first_input == '2':
                # Login
                self.__login()
            else:
                logging.info("User chose to exit.")
                exit()
        except Exception as e:
            logging.error("Error in first_menu: %s", e)

    def __second_menu(self):
        try:
            second_input = input("""
            Hi! How would you like to proceed?
            
            1. Sentiment Analysis
            2. Language Translation
            3. Language Detection
            """)

            logging.info("User selected option: %s", second_input)

            if second_input == '1':
                # Sentiment Analysis
                self.__sentiment_analysis()
            elif second_input == '2':
                # Translation
                self.__language_translation()
            elif second_input == '3':
                # Language Detection
                self.__language_detection()
            else:
                logging.info("User chose to exit.")
                exit()
        except Exception as e:
            logging.error("Error in second_menu: %s", e)
    
    def __register(self):
        try:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            logging.info("Attempting to register user: %s", email)

            if email in self.__database:
                logging.warning("Registration failed. Email already exists: %s", email)
                print("Email already exists")
                self.__first_menu()
            else:
                self.__database[email] = [name, password]
                logging.info("Registration successful for user: %s", email)
                print("Registration successful. Now you can login!")
                self.__first_menu()
        except Exception as e:
            logging.error("Error during registration: %s", e)

    def __login(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            logging.info("Attempting to login user: %s", email)

            if email in self.__database:
                if self.__database[email][1] == password:
                    logging.info("Login successful for user: %s", email)
                    print("Login successful")
                    self.__second_menu()
                else:
                    logging.warning("Login failed. Wrong password for user: %s", email)
                    print("Wrong password, try again")
                    self.__login()
            else:
                logging.warning("Login failed. Email not registered: %s", email)
                print("This email is not registered yet")
                self.__first_menu()
        except Exception as e:
            logging.error("Error during login: %s", e)

    def __sentiment_analysis(self):
        try:
            user_text = input("Enter your text: ")
            logging.info("Performing sentiment analysis for text: %s", user_text)
            model = super().get_model()
            response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
            results = response.text
            logging.info("Sentiment analysis result: %s", results)
            print(results)
            self.__second_menu()
        except Exception as e:
            logging.error("Error during sentiment analysis: %s", e)

    def __language_translation(self):
        try:
            user_text = input("Enter your text: ")
            logging.info("Performing language translation for text: %s", user_text)
            model = super().get_model()
            response = model.generate_content(f"Give me the Bengali translation of this sentence: {user_text}")
            results = response.text
            logging.info("Language translation result: %s", results)
            print(results)
            self.__second_menu()
        except Exception as e:
            logging.error("Error during language translation: %s", e)
        
    def __language_detection(self):
        try:
            user_text = input("Enter your text: ")
            logging.info("Performing language detection for text: %s", user_text)
            model = super().get_model()
            response = model.generate_content(f"Detect the language of this sentence: {user_text}")
            results = response.text
            logging.info("Language detection result: %s", results)
            print(results)
            self.__second_menu()
        except Exception as e:
            logging.error("Error during language detection: %s", e)
