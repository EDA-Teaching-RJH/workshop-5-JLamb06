import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}")
			break 
		else: 
			print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status():
	viewed = False
	while viewed == False:
		terminal1 = input("Would you like to view the systems, the crew or the resources? ")
		terminal = terminal1.lower().strip()
		if terminal == "systems":
			print(ship["systems"])
			again = input("Would you like to view another? ")
			again = again.lower().strip()
			if again == "yes":
				viewed == False
			else:
				viewed == True
		elif terminal == "resources":
			print(ship["resources"])
			again = input("Would you like to view another? ")
			again = again.lower().strip()
			if again == "yes":
				viewed == False
			else:
				viewed == True
		elif terminal == "crew":
			print(ship["crew"])
			again = input("Would you like to view another? ")
			again = again.lower().strip()
			if again == "yes":
				viewed == False
			else:
				viewed == True
		else:
			print("That is not a stat. ")
# TO: Implement function to display ship status, resources, and crew 

def get_user_action(): 
	Actions1 = int(input("Enetr a number between 1 and 4: "))
	return Actions1
# TO: Implement function to get and return user's chosen action 

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 
	
# TO: Implement system repair functionality
 
def add_crew_member(): 
# TO: Implement functionality to add a new crew member 
	print("!")
def handle_random_event():
	print("!")
# TO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
	#energy = 1000
	#torpedoes = 10
	if resource == "energy":
		ship["resources"]["energy"] -= amount
		if  ship["resurces"]["energy"] < 0:
			print("You don't have enough energy for that.")
			ship["resources"]["energy"] += amount
	elif resource == "torpedoes":
		if ship["resources"]["torpedoes"] < 0:
			print("You don't have any torpedoes left for that.")
			ship["resources"]["torpedoes"] += amount
	# TO: Implement resource usage logic 

def replenish_resources(): 
	ship["resources"]["energy"] += random.randint(1,300)
	if ship["resources"]["energy"] > 1000:
		ship["resources"]["energy"] == 1000
	ship["resources"]["torpedoes"] += random.randint(1,5)
	if ship["resources"]["torpedoes"] > 10:
		ship["resources"]["torpedoes"] == 10
# TO: Implement resource replenishment logic 

main()
