from config.BaseConfig import BaseConfig

class ImageConfig(BaseConfig):
    """
    图像配置类，继承自BaseConfig
    """
    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_image_path(self):
        """获取图像路径"""
        return self.config.get('image', 'path', fallback=None)

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


# # 示例：读取配置
# if __name__ == "__main__":
#     # 创建 ImageConfig 实例，读取配置文件
#     image_config = ImageConfig(config_file='config.ini')
    
#     # 获取配置的内容
#     image_path = image_config.get_image_path()
#     image_size = image_config.get_image_size()

#     print(f"Image Path: {image_path}")
#     print(f"Image Size: {image_size}")