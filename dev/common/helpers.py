import importlib.resources


def get_resources_file(file_name: str) -> str:
    with importlib.resources.path('resources', file_name) as path:
        return str(path)
