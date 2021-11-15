from kazuate.GameFacilitator import GameFacilitator

#ゲーム進行役インスタンスを生成
gf = GameFacilitator()

#ゲームクリア（正解する）まで、キーボード入力～正解判定までの一連の処理をループ
while True:
    result = '' #入力値チェック結果を格納する変数

    #キーボードから正しい入力値が得られるまで、キーボード入力とチェック処理をやり直す。
    while not GameFacilitator.VAL_CHECK_OK == result:
        gf.hearValue()                # キーボード入力受付
        result = gf.checkValue()     # 入力値チェック処理

        # 入力値のチェック結果がエラーの場合は、エラーメッセージを出力する。
        if not GameFacilitator.VAL_CHECK_OK == result:
            print(result)
    if gf.judgeAnswer(): #正解時、Trueが返ってきてwhileループを抜ける（ゲーム終了）
        break