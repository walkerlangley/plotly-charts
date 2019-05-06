from setuptools import setup

setup(name='plotly_charts',
      version='0.4',
      description='Helper functions for plotly charts',
      url='http://github.com/walkerlangley/plotly-charts#v0.4',
      author='Walker Langley',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['plotly_charts'],
      install_requires=[
          'plotly',
          'pandas',
          'datetime',
          'cufflinks',
          'numpy',
      ],
      zip_safe=False)
