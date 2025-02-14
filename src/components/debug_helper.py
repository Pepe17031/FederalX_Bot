import flet as ft

#show_border = True
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None