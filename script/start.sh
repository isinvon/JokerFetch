#!/bin/bash

# 进入 jokerfetch 项目的根目录
cd "$(dirname "$0")/.."

# 使用全局环境中的 python 来运行 main.py
python main.py

# 保持命令行窗口开启，方便查看任何输出
read -p "Press any key to continue..."
