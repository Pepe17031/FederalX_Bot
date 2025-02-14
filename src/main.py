import warnings
from collections.abc import Container

from components.progress_bar import ProgressBar

warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from flet.core.theme import Theme

from components import show_border, border_red, border_green, border_blue

from components.buttons import (
    TaskButton,
    FriendsButton,
    QButton,
    AirdropButton,
    HomeButton,
    ButtonBar
)
Test = "T1"
def main(page: ft.Page):

    # Настройки страницы
    page.title = "FederalX"
    page.fonts = {
        "Golos": "/fonts/golos_medium.ttf",
        "GolosBold": "/fonts/golos_bold.ttf",
    }
    page.theme = Theme(font_family="Golos")
    page.bgcolor = "#171717"
    page.padding = 0

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

#--------------------------------------------------------------------

# ---------------------------------------------------------------------------

    bodyBlock = ft.Container(
        bgcolor="#232323",
        border=border_red,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#232323", "#171717"],
        ),
        border_radius=10,
        height=1000,
        margin=ft.Margin(top=5, bottom=10, left=20, right=20),
        padding=10, # отступ от контейнера до содержимого

        content=ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container( # ProgressBar
                    expand=2,
                    border=border_green,
                    alignment=ft.alignment.center,

                    margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                    padding=0,
                    content=ft.Column(
                        spacing=0,
                        alignment=ft.alignment.top_center,
                        controls=[
                            ft.Container(
                                margin=ft.Margin(top=5, bottom=0, left=0, right=0),
                                padding=0,
                                alignment=ft.alignment.top_center,
                                border=border_blue,
                                content=ft.Text(
                                    "Level: 5/10",
                                    color="#FFFFFF",
                                    size=10,
                                )
                            ),
                            ft.Container(
                                margin=ft.Margin(top=5, bottom=0, left=0, right=0),
                                padding=0,
                                alignment=ft.alignment.top_center,
                                border=border_blue,
                                content=ft.ProgressBar(
                                    value=0.3,
                                    height=15,
                                    color="#BA1D3F",
                                    bgcolor="#C8B495",
                                    border_radius=10,
                                )
                                #content=ft.Text("Test")
                            )
                        ]
                    ),
                ),
                ft.Container( # Coins Score
                    expand=2,
                    border=border_green,
                    alignment=ft.alignment.top_center,
                    margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                    padding=0,
                    content=ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=0,
                                border=border_green,
                                margin=0,
                                image_fit=ft.ImageFit.CONTAIN,
                                content=ft.Image(
                                    src="coin.png"
                                )

                            ),
                            ft.Container(
                                padding=0,
                                border=border_green,
                                content=ft.Text(
                                    color="#FFFFFF",
                                    spans=[
                                        ft.TextSpan(
                                            text="927 ",
                                            style=ft.TextStyle(font_family="GolosBold", size=30)
                                        ),
                                        ft.TextSpan(
                                            text="230",
                                            style=ft.TextStyle(size=20)
                                        ),
                                    ]
                                )
                            )
                        ]
                    ),

                ),
                ft.Container( # Trump
                    expand=10,
                    border=border_green,
                    alignment=ft.alignment.top_center,
                    margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                    padding=0,
                    content=ft.Stack(

                        controls=[
                            # ft.Container(  # Gradient Перекрывае линейный
                            #     border=border_blue,
                            #     margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                            #     alignment=ft.alignment.center,
                            #     gradient=ft.RadialGradient(
                            #         colors=["#C8B495", "#222222"],
                            #         radius=0.3,
                            #     ),
                            # ),
                            ft.Container(  # Circle1
                                border=border_green,
                                margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                                alignment=ft.alignment.center,
                                content=ft.Image(
                                    src="small_c.svg"
                                )
                            ),
                            ft.Container(  # Circle2
                                border=border_green,
                                margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                                alignment=ft.alignment.center,
                                content=ft.Image(
                                    src="big_c.svg"
                                )
                            ),
                            ft.Container( #Trump
                                border=border_green,
                                margin=ft.Margin(top=5, bottom=0, left=0, right=0),
                                alignment=ft.alignment.top_center,
                                content=ft.Image(
                                    src="trumpd.png"
                                )
                            ),
                            ft.Container( #Coin
                                border=border_red,
                                margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                                alignment=ft.alignment.center,
                                content=ft.Image(
                                    src="coin.png"
                                )
                            ),
                            ft.Container( #Buildding
                                border=border_blue,
                                margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                                alignment=ft.alignment.bottom_center,
                                content=ft.Image(
                                    src="bulding.png"
                                )
                            ),
                        ]
                    ),

                ),
            ]
        )
    )
# ---------------------------------------------------------------------------

    # Отображаемые элементы
    page.add(
        ft.Column(
            expand=True, # Заполнить все пространство
            spacing = 0, # Отступы между элементами
            wrap=False, # Перенос столбцов
            controls=[
                ft.Container(  # Header
                    #border=border_red,
                    expand=5,
                    content=ProgressBar(),
                ),
                ft.Container(  # Body
                    #border=border_red,
                    expand=28,
                    content=bodyBlock,
                ),
                ft.Container(  # Button Bar
                    #border=border_red,
                    expand=10,
                    content=ButtonBar()
                )
            ]
        )
    )

ft.app(main)


# https://flet.dev/docs/reference/types/alignment/ Выравнивание внутри контейнеров
