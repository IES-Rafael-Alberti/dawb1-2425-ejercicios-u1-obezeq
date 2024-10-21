#!/usr/bin/env python3
# ┌──────────────────────┐
# │ Fantasma Game ~ v1.0 │
# │──────────────────────│
# │ Coded by @obezeq     │
# │ github.com/obezeq    │
# └──────────────────────┘

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────

# DEPENDENCIES
import random
import json
import time
import os

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────

# GLOBAL VARIABLES
global data_file
data_file = "fantasma_data.json"

# ANSI COLOR CODES CLASS
class Colors:
    """ ANSI color codes """
    WHITE = "\033[1;37m"
    GREEN = "\033[1;32m"
    RED = "\033[0;31m"
    BROWN = "\033[0;33m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    LIGHT_BLUE = "\033[1;34m"
    END = "\033[0m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    BOLD = "\033[1m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    WELCOME = ["\033[0;30m", "\033[0;37m", WHITE, RED, BROWN, YELLOW, GREEN, "\033[1;36m", LIGHT_BLUE, BLUE, "\033[0;35m", "\033[1;35m"]

# REFRESH TERMINAL FUNCTION
def refresh():
    """Refresh terminal"""
    os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
    with open("banner_fantasma.txt", 'r') as f:
        banner = f.read()
        print(f"{Colors.END}{Colors.GREEN}{banner}{Colors.END}")
        f.close()

# WELCOME SCREEN
def welcome():
    """Welcome screen"""
    try:
        
        # Ghost Frames Set-up
        frames = []
        for i in range(69):
            space = ' ' * i
            image = f"""{space} .-.\n{space}(o o)\n{space}| O |\n{space}|   |\n{space}'~~~'"""
            frames.append(image)
        
        # Starting welcome screen by openning the banner of the game.
        with open("banner_fantasma.txt", 'r') as f:
            banner = f.read()
            
            # Multicolor Banner Screen
            for c in Colors.WELCOME:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Colors.END}{c}{banner}")
                time.sleep(0.19)
                
            # Ghost screen
            for frame in frames:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Colors.GREEN}{Colors.BOLD}{frame}")
                time.sleep(0.0033)
                
            # Final Welcome screen
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Colors.GREEN}{banner}{Colors.END}")
            f.close()
            
            # Setup Game Title
            os.system('title FANTASMA') if os.name == 'nt' else os.system('echo -ne "\033]0;FANTASMA\007"')
        return True
    
    # If the banner file of the game is not found, it will return an error.
    except FileNotFoundError:
        return FileNotFoundError(f"{Colors.RED}[-] ERROR: Necesitas el archivo 'banner_fantasma.txt'{Colors.WHITE}")

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────

# SAVES THE UPDATED PLAYER DATA BACK TO THE JSON FILE
def save_player_data(data):
    """Saves the updated player data back to the JSON file"""
    try:
        with open(data_file, 'w') as json_file:
            json.dump(data, json_file, indent=1)
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Saving Player Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# CREATE NEW USER DATA FOR NEW PLAYERS
def new_player_data(name):
    """Create new user data for new players"""
    try:
        data = {
            "options": {
                "mode": [1, 100]
            },
            "player_stats": {
                "name": name,
                "attempts": 0,
                "deaths": 0,
                "wins": 0,
                "best_score": None,
                "last_guess": 0
            }
        }
        
        save_player_data(data)
        return data
    
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Creating NEW Player Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# LOADS THE PLAYER DATA FROM A JSON FILE
def load_player_data():
    """Loads the player data from a JSON file"""
    try:
        with open(data_file, 'r') as json_file:
            json_content = json_file.read().strip()
            return json.loads(json_content)
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Loading Player Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# READ DATA FILE AND RETURN THE CONTENT OF IT
def read_file():
    """Read data file and return the content of it"""
    try:
        with open(data_file, 'r') as json_file:
            json_content = json_file.read()
            return json_content
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Reading the Json Player Data Content, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# SAVES THE UPDATED PLAYER DATA BACK TO THE JSON FILE
def save_player_data(data):
    """Saves the updated player data back to the JSON file"""
    try:
        with open(data_file, 'w') as json_file:
            json.dump(data, json_file, indent=1)
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Saving the Player Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# CREATE NEW PLAYER PROFILE & LOADS THE PLAYER DATA FORM A JSON FILE OR CREATES IT IF IT DOENS'T EXISTS
def new_player():
    """Create new player profile & loads the player data from a JSON file or creates it if it doesn't exist."""
    
    try:
        # CHECK IF THE JSON FILE EXISTS
        if os.path.exists(data_file):
            
            # READING CONTENT FROM JSON DATA
            loaded_data = read_file()
            
            # IF THE FILE IS EMPTY => CREATE NEW USER DATA FOR NEW PLAYERS
            if loaded_data.strip().replace(' ', '') == "": 
                name = input(f"{Colors.END}{Colors.GREEN}[+]{Colors.WHITE} {Colors.UNDERLINE}What's your name?{Colors.END} {Colors.GREEN}")
                fantasma_data = new_player_data(name)
            else:
                try:
                    # TRY LOADING THE DATA FILE
                    fantasma_data = json.loads(loaded_data)
                    
                    # CREATE NEW USER DATA FOR NEW PLAYERS
                    if fantasma_data["player_stats"]["name"] is None or fantasma_data["player_stats"]["name"].replace(' ', '') == "":
                        name = input(f"{Colors.END}{Colors.GREEN}[+]{Colors.WHITE} {Colors.UNDERLINE}What's your name?{Colors.END} {Colors.GREEN}")
                        fantasma_data = new_player_data(name)
                        
                # IF THE JSON IS CORRUPTED => RECREATE DATA
                except json.JSONDecodeError as e:
                    name = input(f"{Colors.END}{Colors.GREEN}[+]{Colors.WHITE} {Colors.UNDERLINE}What's your name?{Colors.END} {Colors.GREEN}")
                    fantasma_data = new_player_data(name)
                    
        # IF THE FILE DOESN'T EXIST => RECREATE DATA
        else:
            name = input(f"{Colors.END}{Colors.GREEN}[+]{Colors.WHITE} {Colors.UNDERLINE}What's your name?{Colors.END} {Colors.GREEN}")
            fantasma_data = new_player_data(name)
        
        # RETURN GAME DATA
        refresh()
        return fantasma_data
    
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Creating/Loading Player Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# UPDATES THE GAME OPTIONS AND SAVES THEM TO THE JSON FILE
def update_data(new_options):
    """Updates the game options and saves them to the JSON file"""     
    
    try:
        # Load existing data
        data = load_player_data()
        
        # Update options
        data = new_options
        
        # Save updated data back to the JSON file
        save_player_data(data)
    except Exception as e:
        print(f"{Colors.RED}[-] {Colors.BOLD}{Colors.UNDERLINE}ERROR FOUND while Updating Data, please update this error at fantasma.com/bugs:{Colors.END} \n{Colors.YELLOW}{e}{Colors.WHITE}")
        os._exit(0)

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────

# CALC THE VARIATION FROM USER INPUT TO GHOST POSITION
def calc_variation(bid: int, ghost: int, mode: list) -> tuple[int, any]:
    """CALC THE VARIATION FROM USER INPUT TO GHOST POSITION"""
    variation = abs(bid - ghost)
    variation_percentage = (variation / mode) * 100
    return variation, variation_percentage

# PLAY GAME
def game(fantasma_data):
    """PLAY GAME - The ghost will be in a range based in the mode selected by the user, and the user will need to find it by guessing in which position the ghost is."""
    refresh()
    
    mode = fantasma_data["options"]["mode"] # Load settings
    ghost = random.randrange(mode[0], (mode[1]+1)) # Create the ghost position
    
    attempt = 1
    
    # GAME STARTS
    while True:
        bid = input(f"\n{Colors.END}{Colors.GREEN}{Colors.BOLD}[+]{Colors.WHITE} {Colors.UNDERLINE}¿Donde esta el fantasma?{Colors.END}{Colors.WHITE} ({mode[0]} - {mode[1]}) ~> {Colors.BOLD}").strip().replace(' ', '').lower()
        
        # If the input introduced is a number:
        if bid.isdigit():
            # If the input introduced is an integer
            if float(bid).is_integer():
                # Convert user input to integer
                bid = int(bid)
                
                # Calc variation from User Input to the Ghost Position
                variationts = calc_variation(bid, ghost, mode[1])
                variation = variationts[0]
                variation_percentage = variationts[1]
                
                # If the user found the ghost (ghost & user input difference = 0)
                if variation == 0:
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.RED}¡Quemado!{Colors.END}{Colors.WHITE} Has encontrado al fantasma en {Colors.GREEN}{attempt}{Colors.END} intentos :D{Colors.END}")
                    
                    # Update & Save STATS
                    best_score = fantasma_data["player_stats"]["best_score"]
                    if best_score is None:
                        fantasma_data["player_stats"]["best_score"] = attempt
                    else:
                        if attempt < best_score:
                            fantasma_data["player_stats"]["best_score"] = attempt
                        
                    fantasma_data["player_stats"]["attempts"] += attempt
                    fantasma_data["player_stats"]["last_guess"] = attempt
                    fantasma_data["player_stats"]["wins"] += 1
                    
                    new_options = fantasma_data
                    update_data(new_options)
                    
                    # Ask user to continue the game and return to menu
                    input(f"\n{Colors.END}{Colors.WHITE}Presiona {Colors.BOLD}[ {Colors.NEGATIVE}ENTER{Colors.END} {Colors.WHITE}{Colors.BOLD}]{Colors.END}{Colors.WHITE} para continuar ")
                    refresh()
                    
                    break
                
                # If the user hasn't found the ghost (tell the user how far the ghost is)
                elif variation_percentage <= 5:  # 0-5% del rango (Hot)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.RED}¡Caliente!{Colors.END}{Colors.WHITE} Estás muy cerca.{Colors.END}")
                elif variation_percentage <= 15:  # 6-15% del rango (Tempering)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.YELLOW}¡Templado!{Colors.END}{Colors.WHITE} Estás cerca.{Colors.END}")
                elif variation_percentage <= 30:  # 16-30% del rango (Normal)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.BROWN}¡Normal!{Colors.END}{Colors.WHITE} Estás a una buena distancia.{Colors.END}")
                elif variation_percentage <= 50:  # 31-50% del rango (Cold)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.LIGHT_BLUE}¡Frío!{Colors.END}{Colors.WHITE} Estás algo lejos.{Colors.END}")
                elif variation_percentage <= 80:  # 51-80% del rango (Intense Cold)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.BLUE}¡Frío intenso!{Colors.END}{Colors.WHITE} Estás muy lejos.{Colors.END}")
                elif variation_percentage <= 90: # 81-90% del rango (Freezing)
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.NEGATIVE}{Colors.LIGHT_BLUE}¡Congelando!{Colors.END}{Colors.WHITE} Estás demasiado lejos.{Colors.END}")
                
                # 91-100% difference from ghost (The user freezes to death)
                else:
                    print(f"{Colors.END}{Colors.BOLD}{Colors.UNDERLINE}{Colors.RED}¡{Colors.CROSSED}MUERTO{Colors.END}{Colors.WHITE}!{Colors.END}{Colors.WHITE} Te has {Colors.NEGATIVE}congelado{Colors.END}{Colors.WHITE} vivo.{Colors.END}")
                    
                    # Update & Save STATS
                    fantasma_data["player_stats"]["attempts"] += attempt
                    fantasma_data["player_stats"]["deaths"] += 1
                    new_options = fantasma_data
                    update_data(new_options)
                    
                    # Ask user to continue the game and return to menu
                    input(f"\n{Colors.END}{Colors.WHITE}Presiona {Colors.BOLD}[ {Colors.NEGATIVE}ENTER{Colors.END} {Colors.WHITE}{Colors.BOLD}]{Colors.END}{Colors.WHITE} para continuar ")
                    refresh()
                    
                    break
                
                attempt += 1
                
            # If the input introduced is NOT an integer number
            else:
                print(f"{Colors.END}{Colors.RED}:O{Colors.WHITE} No has introducido un {Colors.RED}número {Colors.CROSSED}entero{Colors.END}{Colors.WHITE}, {Colors.BOLD}inténtalo de nuevo.{Colors.END}{Colors.WHITE}")
                
        # If the input introduced is NOT a number
        else:
            # If the input introduced is "exit", then exit the game and return to menu
            if bid == "exit":
                refresh()
                break
            else:
                print(f"{Colors.END}{Colors.RED}:O{Colors.WHITE} No has introducido un {Colors.RED}{Colors.CROSSED}número{Colors.END}{Colors.WHITE}, {Colors.BOLD}inténtalo de nuevo.{Colors.END}{Colors.WHITE}")

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────
# MENU - Mode
def menu_mode(fantasma_data):
    """MENU - Mode"""
    refresh()
            
    print(f"{Colors.GREEN}┌──────────┐")
    print(f"│   {Colors.UNDERLINE}MODE{Colors.END}{Colors.GREEN}   │")
    print("└──────────┘")
    print(f"{Colors.GREEN}[1] {Colors.UNDERLINE}NOOB{Colors.END}{Colors.WHITE} (1-10)") if fantasma_data["options"]["mode"] == [1, 10] else print(f"{Colors.GREEN}[1]{Colors.WHITE} NOOB (1-10)")
    print(f"{Colors.GREEN}[2] {Colors.UNDERLINE}EASY{Colors.END}{Colors.WHITE} (1-50)") if fantasma_data["options"]["mode"] == [1, 50] else print(f"{Colors.GREEN}[2]{Colors.WHITE} EASY (1-50)")
    print(f"{Colors.GREEN}[3] {Colors.UNDERLINE}NORMAL{Colors.END}{Colors.WHITE} (1-100)") if fantasma_data["options"]["mode"] == [1, 100] else print(f"{Colors.GREEN}[3]{Colors.WHITE} NORMAL (1-100)")
    print(f"{Colors.GREEN}[4] {Colors.UNDERLINE}HARD{Colors.END}{Colors.WHITE} (1-500)") if fantasma_data["options"]["mode"] == [1, 500] else print(f"{Colors.GREEN}[4]{Colors.WHITE} HARD (1-500)")
    print(f"{Colors.GREEN}[5] {Colors.UNDERLINE}CRAZY{Colors.END}{Colors.WHITE} (1-1000)") if fantasma_data["options"]["mode"] == [1, 1000] else print(f"{Colors.GREEN}[5]{Colors.WHITE} CRAZY (1-1000)")
    
    # ASK USER INPUT
    mode = input(f"\n{Colors.GREEN}~>{Colors.WHITE} ").lower().strip().replace(' ', '')
    
    # CHANGE MODES
    if mode == "1" or mode == "noob":
        fantasma_data["options"]["mode"] = [1,10]
    elif mode == "2" or mode == "easy":
        fantasma_data["options"]["mode"] = [1,50]
    elif mode == "3" or mode == "normal":
        fantasma_data["options"]["mode"] = [1,100]
    elif mode == "4" or mode == "hard":
        fantasma_data["options"]["mode"] = [1,500]
    elif mode == "5" or mode == "crazy":
        fantasma_data["options"]["mode"] = [1,1000]
    
    # UPDATE MODE DATA
    update_data(fantasma_data)
        
    refresh()

# MENU - Stats
def menu_stats(fantasma_data):
    """MENU - Stats"""
    refresh()

    # PRINT USER STATS
    print(f"{Colors.GREEN}┌───────────┐")
    print(f"│   {Colors.UNDERLINE}STATS{Colors.END}{Colors.GREEN}   │")
    print("└───────────┘")
    print(f'{Colors.GREEN}• Name: {Colors.WHITE}: {fantasma_data["player_stats"]["name"]}')
    print(f'{Colors.GREEN}• Attempts{Colors.WHITE}: {fantasma_data["player_stats"]["attempts"]}')
    print(f'{Colors.GREEN}• Deaths{Colors.WHITE}: {fantasma_data["player_stats"]["deaths"]}')
    print(f'{Colors.GREEN}• Wins{Colors.WHITE}: {fantasma_data["player_stats"]["wins"]}')
    print(f'{Colors.GREEN}• Best score{Colors.WHITE}: 0') if fantasma_data["player_stats"]["best_score"] is None else print(f'{Colors.GREEN}• Best score{Colors.WHITE}: {fantasma_data["player_stats"]["best_score"]}')
    print(f'{Colors.GREEN}• Last guess{Colors.WHITE}: {fantasma_data["player_stats"]["last_guess"]}')
    
    input()
    refresh()

# MENU - Profile
def menu_profile(fantasma_data):
    """MENU - Profile"""
    refresh()
    print(f"{Colors.GREEN}┌─────────────┐")
    print(f"│   {Colors.UNDERLINE}PROFILE{Colors.END}{Colors.GREEN}   │")
    print("└─────────────┘")
    print(f'{Colors.GREEN}[1] Name: {Colors.WHITE}{fantasma_data["player_stats"]["name"]}')
    print(f'{Colors.GREEN}[2] Exit{Colors.WHITE}')
    
    # ASK USER INPUT
    edit = input(f"\n{Colors.GREEN}~>{Colors.WHITE} ").lower().strip().replace(' ', '')
    
    # EDIT NAME
    if edit == "1" or edit == "edit":
        # ASK NAME EDIT
        name = input(f"\n{Colors.GREEN}[+] {Colors.UNDERLINE}Change your name:{Colors.END} {Colors.WHITE}")
        
        # UPDATE NAME DATA
        fantasma_data["player_stats"]["name"] = name
        update_data(fantasma_data)
        
    refresh()

# MENU
def menu(fantasma_data):
    """MENU OF THE GAME"""
    while True:
        print(f"{Colors.GREEN}┌──────────┐")
        print(f"│   {Colors.UNDERLINE}MENU{Colors.END}{Colors.GREEN}   │")
        print("└──────────┘")
        print(f"{Colors.GREEN}[1]{Colors.WHITE} PLAY")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} MODE")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} STATS")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} PROFILE")
        print(f"{Colors.GREEN}[5]{Colors.WHITE} EXIT")
        
        # ASK USER TO CHOOSE A MENU OPTION
        choice = input(f"\n{Colors.GREEN}~>{Colors.WHITE} ").lower().strip().replace(' ', '')
        
        # PLAY GAME
        if choice == "play" or choice == "jugar" or choice == "1":
            return fantasma_data
        
        # LOAD MODE OPTIONS
        elif choice == "mode" or choice == "modo" or choice == "2":
            menu_mode(fantasma_data)
            
        # LOAD PLAYER STATS
        elif choice == "stats" or choice == "estadisticas" or choice == "3":
            menu_stats(fantasma_data)
            
        # LOAD PROFILE SETTINGS
        elif choice == "profile" or choice == "perfil" or choice == "4":
            menu_profile(fantasma_data)
            
        # EXIT GAME
        elif choice == "exit" or choice == "salir" or choice == "5":
            os._exit(0)
        
        # REFRESH TERMINAL IF USER DOESN'T INTRODUCE ANY OPTION GIVEN AND ASK AGAIN
        else:
            refresh() 
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────

# MAIN FUNCTION
def main():
    """Main Function"""
    
    # WELCOME SCREEN - Starting Game
    welcome_status = welcome()
    
    # IF BANNER FILE IS NOT FOUND
    if isinstance(welcome_status, FileNotFoundError):
        print(welcome_status)
        os._exit(0)
        
    # LOAD GAME
    elif welcome_status:
        
        # LOAD PLAYER DATA OR CREATE ONE
        fantasma_data = new_player()
        
        # START GAME
        while True:
            # START MENU
            fantasma_data = menu(fantasma_data)
            
            # PLAY GAME
            game(fantasma_data)

# HERE THE PROGRAM STARTS A NEW ADVENTURE...
if __name__ == '__main__':
    main()