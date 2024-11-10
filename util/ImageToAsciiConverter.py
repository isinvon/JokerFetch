from PIL import Image


class ImageToTxtArtConverter:
    """ 
    图像转ASCII艺术工具类。

    提供了将图像转换为ASCII艺术的功能，支持彩色输出。

    <pre>
    示例：
    1. 初始化转换器：
    converter = ImageToTxtArtConverter()

    2. 指定输入图像路径：
    input_image_path = "path/to/your/image.jpg"

    3. 设置输出尺寸（可选）：
    scale = 1.0  # 缩放比例（默认为1.0，不缩放）
    output_width = 80  # 输出宽度（字符数）
    output_height = 30  # 输出高度（字符数）

    4. 调用转换方法并获取彩色ASCII艺术字符串：
    colored_ascii_art = converter.convert_image_to_high_saturation_ascii(input_image_path, scale=scale, width=output_width, height=output_height)

    5. 调用转换方法并获取无色ASCII艺术字符串：
    grayscale_ascii_art = converter.convert_image_to_grayscale_ascii(input_image_path, scale=scale, width=output_width, height=output_height)

    6. 将生成的ASCII艺术字符串输出到控制台或保存到文件中。
    print("彩色ASCII艺术：\n", colored_ascii_art)
    print("无色ASCII艺术：\n", grayscale_ascii_art)
    </pre>

    <pre>
    注意：
    1. 输入图像路径应指向有效的图像文件。
    2. 输出尺寸参数（width和height）是可选的，如果不指定，将按原始图像比例自动调整输出尺寸。
    3. 转换方法将返回生成的ASCII艺术字符串，可根据需要进行进一步处理或输出。
    </pre>
    """

    def __init__(self):
        # 字符映射表，用于将像素值映射到相应字符
        self.char_mapping = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    def rgb_to_ansi(self, r, g, b):
        """
        将RGB值转换为ANSI转义序列，以在终端中输出彩色字符。

        :param r: 红色通道值，范围为0-255。
        :param g: 绿色通道值，范围为0-255。
        :param b: 蓝色通道值，范围为0-255。
        :return: 对应的ANSI转义序列字符串，用于在终端中显示带颜色的字符。
        """
        return f"\033[38;2;{r};{g};{b}m"

    def adjust_saturation(self, r, g, b, saturation_factor=1.5):
        """
        增加像素的饱和度。

        :param r: 红色通道值，范围为0-255。
        :param g: 绿色通道值，范围为0-255。
        :param b: 蓝色通道值，范围为0-255。
        :param saturation_factor: 饱和度调整因子，默认为1.5。值越大，饱和度越高。
        :return: 调整后新的RGB值。
        """
        import colorsys
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        s = min(1, s * saturation_factor)
        r_adj, g_adj, b_adj = colorsys.hsv_to_rgb(h, s, v)
        return int(r_adj * 255), int(g_adj * 255), int(b_adj * 255)

    def convert_image_to_high_saturation_ascii(self, image_path, scale=1.0, width=None, height=None):
        """
        将指定路径的图像转换为高饱和度彩色ASCII艺术，并返回生成的ASCII字符串。

        :param image_path: 输入图像的路径。
        :param scale: 缩放比例，用于调整输出大小，默认为1.0。值越大，输出图像越大。
        :param width: 期望输出的宽度（字符数）。若为None，则按高度比例调整宽度。
        :param height: 期望输出的高度（字符数）。若为None，则按宽度比例调整高度。
        :return: 包含彩色ASCII艺术的字符串。
        """
        ascii_art = ""  # 初始化用于存储ASCII艺术字符串
        try:
            # 打开图像
            image = Image.open(image_path)
            original_width, original_height = image.size

            # 计算新图像的大小
            if width is None and height is None:
                raise ValueError("至少需要指定width或height中的一个参数来调整输出尺寸。")

            if width is None:
                ratio = height / original_height
                new_width = int(original_width * ratio)
                new_height = height
            elif height is None:
                ratio = width / original_width
                new_width = width
                new_height = int(original_height * ratio)
            else:
                new_width = width
                new_height = height

            # 调整图像大小并转换为RGB模式
            resized_image = image.resize((new_width, new_height))
            resized_image = resized_image.convert("RGB")

            # 遍历每个像素并生成带颜色的ASCII字符
            for y in range(new_height):
                for x in range(new_width):
                    # 获取像素颜色值
                    r, g, b = resized_image.getpixel((x, y))

                    # 调整饱和度
                    r, g, b = self.adjust_saturation(
                        r, g, b, saturation_factor=1.5)

                    # 将灰度值转换为对应的字符
                    grayscale_value = int((0.3 * r + 0.59 * g + 0.11 * b))
                    char_index = int(grayscale_value / 255 *
                                     (len(self.char_mapping) - 1))
                    char = self.char_mapping[char_index]

                    # 累积带颜色的字符到ascii_art字符串
                    ascii_art += f"{self.rgb_to_ansi(r, g, b)}{char}\033[0m"
                ascii_art += "\n"  # 换行

            return ascii_art  # 返回包含彩色ASCII艺术的字符串
        except Exception as e:
            return f"转换图像时出错: {e}"

    def convert_image_to_grayscale_ascii(self, image_path, scale=1.0, width=None, height=None):
        """
        将图像转换为无色的灰度ASCII艺术，并返回生成的ASCII字符串。

        :param image_path: 输入图像的路径。
        :param scale: 缩放比例，用于调整输出大小，默认为1.0。
        :param width: 期望输出的宽度（字符数）。
        :param height: 期望输出的高度（字符数）。
        :return: 包含无色ASCII艺术的字符串。
        """
        ascii_art = ""
        try:
            image = Image.open(image_path)
            original_width, original_height = image.size

            if width is None and height is None:
                raise ValueError("至少需要指定width或height中的一个参数来调整输出尺寸。")

            if width is None:
                ratio = height / original_height
                new_width = int(original_width * ratio)
                new_height = height
            elif height is None:
                ratio = width / original_width
                new_width = width
                new_height = int(original_height * ratio)
            else:
                new_width = width
                new_height = height

            resized_image = image.resize((new_width, new_height))
            resized_image = resized_image.convert("L")

            for y in range(new_height):
                for x in range(new_width):
                    grayscale_value = resized_image.getpixel((x, y))
                    char_index = int(grayscale_value / 255 *
                                     (len(self.char_mapping) - 1))
                    char = self.char_mapping[char_index]
                    ascii_art += char
                ascii_art += "\n"

            return ascii_art
        except Exception as e:
            return f"转换图像时出错: {e}"


""" # 使用示例：
# 创建工具类实例
converter = ImageToTxtArtConverter()

# 指定输入图像路径
input_image_path = "clown.jpg"

# 设置输出尺寸
output_width = 80
output_height = 30

# 调用转换方法并获取彩色ASCII艺术字符串
colored_ascii_art = converter.convert_image_to_high_saturation_ascii(input_image_path, width=output_width, height=output_height)
# 调用转换方法并获取无色ASCII艺术字符串
grayscale_ascii_art = converter.convert_image_to_grayscale_ascii(input_image_path, width=output_width, height=output_height)

# 将生成的ASCII艺术字符串输出到控制台
print("彩色ASCII艺术：\n", colored_ascii_art)
print("无色ASCII艺术：\n", grayscale_ascii_art)
 """
