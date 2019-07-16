import argparse
from tensorflow.python.lib.io import file_io

# Parameters
ARGS = None


def main():

    # ローカル/クラウドの両者に対応。モード(r)が必要
    fp = file_io.FileIO(ARGS.input_file, 'r')
    print(fp.read())
    fp.close()

    # with構文もOK
    with file_io.FileIO(ARGS.input_file, 'r') as fp:
        print('with:', fp.read())

    # Write も同じ
    with file_io.FileIO(ARGS.output_file, 'w') as fp:
        fp.write("Hello World!")

    # ローカルに書き込んだらエラーにならないがファイルをあとで受け取れない
    with file_io.FileIO('./ignored.txt', 'w') as fp:
        fp.write("Hello World!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input_file',
        default='../input.txt',
        help='Test input data'
    )
    parser.add_argument(
        '-o', '--output_file',
        default='../output.txt',
        help='Test output data'
    )

    ARGS, _ = parser.parse_known_args()
    main()