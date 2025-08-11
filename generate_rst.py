import os

folder_paths = ['splice-api/app','splice-cli/src/splice_cli','splice-lib/src/splice_lib']

for path in folder_paths:
  python_files = [f for f in os.listdir(path) if f.endswith('.py')]
  page_name = path.split("/")[0]
  rst_filename = f"{page_name}.rst"
  with open(os.path.join("docs/source", rst_filename), 'w') as f:
  
  
    f.write(f"{page_name}\n")
    f.write("=" * len(page_name) + "\n")
    for python_file in python_files:
        module_name = os.path.splitext(python_file)[0]
      
        f.write(f"{module_name}\n")
        f.write("-" * len(page_name) + "\n")
        f.write("\n")
        f.write(f".. automodule:: {module_name}\n")
        f.write("   :members:\n")
        f.write("   :undoc-members:\n")
        f.write("   :show-inheritance:\n")
        
