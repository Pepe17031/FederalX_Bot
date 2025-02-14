import flet as ft

# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------


class LvlProgressBar(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = 2
        self.border = border_green
        self.alignment = ft.alignment.center

        self.margin = ft.Margin(top=0, bottom=0, left=0, right=0)
        self.padding = 0
        self.content = ft.Column(
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
                )
            ]
        )