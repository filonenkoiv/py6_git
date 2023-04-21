import random
class WTK():
    def __init__(self):
        self.choices = ['чарівник', 'рицарь', 'злодій']
        self.playerName = None
        self.playerChoice = None
        self.enemyChoice = None
        self.playerHealth = 100
        self.enemyHealth = 100
        self.playerScore = 0
        self.enemyLevel = 0
        self.round = 1

    def print_scores(self):
        print('-' * 40)
        print("Гравець:", self.playerName)
        print("Набрані очки:", self.playerScore)
        print("Здоров'я гравця:", self.playerHealth)
        print("Здоров'я опонента:", self.enemyHealth)
        print("Рівень опонента:", self.enemyLevel)
        with open("scores.txt", "a") as f:
            f.write(f"{self.playerName}: {self.playerScore}\n")

    def get_player_name(self):
        print('-' * 40)
        self.playerName = input("Введіть ваше ім'я: ")

    def logical(self):
        while True:
            self.player_attack()
            self.enemy_defense()
            if self.playerChoice == self.enemyChoice:
                print('-' * 40)
                self.round += 1
                return 'Нічия!'
            if (self.playerChoice == 'чарівник' and self.enemyChoice == 'рицарь') or \
               (self.playerChoice == 'злодій' and self.enemyChoice == 'чарівник') or \
               (self.playerChoice == 'рицарь' and self.enemyChoice == 'злодій'):
                self.playerScore += 1
                self.enemyHealth -= 20
                print('-' * 40)
                self.round += 1
                return 'Ви перемогли!'
            else:
                self.playerHealth -= 20
                print('-' * 40)
                self.print_scores()
                self.round += 1
                print('-' * 40)
                return 'Ви програли!'

    def player_attack(self):
        while True:
            print(f'Раунд {self.round}. Атака гравця.')
            self.playerChoice = input('Оберіть чарівника, рицаря або злодія: ').lower()
            if self.playerChoice in self.choices:
                break
            else:
                print('-' * 40)
                print('Ви обрали невірне значення! Спробуйте ще раз!')

    def player_defense(self):
        while True:
            print(f'Раунд {self.round}. Захист гравця.')
            self.playerChoice = input('Оберіть чарівника, рицаря або злодія: ').lower()
            if self.playerone in self.choices:
                break
            else:
                print('-' * 40)
                print('Ви обрали невірне значення! Спробуйте ще раз!')

    def enemy_attack(self):
        print(f'Раунд {self.round}. Атака опонента.')
        self.enemyChoice = random.choice(self.choices)

    def enemy_defense(self):
        print(f'Раунд {self.round}. Захист опонента.')
        self.enemyChoice = random.choice(self.choices)

    def rungame(self):
        while True:
            print('-' * 40)
            print('Гра «Чарівники, Злодії та Рицарі» (WTK)')
            print('-' * 40)
            choice = input("1 - Ввести ім'я.\n2 - Грати.\n3 - Подивитись результати.\n4 - Вихід з гри.\nВаш вибір: ")
            if choice == '1':
                print('-' * 40)
                print("Для початку гри, потрібно ваше ім'я!")
                self.get_player_name()
            elif choice == '2':
                print('-' * 40)
                print(self.logical())
                print(f"Опонент обрав: {self.enemyChoice}")
                if self.playerHealth == 0 and self.enemyHealth > 0:
                    print('-' * 40)
                    print('\t\t\t\tGAMEOVER')
                    print('-' * 40)
                    break
                elif self.enemyHealth == 0 and self.playerHealth > 0:
                    print('-' * 40)
                    print('ENEMY DOWN')
                    self.enemyLevel += 1
                    self.enemyHealth = 100
            elif choice == '3':
                self.print_scores()
            elif choice == '4':
                print('-' * 40)
                print('\t\t\t\tGameOver')
                print('-' * 40)
                break
            else:
                print('-' * 40)
                print('Ви обрали невірне значення! Спробуйте ще раз!')
game = WTK()
game.rungame()