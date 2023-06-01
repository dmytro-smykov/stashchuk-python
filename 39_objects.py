class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution


img = Image('1920 x 1080', 'Landscape', '.png')

print(img.resolution)

img.resize('4000 x 3000')

print(img.resolution)
