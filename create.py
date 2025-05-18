import os
import shutil
import argparse
import sys

# 引数をパースする
parser = argparse.ArgumentParser(description="フォルダ名を指定してファイルをコピー")
parser.add_argument("folder_name", type=str, help="作成する新しいフォルダ名 (例: ahc046)")
args = parser.parse_args()

# 新しいフォルダのパス
new_folder = os.path.join("..", args.folder_name)

# フォルダが既に存在しているかチェック
if os.path.exists(new_folder):
    print(f"エラー: フォルダ '{new_folder}' は既に存在します。")
    sys.exit(1)  # エラー終了

# フォルダ作成
os.makedirs(new_folder)

# コピーするファイルのリスト
source_files = ["combiner.py", "run.sh", "runall.sh","log.md", "combine.sh"]

# 指定したフォルダへファイルをコピー
for file in source_files:
    shutil.copy(file, new_folder)

# srcフォルダの作成とファイルコピー
new_folder_src = os.path.join(new_folder, "src")
os.makedirs(new_folder_src)

source_files_src = ["main.cpp", "header.hpp"]
for file in source_files_src:
    shutil.copy(file, new_folder_src)

# .gitignoreファイルの作成
gitignore_path = os.path.join(new_folder, ".gitignore")

ignore_items = [
    'log.md',
    'tools',
    'run.sh',
    'out.txt',
    'combiner.py',
    'combine.sh',
    'src/main',
    'src/combined.cpp',
    'logs'
]

with open(gitignore_path, 'w') as f:
    for item in ignore_items:
        f.write(f"{item}\n")

print("complete")
