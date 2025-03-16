import os
import shutil

# 新しいフォルダの作成
new_folder = r"../ahc044"
os.makedirs(new_folder, exist_ok=True)  # 既にフォルダがある場合はエラーを出さずに続行

# コピーするファイルのパス（元ファイル）
source_files = ["combiner.py", "run.sh", "log.md"]

# 指定したフォルダへファイルをコピー
for file in source_files:
    shutil.copy(file, new_folder)  # ファイルをコピー
    
new_folder_src = os.path.join(new_folder, "src")

source_files_src = ["main.cpp", "header.hpp"]
os.makedirs(new_folder_src, exist_ok=True)  # 既にフォルダがある場合はエラーを出さずに続行

for file in source_files_src:
    shutil.copy(file, new_folder_src)  # ファイルをコピー

# 新しい.gitignoreファイルのパス
gitignore_path = os.path.join(new_folder,".gitignore")

# 追加するファイルやディレクトリのリスト
ignore_items = [
    'log.md',
    'tools',
    'run.sh',
    'out.txt',
    'combiner.py',
    'src/main',
    'src/combined.cpp'
]

# .gitignoreファイルに書き込む
with open(gitignore_path, 'w') as f:
    for item in ignore_items:
        f.write(f"{item}\n")

print("complete")