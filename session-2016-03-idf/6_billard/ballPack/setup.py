from distutils.core import setup

setup(name="ballPack",
      packages =['ballPack'],
      package_data = {'ballPack': ['data/*.txt']}, 
      scripts = ['script/tkgui.py'],
      )
