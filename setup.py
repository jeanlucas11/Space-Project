import cx_Freeze
executables = [cx_Freeze.Executable(script="main.py", icon="./assets/icone.png")]
cx_Freeze.setup(
 name="Space do Jean",
 options={"build_exe": {"packages":["pygame"], "include_files":["assets"]}},
 executables = executables
 ) 
