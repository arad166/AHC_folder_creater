import os
import shutil

# 新しいフォルダの作成
new_folder = r"../AHC999"
os.makedirs(new_folder, exist_ok=True)  # 既にフォルダがある場合はエラーを出さずに続行

# コピーするファイルのパス（元ファイル）
source_files = ["combiner.py", "header.hpp", "run.sh", "main.cpp", "log.md"]

# 指定したフォルダへファイルをコピー
for file in source_files:
    shutil.copy(file, new_folder)  # ファイルをコピー

# 新しい.gitignoreファイルのパス
gitignore_path = os.path.join(new_folder,".gitignore")

# 追加するファイルやディレクトリのリスト
ignore_items = [
    'log.md',
    'tools',
    'run.sh',
    'out.txt',
    'combiner.py',
    'main'
]

# .gitignoreファイルに書き込む
with open(gitignore_path, 'w') as f:
    for item in ignore_items:
        f.write(f"{item}\n")

print("complete")