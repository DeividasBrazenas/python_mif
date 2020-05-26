from distutils.core import setup, Extension

module = Extension('prime',
                    include_dirs=['C:\\Git\\python_mif\\PythonExercises\\4'],
                    libraries=['pthread'],
                    sources=['primemodule.c']
                    )

setup(name='prime',
      version='1.0',
      description='Prime package',
      author='Deividas Brazenas',
      url='www.google.com',
      ext_modules=[module])
