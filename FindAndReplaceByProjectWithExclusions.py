import sublime, sublime_plugin
import os
import json

class FindAndReplaceByProjectWithExclusions(sublime_plugin.TextCommand):
  print('reloading FindAndReplaceByProjectWithExclusions')

  def run(self, edit, from_current_file_path=None):

    # Текущее окно сублайма
    window = sublime.active_window()

    # В окне - проект, берём его настройки
    data = window.project_data()

    # Определим exclusions - безопасным извлечением интересуемой настройки из многоуровнего словаря
    # через get.
    exclusions_list = data.get('settings', {}).get("find_and_replace_by_project_with_exclusions")
    exclusions = None
    if exclusions_list is not None:
      exclusions = ', '.join('-' + exclusion for exclusion in exclusions_list)

    # Определим project_path - первый путь из прикреплённых папок в файле
    # проекта.
    sublime_project_file_path = window.project_file_name()
    is_project = sublime_project_file_path is not None
    project_path = None
    if sublime_project_file_path != None:
      project_file = open(sublime_project_file_path)
      json_project = project_file.read()
      dict_project = json.loads(json_project)
      if dict_project is not None and 'folders' in dict_project and dict_project['folders'][0] is not None:
        relative_first_folder_path = dict_project['folders'][0]['path']
        if relative_first_folder_path == '.' or relative_first_folder_path == './':
          relative_first_folder_path = ''
        project_path = os.path.join(os.path.dirname(sublime_project_file_path), relative_first_folder_path)

    # Определим dir_path - путь к директории текущего открытого файла (если
    # таковой открыт).
    dir_path = None
    file_path = self.view.file_name()
    if file_path is not None:
      dir_path = os.path.dirname(file_path)

    # Бизнес логика

    # Определение пути поиска по исходным данным
    search_path = ""
    if from_current_file_path == True and dir_path is not None:
      search_path = dir_path
    elif is_project and project_path is not None:
      search_path = project_path
    elif is_project:
      search_path = "<project>"

    # Дополнение пути поиска исключенем
    where_string = search_path
    if exclusions is not None:
      where_string = search_path + ", " + exclusions

    # Аргументы для открытия панели
    panel_args = {
      "panel": "find_in_files",
      "regex": False,
      "where": where_string
    }

    # if where_string is not None:
    #   panel_args.update({"where": where_string})

    # Показываем панель с настройками в panel_args
    self.view.window().run_command(
      "show_panel",
      panel_args
    )
