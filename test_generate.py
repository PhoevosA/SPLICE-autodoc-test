import os

folder_paths = ['splice-api/app','splice-cli/src/splice_cli','splice-lib/src/splice_lib']

with open("docs/source/Summary.rst", 'w') as f:
  for path in folder_paths:
    python_files = [file for file in os.listdir(path) if file.endswith('.py') and file != "__init__.py"]
    
  
    f.write("Summary" + "\n")
    f.write("=======" + "\n")
    for python_file in python_files:
        module_name = python_file.split(".")[0]
        f.write(".. autosummary::\n")
        f.write("   :toctree: generated")
        f.write("   :recursive:")
        f.write("\n")
        f.write(f"{module_name}")
