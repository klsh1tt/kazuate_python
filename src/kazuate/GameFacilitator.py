import random

'''
ゲーム進行役 クラス
'''
class GameFacilitator :
    # 当てる数
    answer = ''

    # 当てる数の桁数(int)
    answerLength = -1

    # プレイヤーの入力値
    value = 0

    # 入力回数カウンタ
    inputCounter = 0

    # 入力値チェックOK時の目印
    VAL_CHECK_OK = 'OK'

    # 選択された難易度
    level = -1

    # 難易度を表す定数
    LEVEL_EASY = 1
    LEVEL_NORMAL = 2
    LEVEL_HARD = 3

    # 難易度に対応する出題桁数を表す定数
    AS_LENGTH_EASY = 2
    AS_LENGTH_NORMAL = 3
    AS_LENGTH_HARD = 4


    '''
    インスタンス生成時に、当てる数を決定しanswerフィールドに格納します。
    '''
    def __init__(self):
        self.setupAnswerLength()  # answerLengthを決定します

#        print('テスト answerLength:{}'.format((self.answerLength)))
        while len(self.answer) < self.answerLength :
            self.answer += str(random.randint(1, 9))


    '''
     キーボードから回答を受け付け、valueフィールドへ格納します。
    '''
    def hearValue(self):
        print('【テスト】 answer: ' + self.answer)
        print('----------------------------------------------------')
        self.value = input('{}桁の数字を入力してください。'.format(self.answerLength))
        print('【テスト】 value:{}'.format(self.value))


    '''
    キーボードから難易度の選択を受け付け、levelフィールドへ格納します。
    '''
    def hearLevel(self):
        self.level = int(input('難易度を選択してください。（1:EASY  2:NORMAL  3:HARD）'))


    '''
    入力値のチェックを行います。
    エラーの場合はエラーメッセージを戻り値として返します。正常の場合は'OK'を返します。
    '''
    def checkValue(self):
        if len(self.value) != self.answerLength :
            return '【エラー】入力値が{}桁ではありません。'.format(self.answerLength)
        elif '0' in self.value:
            return '【エラー】入力値に「0」が含まれています'

        # 入力値が問題ない場合は、入力回数を+1する。
        self.inputCounter += 1
        return GameFacilitator.VAL_CHECK_OK


    '''
    難易度の入力値のチェックを行います。
    エラーの場合はエラーメッセージを戻り値として返します。正常の場合は'OK'を返します。
    '''
    def checkLevelValue(self):
        if(self.LEVEL_EASY != self.level
            and self.LEVEL_NORMAL != self.level
            and self.LEVEL_HARD != self.level) :

            return '【エラー】入力値は1,2,3のいずれかとして下さい。'

        return GameFacilitator.VAL_CHECK_OK


    '''
    難易度に応じて、出題桁数を設定します。
    難易度はキーボードから入力を受け付けます。
    '''
    def setupAnswerLength(self):
        result = ''  # 入力値チェック結果

        # キーボードから正しい難易度入力が得られるまで、キーボード入力とチェック処理をやり直す。
        while not GameFacilitator.VAL_CHECK_OK == result:
            self.hearLevel()
            result = self.checkLevelValue()

            # 入力値のチェック結果がエラーの場合は、エラーメッセージを出力する。
            if not GameFacilitator.VAL_CHECK_OK == result:
                print(result)

        # 難易度の入力値を元に、answerLengthの桁数を判定し設定します。
        if self.level == GameFacilitator.LEVEL_EASY:
            self.answerLength = GameFacilitator.AS_LENGTH_EASY
        if self.level == GameFacilitator.LEVEL_NORMAL:
            self.answerLength = GameFacilitator.AS_LENGTH_NORMAL
        if self.level == GameFacilitator.LEVEL_HARD:
            self.answerLength = GameFacilitator.AS_LENGTH_HARD


    '''
    入力値が当てる数と合っているかをチェックします。
    このメソッドではフィールド変数valueに不正な値が入っていないことを前提としています。
      （checkValueメソッドを事前に呼んでいることを想定）

    このメソッドは戻り値として以下を返します。
    True        ：正解の場合
    False    ：不正解の場合
    '''
    def judgeAnswer(self):
        hitCount = 0  # 「部分正解」の数

        # 1桁ずつ、「部分正解」の判定を行う。
        print('【テスト】 answer:{}'.format(self.answer))
        i = 0
        for i in range(self.answerLength) :
            ansChar = (self.answer)[i]
            valChar = (self.value)[i]

            if ansChar == valChar:
                hitCount += 1

            i += 1
        print('【テスト】 hitCount:{}'.format(hitCount))

        # 結果を画面に出力する。
        if hitCount == self.answerLength :
            print('正解です！')
            print('正解までの回答数は{}回でした。'.format(self.inputCounter))

            return True
        else:
            print('不正解です。')
            print('部分正解：{}'.format(hitCount))

            return False
