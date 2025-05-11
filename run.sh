#!/bin/sh

# 引数が渡されていない場合はデフォルトで "0000" を使用
input_file="${1:-0000}"

cd "/home/arad166/cp/heur/ahcxxx/src" || exit 1

# DEBUG=1 を指定するとデバッグビルドになる
if [ "$DEBUG" = "1" ]; then
    echo "Building in debug mode...(slow)"
    g++ -O2 -std=c++23 -Wall -D_GLIBCXX_DEBUG -I ac-library main.cpp -o main
else
    echo "Building in release mode...(fast)"
    g++ -O3 -std=c++23 -Wall -I ac-library main.cpp -o main
fi

cd "/home/arad166/cp/heur/ahcxxx" || exit 1

# 実行
src/./main < "tools/in/$input_file.txt" > "out.txt"

# 結果をクリップボードにコピー
cat out.txt | xclip -selection clipboard
