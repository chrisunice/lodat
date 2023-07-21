subst U: C:\VaultNet
python.exe -m pip install --upgrade pip
pip-chill > .\requirements.txt
pip download -r .\requirements.txt --dest U:\PyPI