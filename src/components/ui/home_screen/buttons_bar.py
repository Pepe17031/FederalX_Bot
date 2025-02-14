import flet as ft

# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------

class SmallMenuButton(ft.Container):
    def __init__(self, image_src: str, text: str, expand: int = 1, margin: ft.Margin = None):
        super().__init__()
        self.visible = True # !!!!!!!!!!!!!!!!!!!!!!

        self.border = border_green
        self.expand = expand
        self.bgcolor = "#222222"
        self.border_radius = 5
        self.margin = margin if margin is not None else ft.Margin(top=60, bottom=0, left=0, right=0)
        self.alignment = ft.alignment.center

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src=image_src,
                    fit=ft.ImageFit.FIT_WIDTH,
                ),
                ft.Text(
                    value=text,
                    size=10,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER,
                )
            ]
        )


# Конкретные кнопки, отличающиеся только изображением и текстом
# --------------------------------------------------------------------
class TaskButton(SmallMenuButton):
    def __init__(self):
        super().__init__(image_src="/button_bar/task.svg", text="Задания")

class FriendsButton(SmallMenuButton):
    def __init__(self):
        super().__init__(image_src="/button_bar/friends.svg", text="Друзья")

class HomeButton(SmallMenuButton):
    def __init__(self):
        # Для HomeButton задаём увеличенный размер и свой отступ
        super().__init__(image_src="/button_bar/home.svg", text="Главная", expand=2,
                         margin=ft.Margin(top=0, bottom=50, left=10, right=10))

class QButton(SmallMenuButton):
    def __init__(self):
        super().__init__(image_src="/button_bar/q.svg", text="Опрос")

class AirdropButton(SmallMenuButton):
    def __init__(self):
        super().__init__(image_src="/button_bar/airdrop.svg", text="Аирдроп")
# --------------------------------------------------------------------


# Группа кнопок реализована как Stack (с фоновым изображением)
# --------------------------------------------------------------------
class ButtonBar(ft.Stack):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.bottom_center
        self.selected_button = None  # Текущая выбранная кнопка

        # Создаём список кнопок
        self.buttons = [
            TaskButton(),
            FriendsButton(),
            HomeButton(),
            QButton(),
            AirdropButton()
        ]
        # Назначаем обработчик клика для каждой кнопки: при клике вызывается select_button
        for btn in self.buttons:
            btn.on_click = lambda e, b=btn: self.select_button(b)

        # Формируем стек: нижний слой – фоновое изображение, поверх – контейнер с кнопками
        self.controls = [
            ft.Container(
                border=border_red,
                alignment=ft.alignment.bottom_center,
                content=ft.Image(
                    src="/button_bar/button_bar_bg.svg",
                    fit=ft.ImageFit.FIT_WIDTH,
                )
            ),
            ft.Container(
                margin=ft.Margin(top=0, bottom=10, left=5, right=5),
                alignment=ft.alignment.bottom_center,
                content=ft.Row(
                    expand=True,
                    controls=self.buttons
                )
            )
        ]

    def select_button(self, btn):
        # Снимаем выделение с ранее выбранной кнопки
        if self.selected_button is not None:
            self.selected_button.bgcolor = "#222222"
            self.selected_button.update()
        # Выделяем новую кнопку
        btn.bgcolor = "#111111"
        btn.update()
        self.selected_button = btn

        # Шаблон для смены экранов – сюда можно добавить логику переключения
        self.switch_screen(btn)

    def switch_screen(self, btn):
        # Пустой шаблон для реализации логики смены экранов
        print("Switching screen for", btn)