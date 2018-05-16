import sys
from PIL import Image

class ImageWithFit:

    def __init__(self, path, thumbName = "fav.png", extension = "PNG"):
        self.originalPath = path
        self.originalImage = Image.open(path)
        self.thumbName = thumbName
        self.extension = extension

    def imageIsSquare(self):
        answer = True
        if self.originalImage.width != self.originalImage.height:
            answer = False
        return answer

    def fitImage(self, size):
        imageTmp = self.originalImage
        if self.imageIsSquare == False:
            cropSize = self.originalImage.width
            if self.originalImage.width > self.originalImage.height:
                cropSize = self.originalImage.height
                imageTmp = self.cropFromCenter([cropSize])
        print(size)
        imageTmp.thumbnail(size)
        imageTmp.save(self.thumbName, self.extension)
            
    def cropFromCenter(self, size):
        newWidth = size[0]
        newHeight = size[0]


        if len(size) > 1:
            newHeight = size[1]


        oldWidthTmp = self.originalImage.width
        oldHeightTmp = self.originalImage.height
        changeXPosition = 0
        changeYPosition = 0

        if (oldWidthTmp - newWidth) % 2 != 0 and oldWidthTmp != newWidth:
            oldWidthTmp += 1
            changeXPosition = 1
        if (oldHeightTmp - newHeight) % 2 != 0 and oldHeightTmp != newHeight:
            oldHeightTmp += 1
            changeYPosition = 1
        
        

        left = ((oldWidthTmp - newWidth)/2) - changeXPosition
        top = ((oldHeightTmp - newHeight)/2) - changeYPosition
        right = ((oldWidthTmp + newWidth)/2) - changeXPosition
        bottom = ((oldHeightTmp + newHeight)/2) - changeYPosition

        return self.originalImage.crop((left, top, right, bottom))



class Favinator:

    sizes = (
        (192, 192),
        (180, 180),
        (152, 152),
        (144, 144),
        (120, 120),
        (114, 114),
        (96, 96),
        (76, 76),
        (72, 72),
        (60, 60),
        (57, 57),
        (32, 32),
        (16, 16)
   

    )

    def __init__(self, path, extension = "png"):
        self.extension = extension
        self.imaginator = ImageWithFit(path)
        self.path = path
        self.html = """
            <link rel="apple-touch-icon" sizes="57x57" href="/ico-57.{ext}">
            <link rel="apple-touch-icon" sizes="60x60" href="/ico-60.{ext}">
            <link rel="apple-touch-icon" sizes="72x72" href="/ico-72.{ext}">
            <link rel="apple-touch-icon" sizes="76x76" href="/ico-76.{ext}">
            <link rel="apple-touch-icon" sizes="114x114" href="/ico-114.{ext}">
            <link rel="apple-touch-icon" sizes="120x120" href="/ico-120.{ext}">
            <link rel="apple-touch-icon" sizes="144x144" href="/ico-144.{ext}">
            <link rel="apple-touch-icon" sizes="152x152" href="/ico-152.{ext}">
            <link rel="apple-touch-icon" sizes="180x180" href="/ico-180.{ext}">
            <link rel="icon" type="image/{ext}" sizes="192x192"  href="/ico-192.{ext}">
            <link rel="icon" type="image/{ext}" sizes="32x32" href="/ico-32.{ext}">
            <link rel="icon" type="image/{ext}" sizes="96x96" href="/ico-96.{ext}">
            <link rel="icon" type="image/{ext}" sizes="16x16" href="/ico-16.{ext}">
            <link rel="manifest" href="/manifest.json">
            <meta name="msapplication-TileImage" content="/ico-144.{ext}">
            <!-- Optional u can change colors of tile and chrome cart -->
            <meta name="msapplication-TileColor" content="#ffffff">
            <meta name="theme-color" content="#ffffff">
        """.format(ext = extension)



    def run(self):
        if self.imaginator.imageIsSquare() == False:
            print("Warning: use square dimension for the best performance")

        htmlFile = open("fav.html", "w")
        htmlFile.write(self.html)
        htmlFile.close()
        
        for s in self.sizes:
            self.imaginator.thumbName = "ico-" + str(s[0]) + "." + self.extension
            self.imaginator.fitImage(s)


        


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fav = Favinator(sys.argv[1])
    else:
        fav = Favinator("fav.png")

    fav.run()
