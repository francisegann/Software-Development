import flet as ft 
import random

def main (page: ft.Page):
    def roll(e):
        valor = random.randint(1,6)
        rollNumber.value = str(valor)
        if valor == 1:
            img.src = "/Users/francisegan/Visual Studios/Dice 1.png"
        elif valor == 2:
            img.src = "/Users/francisegan/Visual Studios/Dice 2.jpeg"
        elif valor == 3:
            img.src = "/Users/francisegan/Visual Studios/Dice 3.png"
        elif valor ==4:
            img.src = "/Users/francisegan/Visual Studios/Dice 4.png"
        elif valor == 5:
            img.src = "/Users/francisegan/Visual Studios/Dice 5.jpeg"
        elif valor == 6:
            img.src = "/Users/francisegan/Visual Studios/Dice 6.jpeg" 
        page.update()      
    
    rollNumber = ft.Text(value="No roll yet")
    rollbutton = ft.ElevatedButton(text="Roll Dice",on_click=roll)
    img = ft.Image(src="/Users/francisegan/Visual Studios/Dice 1.png", width=200, height=200)
    
    page.add(rollNumber,rollbutton, img)
    
ft.app(target=main)