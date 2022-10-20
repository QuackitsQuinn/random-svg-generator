import cairocffi as cairo
import requests
import random



class Generate:
    def __init__(self, width, height, outputfolder):
        self.dimensions = (width, height)
        self.outputfolder = outputfolder
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.context = cairo.Context(self.surface)
        self.colors = self.get_color_pallete()
        print("Got colors")
        self.context.set_source_rgb(*self.colors[2])
        self.context.paint()
        self.colors.pop(2)
        for i in range(0, 40):
            self.drawrandomcircle()
            self.drawrandomarc()
            
        self.gen_frame(self.outputfolder)

    def get_color_pallete(self, model="default"):
        r = requests.post("http://colormind.io/api/", json={"model": model})
        colors = r.json()["result"]
        return [self.convert_color(color) for color in colors]

    def getrandomcolor(self):
        return random.choice(self.colors)

    def convert_color(self, color):
        return color[0] / 255, color[1] / 255, color[2] / 255

    def drawrandomarc(self):
        x = random.randint(0, self.dimensions[0])
        y = random.randint(0, self.dimensions[1])
        radius = random.randint(0, self.dimensions[0])
        start = random.randint(0, 360)
        end = random.randint(0, 360)
        color = self.getrandomcolor()
        self.context.set_line_width(random.randint(3, 10))
        self.context.arc(x, y, radius, start, end)
        self.context.set_source_rgb(*color)
        self.context.set_line_cap(cairo.LINE_CAP_ROUND)
        self.context.stroke()
    
    def drawrandomcircle(self):
        # Draws a random circle at a random pos wi
        x = random.randint(0, self.dimensions[0])
        y = random.randint(0, self.dimensions[1])
        radius = random.randint(0, self.dimensions[0]/30)
        color = self.getrandomcolor()
        self.context.arc(x,y,radius,0,360)
        self.context.fill()
        self.context.set_source_rgb(*color)
        self.context.stroke()

    def gen_frame(self, fn):
        self.surface.write_to_png(fn)


if __name__ == "__main__":
    Generate(1080, 1080, "output.png")
