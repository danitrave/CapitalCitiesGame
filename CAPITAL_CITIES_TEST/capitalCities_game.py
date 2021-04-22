import random
from elenco_stati_capitali import state_capital,states
stati = states()
stato_capitale = state_capital()
players = 0
statesQuiz = []
wrongCapitals = []
totalScores = []
finalScores = []
capitals = {}
correct = {}

class Rules:
    def listRules():
        print("LET'S START TO PLAY!")
        print('RULES:')
        print('The aim of the game is to guess the highest number of capital cities of the states in the world')
        print('Each player will start with 100 initial points.')
        print('The game will provide 4 possibilities to the player that will choose one!')
        print('Each time a player provides the wrong answer, will lose 10 points from the initial points')
        print('The player with the highest score, wins!')
        return ''


class Players:
    def number():
        global players
        number = int(input('insert the number of players: '))
        players = number

        return ''

               
class CurrentCapital:
    def capital():
        
        global statesQuiz

        volatileTest = []
        
        while len(volatileTest) < 10:   
            
            stato = stati[random.randint(0,len(stati)-1)]
                        
            if stato not in volatileTest:
                
                volatileTest += [stato,]
                statesQuiz = volatileTest
                
        volatileTest = []
        return statesQuiz

        
class CapitalOptions:
    def options():
        
        quizOptions = []        
        volatileQuiz = []
        
        for y in statesQuiz:
            
            possibilities = tuple()
            risposta = stato_capitale[y]
            possibilities += (risposta,)

            while len(possibilities) < 4:

                optionCapital = stato_capitale[stati[random.randint(0,len(stati)-1)]]  
                
                if optionCapital not in possibilities:
                    possibilities += (optionCapital,)
                         
            possibilities = list(possibilities)
            possibilities.sort()
            volatileQuiz += (possibilities,)
            quizOptions += volatileQuiz
            volatileQuiz = []
            possibilities = ()

        return quizOptions 



class Test(CurrentCapital,CapitalOptions):
    def test():
        
        global wrongCapitals
        global players
        global totalScores
        
        for x in range(players):

            volatileWrongCapital = []

            score = 0

            print("It's time for player number: ",x+1)
            
            questions = CurrentCapital.capital()
            options = CapitalOptions.options()

            for y in range(len(questions)):
                
                question = questions[y]
                print("What is the capital city of",question,"?")
                current = options[y]
                              
                collectChioces = []
                for i in range(len(current)):
                    
                    correct = stato_capitale[question]
                    choices = {}
                    choices[i+1] = current[i]
                    collectChioces += [choices,]
                    
                    print(choices)

                for e in collectChioces:
                    
                    for h in e:
                        
                        reverse = {}
                        reverse[e[h]] = h

                        if correct in reverse:
                            correctAnswer = reverse[correct]
                                    
                answer = int(input("Answer: "))
                
                if answer == correctAnswer:
                    pass
                else:
                    score += 1
                    volatileWrongCapital += [question,]

            wrongCapitals += [volatileWrongCapital,]
            
            totalScores += [score,]

        return ''
        
            

class Scores:
    def scorePerPlayer():

        global totalScores
        global finalScores

        for i in range(len(totalScores)):
            
            initalScore = 100
            finalVolatileScore = 100 - (totalScores[i] * 10)
            finalScores += [finalVolatileScore,]

            initialScore = 100

        winnerScore = max(finalScores)

        winners = []

        for s in range(len(finalScores)):

            if finalScores[s] == winnerScore:
                winners += [s+1,]
            else:
                pass 

        print("The scores of the competitors are: "+" ".join([str(o) for o in finalScores]))
        print("Therefore the winner is/are player/s number"," ".join([str(a) for a in winners]),"with a score of",winnerScore)
        return ''

class WrongCapitals:
    def wrongCapitalsPerPlayer():

        global wrongCapitals

        global capitals

        for p in range(players):
            
             capitals[p+1] = wrongCapitals[p]

        print("Here we present the wrong answers per player:")
        print(capitals)
        return ''


class CorrectionCapitals(WrongCapitals):
    def correction():

        global correct

        for k in range(players):

            capitalToCorrect = capitals[k+1]
            volatileCorrect = []          
            
            for state in capitalToCorrect:

                capital = stato_capitale[state]

                volatileCorrect += [capital,]

            correct[k+1] = volatileCorrect

        print("Here we present the correction to the wrong answers per player:")
        print(correct)
        return ''
        
    
class Table:
    def tabulateCreator():  

        capitalsTable = []
        correctionsTable = []
        playersTable = []
        
        for p in range(players):
            player = "Player N°"+ str(p+1)
            playersTable += [player,]

        for i in capitals:
            capitalsTable += [capitals[i],]

        for e in correct:
            correctionsTable += [correct[e],]

        for ok in range(len(playersTable)):
            print(playersTable[ok])
            print("")
            res1 = "  "
            res2 = "  "
            print("WRONG ANSWERS")
            print(capitalsTable[ok])
            print("CORRECTIONS")
            print(correctionsTable[ok])
            print("")

        return ''

print(Rules.listRules())
print(Players.number())
print(Test.test())
print(Scores.scorePerPlayer())
print(WrongCapitals.wrongCapitalsPerPlayer())
print(CorrectionCapitals.correction())
print(Table.tabulateCreator())

                

                    
                
            
        
        
        


