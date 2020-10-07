# FindAndReplaceByProjectWithExclusions

Sublime provides settings for excluding paths from the indexing process, as well
as settings for excluding paths from the sidebar (from the project). However,
there is no setting to exclude files from "project file search".

The project may contain logs or other data files that should be present in the
project, but they should not be searched, since the files are large or we want
to search only by code.

The package will allow you to configure exclusions separately for each project.

## Install

| ОС            | Команды                                                                                   |
| ---           | ---                                                                                       |
| Mac           | `cmd+shift+p` → Package Control: Install Package → FindAndReplaceByProjectWithExclusions  |
| Linux/Windows | `ctrl+shift+p` → Package Control: Install Package → FindAndReplaceByProjectWithExclusions |

## Settings

1. Add exceptions to project file `alt+p` &#8594; Edit Project:

```json
{
  "settings":
  {
    "find_and_replace_by_project_with_exclusions": [
      "*.log",
      "*.sqlite3",
      "node_modules/",
      "db/migrate/"
    ]
  }
}
```

2. Assign keyboard shortcut `alt+n` &#8594; Key Bindings:

```json
[
  // Find And Replace By Project With Exclusions
  { "keys": ["ctrl+k", "ctrl+f"], "command": "find_and_replace_by_project_with_exclusions" },
  {
    "keys": ["ctrl+shift+k", "ctrl+shift+f"],
    "command": "find_and_replace_by_project_with_exclusions",
    "args": {"from_current_file_path": true}
  }
]
```
