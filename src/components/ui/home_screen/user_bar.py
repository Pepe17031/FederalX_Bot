import flet as ft
# Debug Lines

#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------

class ProgressBar(ft.Container):
    def __init__(self):
        super().__init__()
        self.visible = True # !!!!!!!!!!!!!!!!!!!!!!

        self.bgcolor="#232323"
        self.border_radius=10
        self.height=1000
        self.border=border_red
        self.margin=ft.Margin(top=10, bottom=0, left=20, right=20)  # Отступ от родителя до контейнера
        self.padding=0  # отступ от контейнера до содержимого

        self.content=ft.Row(
            expand=True,
            spacing=0,  # Отступы между элементами
            controls=[
                ft.Container(  # Avatar
                    expand=2,
                    border=border_green,
                    alignment=ft.alignment.center,
                    margin=ft.Margin(top=0, bottom=0, left=10, right=0),
                    padding=7,
                    content=ft.CircleAvatar(foreground_image_src="/avatar.png", radius=100),
                ),
                ft.Container(  # Score
                    expand=4,
                    border=border_green,
                    alignment=ft.alignment.center_left,
                    margin=ft.Margin(top=0, bottom=0, left=10, right=0),
                    padding=0,
                    content=ft.Column(
                        spacing=0,  # Отступы между элементами
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                border=border_blue,
                                content=ft.Text(
                                    color="#FFFFFF",
                                    spans=[
                                        ft.TextSpan(
                                            text="FederalX | ",
                                        ),
                                        ft.TextSpan(
                                            text="LVL 5",
                                            style=ft.TextStyle(font_family="GolosBold")
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                border=border_blue,
                                content=ft.Text(
                                    color="#FFFFFF",
                                    spans=[
                                        ft.TextSpan(
                                            text="Profit/h: ",
                                        ),
                                        ft.TextSpan(
                                            text="1 050$",
                                            style=ft.TextStyle(font_family="GolosBold")
                                        ),
                                    ]
                                )
                            ),

                        ]
                    )
                ),
                ft.Container(  # Energy
                    expand=3,
                    border=border_green,
                    alignment=ft.alignment.top_center,
                    margin=ft.Margin(top=5, bottom=5, left=5, right=5),
                    padding=0,
                    bgcolor="#333333",
                    border_radius=10,
                    content=ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=0,
                                border=border_blue,
                                content=ft.Image(
                                    src="energy.png",
                                )

                            ),
                            ft.Container(
                                border=border_blue,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                    controls=[
                                        ft.Text("997", style=ft.TextStyle(font_family="GolosBold"), color="#FFFFFF"),
                                        ft.Text("/1000", color="#FFFFFF"),

                                    ]
                                )

                            )
                        ]
                    )

                )
            ]
        )
