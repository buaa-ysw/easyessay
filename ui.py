import requests
from datetime import datetime
import pytz
import os
import sys
import queue
import threading
import subprocess

from nicegui import ui
from init import output_path
from main import main_run

output_queue = queue.Queue() # 创建队列用于在线程间传递数据
class StdoutRedirector: # 重定向标准输出流到队列中
    def write(self, message):
        output_queue.put(message)
    def flush(self):
        pass
    def isatty(self):
        return False
sys.stdout = StdoutRedirector() # 将标准输出流重定向到队列
def update_log_from_queue(code_log): # 从队列中读取消息并将其输出到日志
    while True:
        message = output_queue.get()
        code_log.push(message)

def main_run_thread(idea, name, run_btn: ui.button, stop_btn: ui.button, spn: ui.spinner):
    run_btn.disable()
    stop_btn.visible = True
    spn.visible = True
    try:
        while not should_stop:
            main_run(idea, name)

    finally:
        # 无论线程如何结束，都会执行此处的代码
        run_btn.enable()
        spn.visible = False
        stop_btn.visible = False
        pass

def stop_main_thread():
    ui.notify('Rebooting...')
    # python = sys.executable
    # subprocess.call([python, "ui.py"])
    # sys.exit()

def start_main_run_thread(idea, name, run_btn: ui.button, stop_btn: ui.button, spn: ui.spinner):
    global should_stop
    should_stop = False
    ui.notify('Thread started')
    thread = threading.Thread(target=main_run_thread, args=(idea, name, run_btn, stop_btn, spn))
    thread.start()
    thread._stop = True

def sync_info():
    url = "https://api.github.com/repos/buaa-ysw/easyessay"

    try:
        response = requests.get(url)
        data = response.json()

        pushed_at = data["pushed_at"]
        pushed_at = datetime.fromisoformat(pushed_at[:-1]) # 解析时间字符串并将其转换为datetime对象
        pushed_at_utc = pushed_at.replace(tzinfo=pytz.utc) # 将datetime对象的时区设置为UTC
        pushed_at_cst = pushed_at_utc.astimezone(pytz.timezone('Asia/Shanghai')) # 将UTC时间转换为中国标准时间
        build_time = pushed_at_cst.strftime('%Y-%m-%d %H:%M:%S') + " (CST)"
    
    # 获取'name'，并设置name_title
        name_title = data.get("name", "Satellite Dispatch [Error]") # 如果字典 data 中包含键 "name"，则它返回相应的值。如果字典中不存在键 "name"，那么它将返回第二个参数提供的默认值
    
    except Exception as e:
        build_time = "Error: " + str(e)
        name_title = "Satellite Dispatch [Error]"
    return build_time,name_title

def sync_galley():
    try:
        galley_container.clear()

        # 获取output_path路径下的所有文件夹
        folders = [folder for folder in os.listdir(output_path) if os.path.isdir(os.path.join(output_path, folder))]

        with galley_container:
            # 为每个文件夹创建一个ui.expansion
            for folder in folders:
                with ui.expansion(folder, icon='folder').classes('w-full'):
                    # 获取output_path + folder文件夹下的所有文件
                    folder_path = os.path.join(output_path, folder)
                    files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
                    # 为每个文件创建一个ui.expansion
                    for file in files:
                        file_path = os.path.join(folder_path, file)
                        file_extension = os.path.splitext(file)[1]
                        if file_extension == '.md':
                            icon = 'summarize'
                        elif file_extension == '.txt':
                            icon = 'text_snippet'
                        else:
                            icon = 'file'
                            pass
                        # Add file content here
                        
                        with open(file_path, 'r') as f:
                            content = f.read()
                        with ui.expansion(file, icon=icon).classes('w-full'):
                            ui.markdown(content)
    except Exception as e:
        ui.notify('Error: ' + str(e), close_button='X', type='negative')

build_time, name_title = sync_info()

# https://fonts.google.com/icons?icon.set=Material+Icons


# ---------------------------------------------------------------------------------------------------------------------------------------------------#
# UI
# ---------------------------------------------------------------------------------------------------------------------------------------------------#


dark = ui.dark_mode()

def on_expansion():
    if dark.value:
        if main_expansion.value:
            main_expansion.style('background-color: #343434')
        else:
            main_expansion.style('background-color: transparent')
        if log_expansion.value:
            log_expansion.style('background-color: #343434')
        else:
            log_expansion.style('background-color: transparent')
    else:
        if main_expansion.value:
            main_expansion.style('background-color: #f0f0f0')
        else:
            main_expansion.style('background-color: transparent')
        if log_expansion.value:
            log_expansion.style('background-color: #f0f0f0')
        else:
            log_expansion.style('background-color: transparent')

with ui.splitter(value=12).classes('w-full h-full') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            dash_board = ui.tab('Dash Board', icon='dashboard')
            playground = ui.tab('Playground', icon='terminal')
            galley = ui.tab('Galley', icon='browse_gallery')
            settings = ui.tab('Settings', icon='settings')

    with splitter.after:
        with ui.tab_panels(tabs, value=dash_board).props('vertical').classes('w-full h-full'):

            #---------------------------------------------------------------------------------------------------------------------------------------------------#

            with ui.tab_panel(dash_board):
                # ui.label('Dash Board').classes('text-h5')
                ui.label('Content of Dash Board')
            
            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                
            with ui.tab_panel(playground):
                with ui.expansion('Easy Essay', icon='token', on_value_change=on_expansion).classes('w-full') as main_expansion:
                    idea_options = ['Earthquake', 'Typhoon', 'Awesome']
                    with ui.input(label='Input an idea', placeholder='start typing', autocomplete=idea_options).classes('w-full') as idea_input:
                        ui.button(icon='clear', on_click=lambda: idea_input.set_value(None)).props('flat color=negative').bind_visibility_from(idea_input, 'value')
                        # ui.button(icon='send', on_click=lambda: ).props('flat color=primary').bind_visibility_from(main_input, 'value')

                    name_options = ['Earthquake', 'Typhoon', 'Awesome']
                    with ui.input(label='Input a name', placeholder='start typing', autocomplete=name_options).classes('w-full') as name_input:
                        ui.button(icon='clear', on_click=lambda: name_input.set_value(None)).props('flat color=negative').bind_visibility_from(name_input, 'value')
                        # ui.button(icon='send', on_click=lambda: ).props('flat color=primary').bind_visibility_from(main_input, 'value')

                    with ui.row():
                        run_spinner = ui.spinner(size='lg')
                        run_spinner.visible = False
                        run_button = ui.button('Run', icon='send', on_click=lambda: start_main_run_thread(idea_input.value, name_input.value, run_button, stop_button, run_spinner)).bind_enabled_from(idea_input, 'value').bind_enabled_from(name_input, 'value').props('color=primary')
                        stop_button = ui.button('Stop', icon='do_not_disturb_on', on_click=lambda: stop_main_thread()).props('color=negative')
                        stop_button.visible = False
                        # ui.spinner(size='lg').bind_visibility_from(run_button, 'enabled')
                
                with ui.expansion('Log', icon='code', on_value_change=on_expansion).classes('w-full h-100') as log_expansion:
                    with ui.row():
                        ui.button('Copy', icon='content_copy').props('flat color=primary')
                        ui.button('Clear', icon='clear_all', on_click=lambda: code_log.clear()).props('flat color=negative')
                    code_log = ui.log(max_lines=100).classes('w-full h-full')

            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                    
            with ui.tab_panel(galley):
                with ui.row():
                    ui.label('Galley').classes('text-h5')
                    ui.space()
                    ui.button('Refresh', icon='refresh', on_click=lambda: sync_galley()).props('color=primary')
                ui.label('History of Eassy processing...')     
                galley_container = ui.column().classes('w-full h-full')
                sync_galley()

            #---------------------------------------------------------------------------------------------------------------------------------------------------#
                
            with ui.tab_panel(settings):
                # ui.label('Settings').classes('text-h4')
                ui.label('Content of settings')

with ui.footer().style('background-color: #3874c8') as ui_footer:
    ui.label('Last build: ').props('color=white')
    ui.label(build_time).props('color=white')

class DarkButton(ui.button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._state = False
        self.props('flat color=white no-border')
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        self._state = not self._state
        dark.toggle()
        self.update()

    def update(self) -> None:
        self.props(f'icon={"dark_mode" if self._state else "light_mode"}')
        ui_header.style(f'background-color: {"#1f4e88" if self._state else "#3874c8"}')
        ui_footer.style(f'background-color: {"#1f4e88" if self._state else "#3874c8"}')
        # ui_left_drawer.style(f'background-color: {"#b0b9cf" if self._state else "#ebf1fa"}')
        on_expansion()
        # self.props(f'color={"grey" if self._state else "white"}')
        super().update()

with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between') as ui_header:
    # ui.button(on_click=lambda: ui_left_drawer.toggle(), icon='menu').props('flat color=white')
    ui.label(name_title).classes('text-h5 bold')
    ui.space()
    # ui.button(icon='dark_mode', on_click=lambda: dark.toggle()).props('flat color=white no-border')
    DarkButton('')

# 创建一个新线程来从队列中读取消息并将其输出到日志中
update_thread = threading.Thread(target=update_log_from_queue, args=(code_log,))
update_thread.daemon = True
update_thread.start()

ui.run()