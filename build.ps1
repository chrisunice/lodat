pip-chill > .\requirements.txt
del .\dependencies\*
pip download -r .\requirements.txt --dest U:\PyPI
python setup.py bdist_wheel --dist-dir U:\PyPI

# remove some of the junk files
del .\build\ -r -Force
del .\*.egg-info -r -Force
del .\*.pytest_cache -r -Force