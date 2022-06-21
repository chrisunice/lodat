pip freeze > .\requirements.txt
pip download -r .\requirements.txt --dest .\dependencies
#python setup.py bdist_wheel