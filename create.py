import os
import shutil

# 新しいフォルダの作成
new_folder = r"../AHC999"
os.makedirs(new_folder, exist_ok=True)  # 既にフォルダがある場合はエラーを出さずに続行

# コピーするファイルのパス（元ファイル）
source_files = ["combiner.py", "header.hpp", "run.sh", "main.cpp", "log.md", ".gitignore"]

# 指定したフォルダへファイルをコピー
for file in source_files:
    shutil.copy(file, new_folder)  # ファイルをコピー

print("complete")