import os
import shutil


create_requirements = bool("{{ cookiecutter.create_requirements }}")

if create_requirements:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "requirementss.txt",
        )
    )
