#!/bin/sh

SRC_DIR="/home/arad166/cp/heur/ahcxxx/src"
BASE_DIR="/home/arad166/cp/heur/ahcxxx"
IN_DIR="$BASE_DIR/tools/in"
LOG_DIR="$BASE_DIR/logs"

mkdir -p "$LOG_DIR"

# 現在のGitブランチ名を取得（無効な文字は置換）
branch=$(git -C "$BASE_DIR" rev-parse --abbrev-ref HEAD 2>/dev/null | tr '/' '_' | tr -d '\n')

# タイムスタンプを追加
timestamp=$(date "+%Y%m%d_%H%M%S")

# ログファイル名にブランチ名とタイムスタンプを使う
err_log="$LOG_DIR/${branch}_$timestamp.log"

# コンパイル
cd "$SRC_DIR" || exit 1
g++ -O3 -std=c++23 -Wall -I ac-library main.cpp -o main 2>> "$err_log"
if [ $? -ne 0 ]; then
    echo "コンパイルに失敗しました。" >> "$err_log"
    exit 1
fi

cd "$BASE_DIR" || exit 1

# 各入力ファイルに対して実行
for in_file in "$IN_DIR"/*.txt; do
    filename=$(basename "$in_file" .txt)
    echo "Running $filename..." >> "$err_log"
    "$SRC_DIR"/main < "$in_file" > /dev/null 2>> "$err_log"
done
