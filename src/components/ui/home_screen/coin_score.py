import flet as ft

# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------


class CoinScore(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand=2
        self.border=border_green
        self.alignment=ft.alignment.top_center
        self.margin=ft.Margin(top=0, bottom=0, left=0, right=0)
        self.padding=0
        self.content=ft.Row(
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
        )