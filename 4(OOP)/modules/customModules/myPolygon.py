class Polygon:
    __width = None  #private, won't be accisable by the sub classes 
    __height = None #private

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height