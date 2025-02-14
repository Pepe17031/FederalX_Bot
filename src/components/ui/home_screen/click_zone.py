import math, random, asyncio
import flet as ft

# Debug Lines
#--------------------------------------------------------------------
show_border = False
border_red = ft.border.all(3, ft.Colors.RED_600) if show_border else None
border_green = ft.border.all(2, ft.Colors.GREEN_600) if show_border else None
border_blue = ft.border.all(1, ft.Colors.BLUE_600) if show_border else None
#--------------------------------------------------------------------


class ClickZone(ft.Container):
    def __init__(self, w, h):
        super().__init__()
        self.expand=10
        self.border=border_green
        self.alignment=ft.alignment.top_center
        self.margin=ft.Margin(top=0, bottom=0, left=0, right=0)
        self.padding=0
        self.w=w
        self.h=h
        self.isolated = True
        self.on_click = self.handle_click
        self.animating = False


        self.score_counter = ft.Text(
            size=20,
            animate_opacity=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE_IN_OUT),
            opacity=0,  # начальное значение прозрачности
            color="#FFFFFF"
        )

        self.coin_container = ft.Container(
            border=border_red,
            margin=ft.Margin(0, 0, 0, 0),
            alignment=ft.alignment.center,
            left=(self.h - 50) / 2,   # начальное значение
            top=(self.w - 10) / 10,    # начальное значение
            content=ft.Image(src="coin.png"),
            opacity = 0,  # начальное значение прозрачности

        )

        self.content=ft.Stack(
            controls=[
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
                ft.Container(  # Trump
                    border=border_green,
                    margin=ft.Margin(top=5, bottom=0, left=0, right=0),
                    alignment=ft.alignment.top_center,
                    content=ft.Image(
                        src="trumpd.png"
                    )
                ),
                self.coin_container,
                ft.Container(  # Buildding
                    border=border_blue,
                    margin=ft.Margin(top=0, bottom=0, left=0, right=0),
                    alignment=ft.alignment.bottom_center,
                    content=ft.Image(
                        src="bulding.png"
                    )
                ),
                self.score_counter
            ]
        )


    async def score_anim(self):

        # Задаем размер шрифта
        self.score_counter.size = random.randrange(20, 30, 1)

        # Задаем радиус, на котором должны появляться цифры
        radius = random.randrange(100, 120, 1)  # например, 50 пикселей

        # Задаем углы
        if random.choice([True, False]):
            # Правая сторона: от -60° до 60°
            #angle = random.uniform(-math.radians(20), math.radians(60))
            angle = random.uniform(math.radians(0), -math.radians(60))
        else:
            # Левая сторона: от 120° до 240°
            angle = random.uniform(math.radians(180), math.radians(240))

        offset_x = radius * math.cos(angle)
        offset_y = radius * math.sin(angle)
        print(self.w, self.h)
        center_xx = (self.h - 50) / 2
        center_yy = self.w / 6

        # Позиционируем временный текст относительно центра плюс случайное смещение
        self.score_counter.value = "+1"
        self.score_counter.opacity = 1
        self.score_counter.left = center_xx + offset_x
        self.score_counter.top = center_yy + offset_y
        self.score_counter.right = 0
        self.score_counter.bottom = 0

        self.update()  # Обновляем ClickZone

        await asyncio.sleep(0.5)

        self.score_counter.opacity = 0
        self.update()

    async def coin_anim(self):
        if self.animating:
            return
        self.animating = True

        # Анимируем падение монеты:
        # Допустим, монета должна упасть на 200 пикселей вниз
        fall_distance = 200
        steps = 20
        delay = 0.01  # секунд между шагами

        initial_top = self.coin_container.top if self.coin_container.top is not None else 0
        # Гарантируем, что монета видима
        self.coin_container.opacity = 1
        self.coin_container.update()

        # Анимация падения: постепенно увеличиваем значение top
        for i in range(steps):
            new_top = initial_top + fall_distance * ((i + 1) / steps)
            self.coin_container.top = new_top
            self.coin_container.update()
            await asyncio.sleep(delay)

        # После падения делаем монету невидимой
        self.coin_container.opacity = 0
        self.coin_container.update()

        # Также можно вернуть монету в исходное положение для повторного использования
        self.coin_container.top = initial_top
        self.coin_container.opacity = 1
        self.coin_container.update()
        self.animating = False





    async def handle_click(self, event: ft.ContainerTapEvent):
        await self.score_anim()
        await self.coin_anim()