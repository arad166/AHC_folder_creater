#!/bin/sh

# 引数が渡されていない場合はデフォルトで "0000" を使用
input_file="${1:-0000}"

cd "/home/arad166/cp/heur/ahcxxx/src" || exit 1
g++ -O0 -std=c++17 -Wall -D_GLIBCXX_DEBUG -I ac-library main.cpp -o main
cd "/home/arad166/cp/heur/ahcxxx" || exit 1
src/./main < "tools/in/$input_file.txt" > "out.txt"

cd "/home/arad166/cp/heur/ahcxxx/" || exit 1

# ファイルの内容をクリップボードにコピー
cat out.txt | xclip -selection clipboard