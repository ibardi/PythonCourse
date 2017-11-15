import string
import copy

### DO NOT MODIFY THIS FUNCTION ###
def load_wordlist(file_name):
    '''
    '''
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_a_valid_word(word_list, word):
    '''    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_joke_string():
    """
    Returns: an article in encrypted text.
    """
    f = open("joke.txt", "r", encoding = 'utf-8') #can't read the apostrophe without this
    joke = str(f.read())
    f.close()
    return joke

WORDLIST_FILENAME = 'words.txt'


class Text(object):

    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Text object
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_text(self):
        '''
        Returns: self.text
        '''
        return self.text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]


    ### YOU NEED TO MODIFY THIS METHOD ###
    def create_moved_dict(self, shift):
        '''
        Creates a dictionary that maps every letter to a
        character moved down the alphabet by the input move. 

        move: an integer, 0 <= move < 26

        Returns: a dictionary

        Example: an_instance_of_Text.create_moved_dict(2) would generate
        {'a': 'c', 'b': 'd', 'c':'e', ...}  
        '''
        lowercase_letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        inverselowercase_letters = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        uppercase_letters = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        inverseuppercase_letters = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

        def mover(dictionary,shift):
            dict = {}
            for element in dictionary:
                if dictionary[element] <= 26 - shift:
                    dict[element] = (dictionary[element] + shift)
                else:
                    dict[element] = (dictionary[element] + shift - 26)
            return dict
        
        def switcher(dictionary):
            dictionarymap = {}
            for element in dictionary:
                dictionarymap[dictionary[element]] = element
            return dictionarymap

        def backtoletters(dictionary,mapping):
            dict = {}
            for key in dictionary:
                dict[mapping[key]] = dictionary[key]
            return dict

        def combiner(dictionary,shift,reference):
            local_dict = mover(dictionary,shift)
            local_dict = switcher(local_dict)
            local_dict = backtoletters(local_dict,reference)
            local_dict = switcher(local_dict)
            return local_dict

        changedlower = combiner(lowercase_letters,shift,inverselowercase_letters)
        changedupper = combiner(uppercase_letters,shift,inverseuppercase_letters)
    


        return {**changedlower,**changedupper}

    ### YOU NEED TO MODIFY THIS METHOD ###
    def apply_move(self, shift):
        '''
        Applies the cipher to self.text with the input move       

        move: an integer, 0 <= move < 26

        Returns: the text (string) in which every character is moved
             down the alphabet by the input move
        '''
        dict = self.create_moved_dict(shift)
        text = self.get_text()
        shiftedtext = ''
        for character in text:
            try:
                shiftedtext = shiftedtext + dict[character]
            except KeyError:
                shiftedtext = shiftedtext + character
        return shiftedtext


class PlainText(Text):

    ### YOU NEED TO MODIFY THIS METHOD ###
    def __init__(self, text, shift):
        '''
        Initializes a PlainText object        

        text: a string
        move: an integer

        A PlainText object inherits from Text and has five attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
            self.move (integer, determined by input move)
            self.encrypting_dict (dictionary, built using move)
            self.encrypted_text (string, created using move)

        Note: you must use the parent class constructor(__init__ function) 
        so less code is repeated
        '''
        Text.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = self.create_moved_dict(shift)
        self.encrypted_text = self.apply_move(shift)


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_move(self):
        '''
        Used to safely access self.move outside of the class

        Returns: self.move
        '''
        return self.shift


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        copy = copy.deepcopy(self.encrypting_dict)
        return copy


    ### YOU NEED TO MODIFY THIS METHOD ###
    def get_encrypted_text(self):
        '''
        Used to safely access self.encrypted_text outside of the class

        Returns: self.encrypted_text
        '''
        return self.encrypted_text

    ### YOU NEED TO MODIFY THIS METHOD ###
    def change_move(self, shift):
        '''
        Changes self.move of the PlainText and updates other 
        attributes determined by move (ie. self.encrypting_dict and 
        encrypted_text).

        move: an integer, 0 <= move < 26

        Returns: nothing
        '''
        text = self.get_encrypted_text(self)
        self.__init__(text,shift)
        return none

class CipherText(Text):

    
    ### YOU NEED TO MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a CipherText object

        text: a string

        a CipherText object has two attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
        '''
        Text.__init__(self,text)


    ### YOU NEED TO MODIFY THIS METHOD ###
    def decrypt_text(self):
        '''
        Decrypt self.text by trying every possible move value
        and find the "best" one. We will define "best" as the move that
        creates the maximum number of real words when we use apply_move(move)
        on the text. If s is the original move value used to encrypt
        the text, then we would expect 26 - s to be the best move value 
        for decrypting it.

        Returns: a tuple of the best move value used to decrypt the text
        and the decrypted  text using that move value. Check out the
        test case in main function below.

        '''
        last_shift = 0
        bestoption = 0
        word_list = load_wordlist('words.txt')
        for shift in range(27):
            decrypt_joke = self.apply_move(shift)
            wordlist = decrypt_joke.split(' ')
            validwords = 0
            for word in wordlist:
                if is_a_valid_word(word_list,word):
                    validwords += 1
            if validwords > bestoption:
                last_shift = shift
                bestoption = validwords
        return (last_shift,self.apply_move(last_shift))


### DO NOT MODIFY THIS FUNCTION ###
def decrypt_joke():
    joke = CipherText(get_joke_string())
    return joke.decrypt_text()


### DO NOT MODIFY THIS FUNCTION ###
def main():
    # Example test case (PlainText)
    plaintext = PlainText('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_encrypted_text())

    # Example test case (CipherText)
    ciphertext = CipherText('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_text())

    print(decrypt_joke())

if __name__ == '__main__':
    main()
