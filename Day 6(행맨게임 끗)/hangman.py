# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
# """"""는 여러 줄 문자열을 만드는 방법임
# """"""로 묶인 하나의 그림이 인덱스 1개로 읽힘
hangman_pics = [
    # 인덱스 0번
    """------
     |    |
     |
     |
     |
     |
    ---""",
    # 인덱스 1번 
     """ ------
     |    |
     |    O
     |
     |
     |
    ---""",
    # 인덱스 2번
     """------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    # 인덱스 3번
     """------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    # 인덱스 4번 
     """------
     |    |
     |    O
     |   /|\
     |
     |
    --- """,
    # 인덱스 5번
     """------
     |    |
     |    O
     |   /|\
     |   /
     |
    ---""",
    # 인덱스 6번
    """------
     |    |
     |    O
     |   /|\
     |   / \
     |
    --- """ 
    ]


class HangmanGame:
    def __init__(self, words):
        # 랜덤하게 선택될 단어.
        self.word = random.choice(words).lower() 
        # 시도 수 6번 
        # 추측한 알파벳을 담을 빈 집합
        # 리스트로도 가능하지만 중복 체크를 위해 함수 사용. 
        self.guessed_letters = set() 
        self.lives_left = 6 
        
        
    def make_guess(self, guess):
        
        # 원래는 이미 추측했는지를 두 번째로 뒀었는데 그렇게 하면 이미 추측한 글자를 "맞췄다"라고 먼저 할 수 있음
        # 추측했는지 먼저 검사하고, 그게 아니라면 단어랑 비교하고, 맞고/틀림을 확인해야 함. 
        if guess in self.guessed_letters: 
            print("이미 추측한 글자입니다.")

        elif guess in self.word: 
            # append는 리스트에서 add는 함수에서 씀 
            # append는 중복을 허용하고, add는 중복을 불허함
            # append는 순서를 유지하고, add는 순서가 없음 
            # 행맨 게임에서 add를 이용하는 이유는 집합으로 중복 추축을 방지하기 위함
            self.guessed_letters.add(guess)
            print("글자를 맞추셨군요. 더 힘내봐요") 
                                
        else:
            #틀렸어도 추측한 레터로 추가해야 나중에 또 틀리면 또 틀렸다고 알려줌. 
            self.guessed_letters.add(guess) 
            self.lives_left -= 1
            print(f"(틀렸습니다. 남은 시도 횟수 {self.lives_left})")

    def display(self):
        #resutl는 빈 문자열로 시작함
        result = ""
        # for char in self.word는 self.word에 있는 문자를 하나씩 가져옴. 
        # 각 character를 순회하라는 뜻 
        # 각 character를 순회해서 self.guessed_letters가 self.word에 있으면 
        # result char를 추가하고 할당하라는 뜻. 
        # 만약에 없으면 result에 "-"를 추가하고 할당하라는 뜻 
        for char in self.word:
            if char in self.guessed_letters:
                result += char
            else: 
                result += "_"
        return result
    
    # """"""로 묶여 있는 하나가 인덱스 하나니까... 각각 인덱스를 목숨이 사라지면서 보여주라는 뜻. 
    def display_hangman(self):
        index = 6 - self.lives_left
        return hangman_pics[index]     
    
    # play 메서드. 
    # 먼저 행맨 게임을 시작한다는 메시지를 보여주고 
    # 단어 몇개 맞췄는지 self.display 메서드 보여줌 
    # 그리고 self.display_hangman 도 보여줌. 

    def play(self):
        print("행맨 게임을 시작합니다")
        print(f"단어: {self.display()}")
        print(self.display_hangman())

    # while self.lives_left가 0보다 큰데 self.guessed_letters에 있는 character가 self.word character에 모두 있으면 
    # 축하한다고 말해주고 게임 종료 

        while self.lives_left > 0:
            if all(char in self.guessed_letters for char in self.word):
                print(f"축하합니다. 단어를 맞추셨습니다:{self.word}")
                return
    
    # 그게 아니면 계속 글자를 입력하라고 보여주면 됨 (대소문자 오류방지 추가)
    # 그리고 make_guess 메서드 계속 돌아감... input과 함께 
            guess = input("글자를 입력하세요: ").lower().strip()
            if not guess: 
                print("글자를 입력하세요!")
                continue

            self.make_guess(guess)

    # 그리고 계속 단어 상황판과 행맨 그림 계속 보여주고 
    # 추측한 글자는 콤마로 분류하고 알파벳 순으로 정렬해서 추측한 글자라고 계속 보여 줌. 
            print(f"단어:{self.display()}")
            print(self.display_hangman())
            print(f"추측한 글자:{','.join(sorted(self.guessed_letters))}")
            print("_" * 30)

        print(f"게임오버. 정답은 {self.word}였습니다.")


if __name__ == "__main__":
    game = HangmanGame(words)
    game.play()