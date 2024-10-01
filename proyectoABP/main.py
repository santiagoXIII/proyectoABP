import flet as ft


def main(page: ft.Page):
    page.title="proyectoABP"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor="#337aff"
    label=ft.Text("Las STEM en la historia universal")
    
    imgLogo=ft.Image(src="logocetis.jpg",width=200,height=200)
    page.add(label,imgLogo)
ft.app(main)
