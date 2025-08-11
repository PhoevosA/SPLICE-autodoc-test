import os

folder_paths = ['splice-api/app','splice-cli/src/splice_cli','splice-lib/src/splice_lib']

for path in folder_paths:
  python_files = [f for f in os.listdir(path) if f.endswith('.py') and f != "__init__.py"]
  page_name = path.split("/")[0]
  page_name = page_name.split("-")[1].capitalize()
  rst_filename = f"{page_name}.rst"
  with open(os.path.join("docs/source", rst_filename), 'w') as f:
  
  
    f.write(f"{page_name}\n")
    f.write("=" * len(page_name))
    for python_file in python_files:
        module_name = os.path.splitext(python_file)[0]
        f.write(f"\n{python_file}\n")
        f.write("^" * len(python_file) + "\n")
        f.write("\n")
        f.write(f".. autosummary::\n")
        f.write("   :toctree: generated\n")
        f.write("   :recursive:\n")
        f.write("\n")
        f.write("\n{module_name}\n")
        f.write("\n")
        f.write(f".. automodule:: {module_name}\n")
        f.write("   :member-order: groupwise\n")
        f.write("   :members:\n")
        f.write("   :undoc-members:\n")
        f.write("   :show-inheritance:\n") 

