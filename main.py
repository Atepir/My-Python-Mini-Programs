import Drawing
import Conversio
import Playing
import time

while True :
    time.sleep(3)
    Drawing.MyPaintApp().run()
    time.sleep(3)
    Conversio.exec()
    Playing.main().run()
    time.sleep(28)