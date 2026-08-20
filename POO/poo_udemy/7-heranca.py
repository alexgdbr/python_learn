# Classe Pai (Super classe) - Generalista
class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
    
# CLasse derivada (Subclasse) - Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0, storyline=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyline = storyline
        
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

mult_game = Game("Fortnite", 2017, True, 8.0)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Last of Us 2", 2020, 9.5, "Emocionante história de sobrevivência e vingança")
sing_game.technical_sheet()