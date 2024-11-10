
# ANSI 转义序列的基本16色
COLORS = [
    "\033[0;30m██",  # Black
    "\033[0;31m██",  # Red
    "\033[0;32m██",  # Green
    "\033[0;33m██",  # Yellow
    "\033[0;34m██",  # Blue
    "\033[0;35m██",  # Magenta
    "\033[0;36m██",  # Cyan
    "\033[0;37m██",  # White
    "\033[1;30m██",  # Bright Black (Gray)
    "\033[1;31m██",  # Bright Red
    "\033[1;32m██",  # Bright Green
    "\033[1;33m██",  # Bright Yellow
    "\033[1;34m██",  # Bright Blue
    "\033[1;35m██",  # Bright Magenta
    "\033[1;36m██",  # Bright Cyan
    "\033[1;37m██"   # Bright White
]
RESET = "\033[0m"  # 重置颜色

def get_color_blocks():
    """ 
    获取系统色彩块
    <br/>
    输出样式(16个小色块)：
    <p>██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██</p>
    """
    # 将每种颜色块组合成一行
    color_line = ''.join(COLORS) + RESET # 可自主设置间隔符号
    return color_line
""" 
# 测试输出
if __name__ == '__main__':
    print("系统色彩块:")
    print(get_color_blocks())
 """