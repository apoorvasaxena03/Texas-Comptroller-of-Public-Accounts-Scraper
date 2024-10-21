#%%
import subprocess
#%%

def run_notebook():
    notebook_path = r"C:\Users\Apoorva.Saxena\OneDrive - Sitio Royalties\Desktop\Project - Apoorva\Python\Scraping\Texas-Comptroller-of-Public-Accounts-Scraper\scraper.ipynb"
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook_path])

#%%
run_notebook()
#%%
if __name__ == "__main__":
    run_notebook()