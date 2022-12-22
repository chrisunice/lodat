pip-chill > .\requirements.txt
del .\dependencies\*
pip download -r .\requirements.txt --dest .\dependencies
python setup.py bdist_wheel --dist-dir U:\PyPI