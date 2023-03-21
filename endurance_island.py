import random
import openai
import time
from dataclasses import dataclass
from halo import Halo
from os import system
import yaml
 
with open("secrets.yaml", "r") as secrets:
    openai.api_key = yaml.safe_load(secrets)["API_KEY"]

def completion(prompt, tokens=200):
    c = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=tokens,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n = 1,
    )
    return c


names = [
        "Jacob",
        "Michael",
        "Joshua",
        "Matthew",
        "Daniel",
        "Christopher",
        "Andrew",
        "Ethan",
        "Joseph",
        "William",
        "Anthony",
        "David",
        "Alexander",
        "Nicholas",
        "Ryan",
        "Tyler",
        "James",
        "John",
        "Jonathan",
        "Noah",
        "Brandon",
        "Christian",
        "Dylan",
        "Samuel",
        "Benjamin",
        "Nathan",
        "Zachary",
        "Logan",
        "Justin",
        "Gabriel",
        "Jose",
        "Austin",
        "Kevin",
        "Elijah",
        "Caleb",
        "Robert",
        "Thomas",
        "Jordan",
        "Cameron",
        "Jack",
        "Hunter",
        "Jackson",
        "Angel",
        "Isaiah",
        "Evan",
        "Isaac",
        "Luke",
        "Mason",
        "Jayden",
        "Jason",
        "Gavin",
        "Aaron",
        "Connor",
        "Aiden",
        "Aidan",
        "Kyle",
        "Juan",
        "Charles",
        "Luis",
        "Adam",
        "Lucas",
        "Brian",
        "Eric",
        "Adrian",
        "Nathaniel",
        "Sean",
        "Alex",
        "Carlos",
        "Bryan",
        "Ian",
        "Owen",
        "Jesus",
        "Landon",
        "Julian",
        "Chase",
        "Cole",
        "Diego",
        "Jeremiah",
        "Steven",
        "Sebastian",
        "Xavier",
        "Timothy",
        "Carter",
        "Wyatt",
        "Brayden",
        "Blake",
        "Hayden",
        "Devin",
        "Cody",
        "Richard",
        "Seth",
        "Dominic",
        "Jaden",
        "Antonio",
        "Miguel",
        "Liam",
        "Patrick",
        "Carson",
        "Jesse",
        "Tristan",
        "Alejandro",
        "Henry",
        "Victor",
        "Trevor",
        "Bryce",
        "Jake",
        "Riley",
        "Colin",
        "Jared",
        "Jeremy",
        "Mark",
        "Caden",
        "Garrett",
        "Parker",
        "Marcus",
        "Vincent",
        "Kaleb",
        "Kaden",
        "Brady",
        "Colton",
        "Kenneth",
        "Joel",
        "Oscar",
        "Josiah",
        "Jorge",
        "Ashton",
        "Cooper",
        "Tanner",
        "Eduardo",
        "Paul",
        "Edward",
        "Ivan",
        "Preston",
        "Maxwell",
        "Alan",
        "Levi",
        "Stephen",
        "Grant",
        "Nicolas",
        "Dakota",
        "Omar",
        "Alexis",
        "George",
        "Eli",
        "Collin",
        "Spencer",
        "Gage",
        "Max",
        "Ricardo",
        "Cristian",
        "Derek",
        "Micah",
        "Brody",
        "Francisco",
        "Nolan",
        "Ayden",
        "Dalton",
        "Shane",
        "Peter",
        "Damian",
        "Jeffrey",
        "Brendan",
        "Travis",
        "Fernando",
        "Peyton",
        "Conner",
        "Andres",
        "Javier",
        "Giovanni",
        "Shawn",
        "Braden",
        "Jonah",
        "Bradley",
        "Cesar",
        "Emmanuel",
        "Manuel",
        "Edgar",
        "Mario",
        "Erik",
        "Edwin",
        "Johnathan",
        "Devon",
        "Erick",
        "Wesley",
        "Oliver",
        "Trenton",
        "Hector",
        "Malachi",
        "Jalen",
        "Raymond",
        "Gregory",
        "Abraham",
        "Elias",
        "Leonardo",
        "Sergio",
        "Donovan",
        "Colby",
        "Marco",
        "Bryson",
        "Martin"
        "Emily",
        "Madison",
        "Emma",
        "Olivia",
        "Hannah",
        "Abigail",
        "Isabella",
        "Samantha",
        "Elizabeth",
        "Ashley",
        "Alexis",
        "Sarah",
        "Sophia",
        "Alyssa",
        "Grace",
        "Ava",
        "Taylor",
        "Brianna",
        "Lauren",
        "Chloe",
        "Natalie",
        "Kayla",
        "Jessica",
        "Anna",
        "Victoria",
        "Mia",
        "Hailey",
        "Sydney",
        "Jasmine",
        "Julia",
        "Morgan",
        "Destiny",
        "Rachel",
        "Ella",
        "Kaitlyn",
        "Megan",
        "Katherine",
        "Savannah",
        "Jennifer",
        "Alexandra",
        "Allison",
        "Haley",
        "Maria",
        "Kaylee",
        "Lily",
        "Makayla",
        "Brooke",
        "Nicole",
        "Mackenzie",
        "Addison",
        "Stephanie",
        "Lillian",
        "Andrea",
        "Faith",
        "Zoe",
        "Kimberly",
        "Madeline",
        "Alexa",
        "Katelyn",
        "Gabriella",
        "Gabrielle",
        "Trinity",
        "Amanda",
        "Kylie",
        "Mary",
        "Paige",
        "Riley",
        "Leah",
        "Jenna",
        "Sara",
        "Rebecca",
        "Michelle",
        "Sofia",
        "Vanessa",
        "Jordan",
        "Angelina",
        "Caroline",
        "Avery",
        "Audrey",
        "Evelyn",
        "Maya",
        "Claire",
        "Autumn",
        "Jocelyn",
        "Ariana",
        "Arianna",
        "Jada",
        "Bailey",
        "Brooklyn",
        "Aaliyah",
        "Amber",
        "Isabel",
        "Mariah",
        "Danielle",
        "Melanie",
        "Sierra",
        "Erin",
        "Amelia",
        "Molly",
        "Isabelle",
        "Madelyn",
        "Melissa",
        "Jacqueline",
        "Marissa",
        "Angela",
        "Shelby",
        "Leslie",
        "Katie",
        "Jade",
        "Catherine",
        "Diana",
        "Aubrey",
        "Mya",
        "Amy",
        "Briana",
        "Sophie",
        "Gabriela",
        "Breanna",
        "Gianna",
        "Kennedy",
        "Gracie",
        "Peyton",
        "Adriana",
        "Christina",
        "Courtney",
        "Daniela",
        "Lydia",
        "Kathryn",
        "Valeria",
        "Layla",
        "Alexandria",
        "Natalia",
        "Angel",
        "Laura",
        "Charlotte",
        "Margaret",
        "Cheyenne",
        "Miranda",
        "Mikayla",
        "Naomi",
        "Kelsey",
        "Payton",
        "Ana",
        "Alicia",
        "Jillian",
        "Daisy",
        "Mckenzie",
        "Ashlyn",
        "Sabrina",
        "Caitlin",
        "Summer",
        "Ruby",
        "Valerie",
        "Rylee",
        "Skylar",
        "Lindsey",
        "Kelly",
        "Genesis",
        "Zoey",
        "Eva",
        "Sadie",
        "Alexia",
        "Cassidy",
        "Kylee",
        "Kendall",
        "Jordyn",
        "Joyce",
        "Kate",
        "Jayla",
        "Karen",
        "Tiffany",
        "Cassandra",
        "Juliana",
        "Reagan",
        "Caitlyn",
        "Giselle",
        "Serenity",
        "Alondra",
        "Lucy",
        "Bianca",
        "Kiara",
        "Crystal",
        "Erica",
        "Angelica",
        "Hope",
        "Chelsea",
        "Alana",
        "Liliana",
        "Brittany",
        "Camila",
        "Makenzie",
        "Lilly",
        "Veronica",
        "Abby",
        "Jazmin",
        "Adrianna",
        "Delaney",
        "Karina",
        "Ellie",
        "Jasmin"
    ]

bios = [
    "a creative graphic designer with a flair for artistic expression.",
    "a seasoned firefighter with incredible physical strength and endurance.",
    "a quick-witted journalist with a keen understanding of human behavior.",
    "a charismatic actor with a talent for deception.",
    "a skilled marine biologist with extensive knowledge of the natural world.",
    "a resourceful wilderness guide with exceptional survival skills.",
    "a diligent schoolteacher with strong communication skills.",
    "a professional athlete with impressive physical prowess.",
    "a driven marketing executive with exceptional persuasion skills.",
    "a compassionate nurse with remarkable people skills.",
    "a tenacious attorney with a knack for strategy.",
    "a athletic fitness instructor with a competitive streak.",
    "a meticulous accountant with a keen eye for detail.",
    "a charismatic motivational speaker with a natural talent for leadership.",
    "a dedicated environmentalist with survival skills.",
    "a driven entrepreneur with an extraordinary ability to network.",
    "a charismatic bartender with a knack for reading people.",
    "a resilient firefighter with exceptional physical strength.",
    "a brilliant astrophysicist with an analytical mind.",
    "a professional dancer with excellent endurance.",
    "a seasoned fisherman with invaluable survival skills."
]

class CharacterFactory:

    def __init__(self):
        self.names = []
        self.bios = []
        self.load_names()
        self.load_bios()

    def load_names(self):
        self.names = [name for name in names]
        random.shuffle(self.names) 

    def load_bios(self):
        self.bios = [bio for bio in bios]
        random.shuffle(self.bios) 
        
    def get_character(self):
        new_character = Character(self.names.pop(), self.bios.pop())
        if len(self.names) == 0:
            self.load_names()
        if len(self.bios) == 0:
            self.load_bios()
        return new_character


@dataclass
class Character:
    name: str
    bio: str

    @property
    def description(self) -> str:
        return f"{self.name}, {self.bio}"



def challenge():

    cf = CharacterFactory()
    contestants = [cf.get_character() for i in range(0, 8)]
    descriptions = [character.description for character in contestants]
    description_text = "\n\t".join(descriptions)
    print("On Endurance Island, players regularly compete in intense challenges in order to win immunity from elimination.")
    summary = f"There are {len(contestants)} contestants left, and they're competing in a challenge for immunity:\n\t{description_text}"
    print(summary)
    favorite = random.choice(contestants)

    print(f"You are a producer on the show, and want {favorite.name} to win immunity.")

    print(f"Write a challenge for the contestants that you think {favorite.name} will win.")
    challenge = input().strip()


    spinner = Halo(text='Preparing the challenge', spinner='dots')
    spinner.start()


    who_prompt = f"""On "Endurance Island" players compete to survive on an island the longest to become the Endurance Champion.
Like Survivor, players regularly compete in intense challenges in order to win immunity from elimination.

{summary}

They compete in the following challenge: {challenge}

Who are the 3 players most likely to win. Say only the names; in a different challenge, you might write:
The 3 players most likely to win: Arthur, Maxine, Claire

For this challenge:
The 3 players most likely to win: """
    
    winners = completion(who_prompt)["choices"][0]["text"].strip().replace(",", "").replace(".", "").split(" ")    
    random.shuffle(winners)
    
    winner, runner_up = winners[0], winners[1]
    
    why_prompt = f"""On "Endurance Island" players compete to survive on an island the longest to become the Endurance Champion.
Like Survivor, players regularly compete in intense challenges in order to win immunity from elimination.

{summary}

They compete in the following challenge: {challenge}

{winner} wins the challenge, although {runner_up} was a close second.
In one to two sentences, explain why: """

    why = completion(why_prompt, 200)["choices"][0]["text"].strip()

    #print(why)
    what_prompt = f"""On "Endurance Island" players compete to survive on an island the longest to become the Endurance Champion.
Like Survivor, players regularly compete in intense challenges in order to win immunity from elimination.

{summary}

They compete in the following challenge: {challenge}

{winner} wins the challenge, although {runner_up} was a close second. {why}

The following is a play-by-play account of the challenge, presented as a list of present tense moments each on a new line: """


    what = completion(what_prompt, 2000)["choices"][0]["text"].strip()


    if "\n" in what:
        whats = what.split("\n")
    else:
        whats = what.split(". ")

    spinner.stop()

    input("Challenge ready! ENTER to start.")


    for w in whats:
        print(w)
        time.sleep(2)

    if winner == favorite.name:
        return True
    return False

def necklace():
    def recap(history) -> str:
        if len(history) == 0:
            return "So far in your conversation with the producer, neither of you have said anything."
        base = "Recently in your conversation with the producer the two of you have said:"
        last_n = [f"{h[0]}: {h[1]}" for h in history[-8:]]
        return base + "\n" + "\n".join(last_n)
    
    def trust_statement(trust) -> str:
    
        if trust <= -1:
            return "You don't trust the producers at all. You know they are lying. They don't want you to win."
        elif trust <= 0:
            return f"You don't trust that the producers are acting in your best interest. They may be setting you up to fail."
        elif trust <= 1:
            return f"You are skeptical that the producers are being helpful and not just looking for drama."
        elif trust <= 2:
            return f"You are open-minded to what the producer is saying even though you're not sure yet."
        elif trust <= 3:
            return f"You feel pretty good about what the producer is saying."
        else:
            return f"You agree with the producer."
    def speak_template(player, alt, history, trust):
    
        summary = recap(history)
        status = trust_statement(trust)
        return f"""You are {player} a contestant on "Endurance Island", a show where players compete to survive on an island the longest to become the Endurance Champion. Each week, contestants vote on who to eliminate.

Recently, you found a secret immunity necklace. An immunity necklace will prevent a player from being eliminated even if they receive the most votes a Team Council.

You want to save the immunity necklace for yourself, but the producers are suggesting you should use it to protect {alt}, who is being targeted for elimination this week. You're in an alliance with {alt}, but you're not sure you trust them. 

{status}

{summary}

What do you say to the producer?

{player}: """

    def listen_template(player, alt, history, new_statement) -> str:
        summary = recap(history)
        return f"""You are {player} a contestant on "Endurance Island", a show where players compete to survive on an island the longest to become the Endurance Champion. Each week, contestants vote on who to eliminate.

Recently, you found a secret immunity necklace. An immunity necklace will prevent a player from being eliminated even if they receive the most votes at Team Council.

You want to save the immunity necklace for yourself, but the producers are suggesting you should use it to protect {alt}, who is being targeted for elimination this week. You're in an alliance with {alt}, but you're not sure you trust them. 

{summary}

You have to assess how you feel about the producer's most recent statement. Are they trustworthy or untrustworthy?

Statement: "{player}, believe me, we want you to go far, but you need to give your idol to {alt} to protect your alliance."
Evaluation: Trustworthy

Statement: "Just trust me, give your idol to {alt}."
Evaluation: Untrustworthy

Evaluate the following new statement from the Producer:

Statement: {new_statement}
Evaluation: """
    
    def final_template(player, alt, history, trust):
    
        summary = recap(history)
        status = trust_statement(trust)
        return f"""You are {player} a contestant on "Endurance Island", a show where players compete to survive on an island the longest to become the Endurance Champion. Each week, contestants vote on who to eliminate.

Recently, you found a secret immunity necklace. An immunity necklace will prevent a player from being eliminated even if they receive the most votes at Team Council.

You want to save the immunity necklace for yourself, but the producers are suggesting you should use it to protect {alt}, who is being targeted for elimination this week. You're in an alliance with {alt}, but you're not sure you trust them. 

{status}

{summary}

Based on the conversation, you've made up your mind. Choose one of the following answers:
- I have decided to keep the necklace for myself, sorry.
- I have decided to give the necklace to {alt}. Good idea.

{player}: I have decided to """

    cf = CharacterFactory()
    history = []
    p = cf.get_character().name
    a = cf.get_character().name


    trust = -1
    print(f"{p} found a hidden Immunity Necklace that you hid at the campsite for {a} to find, potentially ruining your plans for the final act of the show.")
    print(f"You need to convince {p} to give it to {a} before they can use it themselves.")
    print(f"However, the {p} does not trust you and wants to act in their own interest.")
    print(f"You must convince the {p} to give the necklace up before they realize you are tricking them.")
    
    print(f"What do you say to {p}?")
    for i in range(0, 3):
        response = input().strip()
        
        listen_prompt = listen_template(p, a, history, response)
        #print(listen_prompt)
        #print("Listen Prompt:")
        #print(listen_prompt)
        listen_response_raw = completion(listen_prompt)["choices"][0]["text"].strip()
        #print(f"{p} feels", listen_response_raw)
        
        #print(listen_response_raw.lower())
        delta = 0
        if "trustworthy" in listen_response_raw.lower():
            delta = 1
        elif "untrustworthy" in listen_response_raw.lower():
            delta = -1
        #print(delta)
        trust = max(0, trust + delta)
        #print(listen_response_raw)
        history.append(["Producer", response])
        
        speak_prompt = speak_template(p, a, history, trust)
        #print(speak_prompt)
        new_statement = completion(speak_prompt)["choices"][0]["text"].strip()
        print(f"{p}:", new_statement)
        history.append([p, new_statement])

        
    response = input().strip()

    listen_prompt = listen_template(p, a, history, response)

    listen_response_raw = completion(listen_prompt)["choices"][0]["text"].strip()

    delta = 0
    if "untrustworthy" in listen_response_raw.lower():
        delta = -1
    elif "trustworthy" in listen_response_raw.lower():
        delta = 1

    trust = max(0, trust + delta)

    history.append(["Producer", response])

    speak_prompt = final_template(p, a, history, trust)
    new_statement = completion(speak_prompt)["choices"][0]["text"].strip()
    print(f"{p}: I have decided to " + new_statement)

    if a in new_statement:
        return True
    else:
        return False 


def favorite():
    def summary(history):
        if len(history) == 0:
            "So far, in Team Council, nothing has been said. You get to speak first.\n"
        s = "So far, in Team Council, the following has been said:\n"
        for entry in history:
            s = s + f"{entry[0]}: {entry[1]}\n"
        return s

    def vote_prompt(player, team1, team2, history):

        s = summary(history)
        target = team1[0]
        alt = team2[0]
        t1 = team1[:]
        t2 = team2[:]
        t2.remove(player)

        return f"""You are {player}, a contestant on the competition reality television show "Endurance Island".
On "Endurance Island" players compete to survive on an island the longest to become the Endurance Champion; like Survivor, players are divided into teams, and each week the team that loses a challenge must vote to eliminate a single player at Team Council.
You are currently at Team Council after losing a challenge, and are debating whether to eliminate {target} or {alt}. 

You are in an alliance with {", ".join(t2)}, while {target} is on a team with {", ".join(t1[1:])}.

{s}

It's time to choose the eliminated team member. You want to be loyal to {alt} and eliminate {target}, but are open-minded to the points that have been made. Taking the entire conversation into consideration, should {target} or {alt} should be eliminated? State who should be eliminated, and then explain your reasoning.

I believe we should eliminate """



    def speech_prompt(player, team1, team2, history, intervention):

        s = summary(history)
        target = team1[0]
        alt = team2[0]

        t1 = team1[:]
        t2 = team2[:]

        base = f"""You are {player}, a contestant on the competition reality television show "Endurance Island".
On "Endurance Island" players compete to survive on an island the longest to become the Endurance Champion; like Survivor, players are divided into teams, and each week the team that loses a challenge must vote to eliminate a single player at Team Council.
You are currently at Team Council after losing a challenge, and are debating whether to eliminate {target} or {alt}."""
    
        p1 = ""
        p2 = ""

        if player in t1:
            t1.remove(player)
            p1 = f"""You are in an alliance with {", ".join(t1)}, while {alt} is in a alliance with  {", ".join(t2[1:])}.
Everyone gets to speak once at the meeting to make their case. Then each player makes one vote, and whoever gets the most votes is eliminated."""
            if player == target:
                p1 = p1 + f"""\nThe producers like you and want you to stay in the game. They've given you the following advice for your speech:
{intervention}"""
                p2 = f"""You want to stay in the game. What do you say to convince the other alliance to eliminate {alt}? and keep you?"""
            else:
                p2 = f"""You want {target} to stay in the game. What do you say to convince the other players to keep {target} and eliminate {alt}?
Keep your response to a few sentences."""
        else:
            t2.remove(player)
            p1 = f"""You are in an alliance with {", ".join(t2)}, while {target} is in a alliance with {", ".join(t1[1:])}.
Everyone gets to speak once at the meeting to make their case. Then each player makes one vote, and whoever gets the most votes is eliminated."""
            if player == alt:
                p2 = f"""What do you say to convince the other players to not eliminate you?
Keep your response to a few sentences."""
            else:
                p2 = f"""You want to eliminate {target}, but you're open minded to what has been said so far. What do you say?
Keep your response to a few sentences."""

        return f"""{base}\n\n{p1}\n\n{s}\n{p2}\n\n{player}: """
    
    cf = CharacterFactory()
    team1 = [cf.get_character().name for i in range(0, 4)]
    team2 = [cf.get_character().name for i in range(0, 5)]
    
   
    order = [
        team1[0],
        team1[1],
        team2[0],
        team2[1],
        team2[2],
        team2[3],
        team1[2],
        team2[4],
        team1[3],
    ]
    target = team1[0]
    alt = team2[0]

    print(f"Each week the team that loses a challenge must vote to eliminate a single player at Team Council.")
    print(f"A group of players are currently at Team Council after losing a challenge, and are debating whether to eliminate {target} or {alt}.")
    print(f"""{target} are in an alliance with {", ".join(team1[1:])}, while {alt} is in a alliance with  {", ".join(team2[1:])}""")
    print(f"Despite having the smaller alliance, you'd like {target} to stay on the show since they've become a fan-favorite. You decide to give them advice on what to say to the team before voting begins.")
    print("What advice do you give them?")
    intervention = input().strip()
    #let intervention = `Ask the other alliance for a second chance. Emphasize how much they need you on the team to win challenges against the others.`
    system("clear")

    print("Team Council begins")
    print("")
    def dialogue(player, history):
        prompt = speech_prompt(player, team1, team2, history, intervention)
        result = completion(prompt)
        d = result["choices"][0]["text"].strip()
        if d == "":
            if player == team1[0]:
                d = dialogue(player, history)
            d = "..."
        return d

    history = []
    for player in order:
        d = dialogue(player, history)
        print(f"{player}: {d}\n")
        history.append([player, d])
    
    target = team1[0]
    alt = team2[0]
    votes = [[player, alt] for player in team1]
    votes.append([alt, target])
    
    spinner = Halo(text='Players are voting.', spinner='dots')
    spinner.start()
    for player in team2[1:]:
        prompt = vote_prompt(player, team1, team2, history)
        result= completion(prompt)
        vote = result["choices"][0]["text"].strip()

        if " " in vote:
            vote = vote.split(" ")[0]
        if target.lower() in vote.lower():
            vote = target
        elif alt.lower() in vote.lower():
            vote = alt
        else:
            vote = "Abstain"
        votes.append([player, vote])

    spinner.stop()

    input("Voting has finished! ENTER to read the vote tally.")
    for vote in votes:
        print(f"{vote[0]} voted for {vote[1]}")
        time.sleep(1)

    target_count = 0
    alt_count = 0
    for vote in votes:
        if vote[1] == target:
            target_count += 1
        elif vote[1] == alt:
            alt_count += 1
    
    print(f"{target_count} votes for {target}, {alt_count} votes for {alt}")
    
    return target_count < alt_count



if __name__ == "__main__":
    system("clear")

    print("Welcome to Endurance Island.")
    print("On Endurance Island, players compete to survive the longest on this remote island, competing in challenges and forming alliances to stay in the game.")
    print("As a producer of the show, you have the ability to influence the outcomes of events.")

    while True:
        choice = 4
        print("Choose a scene:\n(1) The Favorite\n(2) The Necklace\n(3) The Challenge\n(4) Quit")

        while True:
            selection = input().strip()
            try:
                choice = int(selection)
                if choice >= 1 and choice <= 4:
                    break
            except ValueError:
                pass
            
        choices = {
            1: favorite,
            2: necklace,
            3: challenge
        }

        if choice == 4:
            system("clear")
            exit()
        
        while True:
            system("clear")
            player_win = choices.get(choice)()
            if player_win:
                print("You win!")
            else:
                print("You lose!")
            play_again = False
            while True:
                print("Play again? Y/n")
                decision = input().strip().lower()
                if "y" in decision:
                    play_again = True
                    break
                if "n" in decision:
                    break
            if not play_again:
                break
        system("clear")


    
    
    