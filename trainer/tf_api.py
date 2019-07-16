import argparse

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.contrib import saved_model

# Parameters
ARGS = None
NUM_TRAIN = 8


def main():

    train_x = np.random.rand(NUM_TRAIN, 2)
    train_y = (np.sum(train_x, axis=1) > 1.0) * 1
    train_y = train_y.reshape(NUM_TRAIN, 1)

    # Sequentialモデル使用(Sequentialモデルはレイヤを順に重ねたモデル)
    model = Sequential()

    # 結合層(2層->8層)
    model.add(Dense(NUM_TRAIN, input_dim=2, activation="tanh"))

    # 結合層(4層->1層)：入力次元を省略すると自動的に前の層の出力次元数を引き継ぐ
    model.add(Dense(1, activation="sigmoid"))

    # モデルをコンパイル
    model.compile(loss="binary_crossentropy", optimizer="sgd")

    model.summary()

    # Callbackを定義し、TensorBoard出力の追加
    li_cb = []
    li_cb.append(TensorBoard(log_dir=ARGS.tensor_board))

    # 訓練実行
    model.fit(train_x, train_y, epochs=1, callbacks=li_cb)

    # Saved Model形式でエクスポート
    saved_model.save_keras_model(model, ARGS.saved_model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--tensor_board',
        default='./tb',
        help='Tenosorboard log'
    )
    parser.add_argument(
        '-s', '--saved_model',
        default='./saved_model',
        help='Saved Model directory'
    )

    ARGS, _ = parser.parse_known_args()
    main()