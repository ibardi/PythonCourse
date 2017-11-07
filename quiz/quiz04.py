ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return '{} has the following states: {}.'.format(self.name,self.winning_states)


    def win_state(self, state):
        """Adds a state to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes = self.votes + ELECTORS.get(state)
        #KNOWN MISTAKE. I NEED TO REFERENCE THE VALUE ASSOCIATED WITH THE KEY. 

    def __gt__(self,another):
        if self.votes > another.votes:
            return True
        return False

def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'],votes=55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()