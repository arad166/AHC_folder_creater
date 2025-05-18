#!/bin/bash

# エラー時にスクリプトを終了
set -e

# 実行コマンド
python3 combiner.py src/main.cpp src/combined.cpp

# ファイルの内容をクリップボードにコピー
cat src/combined.cpp | xclip -selection clipboard