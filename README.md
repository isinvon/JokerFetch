# 生成 requirements.txt 文件

pip freeze > requirements.txt

# 显示库

pip freeze

# 注意

如果想要通过start.bat启动项目，就要在项目内部安装虚拟环境venv，使用全局环境是无法启动的：

- 创建虚拟环境：

  python -m venv venv
- 激活虚拟环境（windows）

  venv\Scripts\activate
- 激活虚拟环境（macos）

  source venv/bin/activate

接着安装依赖：

- pip install xxx xxx
- pip freeze > requirements.txt
- pip freeze (显示需要安装的依赖，就是需要写入到requirements.txt中的内容)
-
