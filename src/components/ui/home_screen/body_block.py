import flet as ft

from components.ui.home_screen.lvl_progress_bar import LvlProgressBar
from components.ui.home_screen.coin_score import CoinScore
from components.ui.home_screen.click_zone import ClickZone

# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------


class BodyBlock(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        w = page.width
        h = page.height
        self.visible = True # !!!!!!!!!!!!!!!!!!!!!!
        self.bgcolor="#232323"
        self.border=border_red
        self.gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#232323", "#171717"],
        )
        self.border_radius=10
        self.height=1000
        self.margin=ft.Margin(top=5, bottom=10, left=20, right=20)
        self.padding=10 # отступ от контейнера до содержимого

        self.content=ft.Column(
            expand=True,
            spacing=0,
            controls=[
                LvlProgressBar(),
                CoinScore(),
                ClickZone(w, h),
            ]
        )
