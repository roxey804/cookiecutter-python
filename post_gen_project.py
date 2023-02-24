import os
import shutil

# Perhaps a more advanced python script here  - This isn't currently being used

create_requirements = bool("{{ cookiecutter.action }}")

if action:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "new_file.txt",
        )
    )
