# PIL 需要安装 Pillow
from PIL import Image

class ImageToTxtArtConverterPlus:
    """ 
    - ImageToTxtArtConverterPlus是ImageToTxtArtConverter的升级版
    
    图像转 ASCII 艺术转换器
    - 支持彩色和灰度模式。
    - 支持自定义字符集。
    - 支持自定义缩放。
    - 支持自定义宽度和高度。
    
    注意:
    - 如果colored=True, 则会将图像转换为彩色 ASCII 艺术。
    - 如果colored=False, 则会将图像转换为灰度 ASCII 艺术。(使用灰色请自行更改所用的拼接字符集，改成其他的字符集，不然会是一片灰色)
    - 如果width和height都为None, 则会按scale缩放图像。

    用法示例：
    converter = ImageToTxtArtConverter(scale=0.1, colored=True, width=50, height=20)
    converter.get_image_ascii("your_image.jpg")

    使用的字符集（字符集数量越少越清晰，越密集颜色越浓）：
    1. 密集字符集：["█"]
    2. 密集字符集：["█", "▓", "▒", "░", " "]
    3. 密集字符集：["█", "▓", "░"]
    4. 密集字符集：["█", "░"]
    5. 密集字符集：["█", "▒", "░"]
    """
    
    def __init__(self, scale=0.1,colored=False, width=None, height=None):
        self.scale = scale
        self.colored = colored
        self.width = width
        self.height = height

    def rgb_to_ansi(self, r, g, b):
        """将 RGB 转换为 ANSI 颜色编码"""
        return f"\033[38;2;{r};{g};{b}m"

    def image_to_ascii(self, image):
        """
        将图像转换为 ASCII 艺术

        - 特殊字符参考: https://cn.symbolslist.com/

        """
        # 使用更密集的字符集，调整字符集的选择以控制显示效果
        # 1
        # ascii_chars = ["█"]
        # ascii_chars = ["c", " "]
        # 2
        # ascii_chars = ["▓"] 
        # 3
        # ascii_chars = ["░"]
        # ascii_chars = ["▓","▒","█","▊","▌",' ']
        ascii_chars = ["█","▓"," "]
        # ascii_chars = ["▍" ," "]
        # 4
        # ascii_chars = ["▒"]
        # 4
        # ascii_chars = ["█", "▓", "▒", "░", " "]
        # 5
        # ascii_chars = ["█", "▓", "░"]
        # 6
        # ascii_chars = ["█", "░"]
        # 7
        # ascii_chars = ["█", "▒", "░"]
        # 8
        # ascii_chars = ["█", "▒", "░", "▒", "░"]
        
        width, height = image.size
        ascii_art = ""
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                if self.colored and isinstance(pixel, tuple):  # 彩色处理
                    r, g, b = pixel[:3]
                    gray = int(sum(pixel[:3]) / 3)  # 获取灰度值
                    char_index = int(gray / 255 * (len(ascii_chars) - 1))  # 映射到字符集
                    ascii_art += self.rgb_to_ansi(r, g, b) + ascii_chars[char_index]
                else:  # 灰度处理
                    gray = int(sum(pixel[:3]) / 3)  # 获取灰度值
                    char_index = int(gray / 255 * (len(ascii_chars) - 1))  # 映射到字符集
                    ascii_art += ascii_chars[char_index]  # 使用密集字符映射灰度
            ascii_art += "\033[0m\n"  # 重置颜色
        return ascii_art

    def get_image_ascii(self, image_path):
        """显示图像的 ASCII 艺术表示"""
        image = Image.open(image_path)
        
        # 根据 width 和 height 调整图像尺寸，如果未提供则按 scale 缩放
        if self.width and self.height:
            image = image.resize((self.width, self.height))
        else:
            image = image.resize(
                (int(image.width * self.scale), int(image.height * self.scale))
            )
        
        image = image.convert("RGB")  # 转换为 RGB 模式
        ascii_art = self.image_to_ascii(image)        
        return ascii_art

# 使用示例
# converter = ImageToTxtArtConverterPlus(scale=0.1, colored=True, width=50, height=18)

# print(converter.get_image_ascii("../resources/clown.jpg"))
