import zc.recipe.egg

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.bin = buildout['buildout']['bin-directory']
        
    def install(self):
        zc.recipe.egg.Egg(self.buildout, 'Shinken', {'eggs': 'Shinken'})
        

    update = install
