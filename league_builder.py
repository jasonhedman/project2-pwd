import csv

# runs only if executed
if __name__ == "__main__":
    # opens file only for block of code
    with open("soccer_players.csv") as csv_file:
        # read file with csv module
        csv_reader = csv.reader(csv_file, delimiter=",")
        # array of all players from file
        players = [row for row in csv_reader]
        skilled_players = [row for row in players if row[2]=="YES"]
        unskilled_players = [row for row in players if row[2]=="NO"]
        teams = {
            "Sharks":[],
            "Dragons":[],
            "Raptors":[]
        }
        team_keys = list(teams.keys())
        # loops through skilled players and puts them into teams evenly
        for i,player in enumerate(skilled_players):
            teams[team_keys[i%3]].append(player)
        # does the same for unskilled players
        for i,player in enumerate(unskilled_players):
            teams[team_keys[i%3]].append(player)
    # creates output file that prints every team with a list of its players
    output = open('team.txt', 'w')
    letter_template = "Dear {}, \n\nYour child, {}, has been assigned to the {}! \n\nThe team's first practice will be on January 1st at 6:30 pm."
    for key in team_keys:
        output.write(key + "\n");
        for player in teams[key]:
            output.write(player[0] + ", " + player[2] + ", " + player[3] + "\n")
            # creates and writes the letter for each player
            letter = open(player[0].replace(' ', '_')+".txt", "w")
            letter.write(letter_template.format(player[3], player[0], key))
        output.write("\n")
