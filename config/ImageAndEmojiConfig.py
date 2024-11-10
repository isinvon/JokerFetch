import ast
import random
from config.BaseConfig import BaseConfig

class ImageAndEmojiConfig(BaseConfig):
    """
    图像配置类，继承自BaseConfig
    """
    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()
        
    def get_image_type(self):
        """
        获取图像类型

        返回值：
        str -- 图像类型
        """
        return self.config.get('image', 'type', fallback=None)

    def get_image_width(self):
        """
        获取图像宽度
        
        返回值：
        int -- 图像宽度
        """
        return int(self.config.get('image', 'width', fallback=None))
    
    def get_image_height(self):
        """
        获取图像高度
    
        返回值：
        int -- 图像高度
        
        """
        return int(self.config.get('image', 'height', fallback=None))
    
    def get_image_scale(self):
        """
        获取图像缩放比例
        
        返回值：
        int -- 图像缩放比例
        """
        
        return int(self.config.get('image','scale', fallback=None))

    def get_image_path(self):
        """ 
        
        获取图像路径
        
        返回值：
        str -- 图像路径
        """
        type = self.get_image_type()
        
        # 获取字符串类型的列表
        list =  self.config.get(type, 'image', fallback=None)
        
        # 将字符串类型的列表转化为列表类型
        image_path_list = ast.literal_eval(list)

        image_count =  image_path_list.__len__()
        
        # 随机获取一个图片路径
        index =  random.randint(0, image_count-1)
        
        return image_path_list[index]
    
    def get_emoji(self):
        """
        获取emoji

        返回值：
        str -- emoji
        """
        type = self.get_image_type()

        emoji =  self.config.get(type, 'emoji', fallback=None)
        
        return emoji
    
    def get_talk(self):
        """
        获取talk

        返回值：
        str -- talk
        """
        type = self.get_image_type()

        # 获取字符串类型的列表
        list =  self.config.get(type, 'talk', fallback=None)
        
        # 将字符串类型的列表转化为列表类型
        talk_list = ast.literal_eval(list)

        talk_count =  talk_list.__len__()
        
        # 随机获取一个图片路径
        index =  random.randint(0, talk_count-1)
        
        return talk_list[index]