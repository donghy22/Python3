class pokemon :
    def __init__(self, name, hp, power, skill):
        self.name = name
        self.hp = hp
        self.power = power
        self.skill = skill
    def info(self):
        print(f'포켓몬:{self.name}')
        print(f'체력:{self.hp}')
        print(f'공격력:{self.power}')
        print(f'기술:{self.skill}')
    def attack(self,skill_number):
        print(self.skill[skill_number])

pokemon1 = pokemon("피카츄", 35, 55, ['100만 볼트','전광석화','번개'])
pokemon2 = pokemon('파이리', 39, 52, ['불꽃세례','화양방사','회오리불꽃'])
pokemon3 = pokemon('꼬부기', 44, 48, ['거품','물대포','하이드로펌프'])

pokemon1.info()
pokemon2.info()
pokemon3.info()

pokemon1.attack(0)
pokemon2.attack(1)
pokemon3.attack(2)

#과제
#나만의 클래스 만들기, 단, input을 활용하여 인스턴스를 생성하는 함수를 만들어보세요!