from distutils.core import setup
setup(
  name = 'eazymind',         # How you named your package folder (MyLib)
  packages = ['eazymind','eazymind/nlp'],   # Chose the same as "name",
  version = '0.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'AI Library providing ai-as-a-service for abstractive text summarization , just your text to be summarized and key obtained from free registeration on eazymind and a summary would be provided , get key from http://eazymind.herokuapp.com/arabic_sum',   # Give a short description about your library
  author = 'amr zaki',                   # Type in your name
  author_email = 'theamrzaki@hotmail.com',      # Type in your E-Mail
  url = 'https://github.com/theamrzaki/eazymind',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/theamrzaki/eazymind/archive/v0.0.3.tar.gz',    # I explain this later on
  keywords = ['nlp', 'text', 'summarization' , 'ai' ,'natural language processing'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7', 
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)