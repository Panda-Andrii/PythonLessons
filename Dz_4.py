class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
        print("Камера увімкнена")

    def take_photo(self):
        print("Роблю фото з яскравістю {self.resolution} у міліпікселях")
