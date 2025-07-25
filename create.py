import os
import shutil
import argparse
import sys
import re

# コピー元ファイル
SOURCE_FILES = ["combiner.py", "run.sh", "runall.sh", "log.md", "combine.sh"]
SOURCE_FILES_SRC = ["main.cpp", "header.hpp"]
GITIGNORE_ITEMS = [
    'log.md',
    'tools',
    'run.sh',
    'runall.sh',
    'out.txt',
    'combiner.py',
    'combine.sh',
    'src/main',
    'src/combined.cpp',
    'logs'
]


def parse_args():
    parser = argparse.ArgumentParser(description="フォルダ名を指定してファイルをコピー")
    parser.add_argument("folder_name", type=str, help="作成する新しいフォルダ名 (例: ahc046)")
    return parser.parse_args()


def create_folder(path):
    if os.path.exists(path):
        print(f"エラー: フォルダ '{path}' は既に存在します。")
        sys.exit(1)
    os.makedirs(path)


def copy_files(files, dest_folder):
    for file in files:
        try:
            shutil.copy(file, dest_folder)
        except Exception as e:
            print(f"ファイル '{file}' のコピーに失敗しました: {e}")
            sys.exit(1)


def create_gitignore(path, items):
    try:
        with open(path, 'w') as f:
            for item in items:
                f.write(f"{item}\n")
    except Exception as e:
        print(f".gitignoreの作成に失敗しました: {e}")
        sys.exit(1)


def main():
    args = parse_args()
    new_folder = os.path.join("..", args.folder_name)
    create_folder(new_folder)
    copy_files(SOURCE_FILES, new_folder)

    # run.shとrunall.shのahcXXX部分を置換
    for script_name in ["run.sh", "runall.sh"]:
        script_path = os.path.join(new_folder, script_name)
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # ahcXXX を引数のフォルダ名で置換
            # ahcの後に数字が続くパターンを置換
            content = re.sub(r"ahcxxx", args.folder_name, content)
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"{script_name}の置換に失敗しました: {e}")
            sys.exit(1)

    new_folder_src = os.path.join(new_folder, "src")
    create_folder(new_folder_src)
    copy_files(SOURCE_FILES_SRC, new_folder_src)

    gitignore_path = os.path.join(new_folder, ".gitignore")
    create_gitignore(gitignore_path, GITIGNORE_ITEMS)

    print("complete")


if __name__ == "__main__":
    main()
