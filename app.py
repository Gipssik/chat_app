import flet as ft


def delete_task(e: ft.ControlEvent, task: ft., tasks):


def add_task(page: ft.Page, task: ft.TextField, tasks: ft.Column):
    task_row = ft.Row(
        [
            ft.Text(task.value, expand=True),
            ft.IconButton(ft.icons.DELETE, on_click=delete_task),
        ]
    )
    task_container = ft.Container(
        task_row,
        padding=20,
        border=ft.border.all(1, ft.colors.BLACK38),
        bgcolor=ft.colors.BLUE_GREY_50,
        border_radius=5,
    )
    tasks.controls.insert(0, task_container)
    task.value = ""
    task.focus()
    page.update()


def main(page: ft.Page):
    page.title = "Todo App"
    page.window_width = 450
    page.window_height = 800
    tasks = ft.Column()
    task = ft.TextField(hint_text="Enter a task...", on_submit=lambda e: add_task(page, task, tasks), expand=True)
    add_button = ft.IconButton(ft.icons.ADD_TASK, on_click=lambda e: add_task(page, task, tasks))
    inputs = ft.Row([task, add_button])
    page.add(inputs, tasks)


ft.app(port=8000, target=main)
