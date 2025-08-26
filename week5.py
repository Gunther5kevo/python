# Base class: Person
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce(self):
        return f"My name is {self.name}, I'm {self.age} years old from {self.nationality}."


# Child class: Player (inherits Person)
class Player(Person):
    def __init__(self, name, age, nationality, position, goals=0):
        super().__init__(name, age, nationality)
        self.position = position
        self.goals = goals

    def introduce(self):  # Polymorphism (method override)
        return f"{self.name} plays as a {self.position} for Chelsea FC."

    def score_goal(self):
        self.goals += 1
        return f"⚽ GOAL! {self.name} has now scored {self.goals} goals."


# Another child class: Coach (inherits Person)
class Coach(Person):
    def __init__(self, name, age, nationality, tactic):
        super().__init__(name, age, nationality)
        self.tactic = tactic

    def introduce(self):  # Polymorphism again
        return f"{self.name} is the Chelsea coach. Preferred tactic: {self.tactic}."


# Chelsea FC class to hold players and coach
class ChelseaFC:
    def __init__(self, coach):
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def team_info(self):
        info = f"Coach: {self.coach.name}\nPlayers:\n"
        for p in self.players:
            info += f"- {p.name}, {p.position}, Goals: {p.goals}\n"
        return info


# --- Testing our classes ---
# Create coach
poch = Coach("Mauricio Pochettino", 51, "Argentina", "4-3-3")

# Create players
sterling = Player("cole Palmer", 29, "England", "attacker")
enzo = Player("Enzo Fernández", 23, "Argentina", "Midfielder")

# Create Chelsea team
chelsea = ChelseaFC(poch)
chelsea.add_player(sterling)
chelsea.add_player(enzo)

# Show outputs
print(poch.introduce())
print(sterling.introduce())
print(enzo.score_goal())
print(chelsea.team_info())
