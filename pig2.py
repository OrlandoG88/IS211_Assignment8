import random
import time




def roll_die(sides=6):
    random.seed(0)
    """ function to simulate roll of a die"""
    return random.randint(1, sides)

class player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name} total is {self.total}"

    #def Type_(self):
        #return "Human"

    def play_turn(self):
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h':
            die = roll_die()
            if die == 1:
                print(f"{self.name} rolled a {die}, no points added this turn")
                break
            turn_total += die
            print(
                f"{self.name} rolled a {die}"
                f"{self.name}  possible total is {turn_total}"

            )
            roll_hold = input('roll or hold?').lower()
            if roll_hold == 'h':
                self.total += turn_total
            print (f"{self.name} total: {self.total}")


class ComputerPlayer(player):
    def __init__(self,name):
        self.name = name
        self.total = 0
        self.turn_total = 0




    def play_turn(self):
        print("computers turn")
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h':
            die = roll_die()
            if die == 1:
                print(f"{self.name} rolled a {die}, no points added this turn")
                break
            turn_total += die


            if 25 <= turn_total <= 100 - self.turn_total:
                roll_hold = 'h'
                self.total += turn_total
                print(f"{self.name} total: {self.total}")
            else:
                roll_hold = 'r'



    def Type_(self):
        return "computer"




class player_factory:

    def __init__(self):
        pass


    def instantiate(self, name, type):
        #Player_Type = input("Is player Human or Computer?").lower()
        if type == 'computer':
            return ComputerPlayer("computer")
        elif type == 'human':
            return player('human')





class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None







    def check_winner(self):
        '''return true if there is winner'''
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True



    def play_game(self):
        current_player = self.players[0]
        #start game counter
        #game_start = time.time()



        while not self.check_winner():
            current_player.play_turn()
            #current_player.computer_turn()
            if current_player == self.players[0]:
                current_player = self.players[1]
            elif current_player == self.players[1]:
                current_player = self.players[0]

        # check for time
        # if time >= 1minute, then break the game


        print(f"The winner is {self.winner}, thanks for playing goodbye")


class TimedGameProxy(Game):

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.start_time = time.time()


    #def play_game(self):


    def game_timer(self):
        if time.time() - self.start_time >= 60:
            if players[0].total > players[1].total:
                print("Time is up. Player 1 wins.")
            else:
                print("Time is up. Player 2 wins.")
        else:
            time_elapsed = time.time() - self.start_time
            time_remaining = 60 - time_elapsed
            print(f"There are still {time_remaining} seconds remaining. Continue playing!")


if __name__ == "__main__":

    PF = player_factory()
    p1_type = input("human or computer?")
    p2_type = input("human or computer?")

    p1 = PF.instantiate('p1', p1_type)
    p2 = PF.instantiate('p2', p2_type)

    print(type(p1))
    print(type(p2))
    pig_game = Game(p1, p2)
    pig_game.play_game()