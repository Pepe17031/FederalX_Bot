# Используем официальный образ Python (подберите нужную версию, например, 3.10)
FROM python:3.12-slim

# Устанавливаем зависимомти
#RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y curl build-essential

# Устанавливаем Rust через rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . /app

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

RUN poetry install

# Если нужно установить flet-desktop или другие зависимости:
# RUN pip install --no-cache-dir flet[all]

# Открываем порт 8000
EXPOSE 8000

# Запускаем приложение Flet.
CMD ["poetry", "run", "flet", "run", "--web", "--host", "0.0.0.0", "--port", "8000"]
