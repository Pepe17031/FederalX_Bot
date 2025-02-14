import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from flet.core.theme import Theme

from components.ui.home_screen.buttons_bar import ButtonBar
from components.ui.home_screen.user_bar import ProgressBar
from components.ui.home_screen.body_block import BodyBlock


# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------


def main(page: ft.Page):

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

    page.add(
        ft.Column(
            expand=True,
            spacing = 0,
            wrap=False,
            controls=[
                ft.Container( # User Bar
                    border=border_red,
                    expand=5,
                    content=ProgressBar(),
                ),
                ft.Container(  # Body
                    border=border_red,
                    expand=28,
                    content=BodyBlock(page),
                ),
                ft.Container(  # Button Bar
                    border=border_red,
                    expand=10,
                    content=ButtonBar()
                )
            ]
        )
    )

ft.app(main)