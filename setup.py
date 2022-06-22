import cx_Freeze

executables = [cx_Freeze.Executable(
base="Win32GUI",
    script="cobrinha.py", icon="assets/icon.ico")]

cx_Freeze.setup(
    name="Cobrinha",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)