## Steps needed to run the project locally: 
1. extract the content of static.zip, ensure you have similar folder structure
![image](https://user-images.githubusercontent.com/111225040/213848310-731759d1-b2f5-449e-8317-5ebc89ab2d0a.png)
2. Create a virtual enviroment with python verion>=3.7 & <3.11(3.9 is preferred) and run install the requirements with commands(or any other commands that achieve similar purpose):
```
py -m virtualenv -p="<path to python-exe >" venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
3. run the server:
```
python -m flask run
```

## Debugging
Ensure pip is already installed in your virtual environment(on windows machine)
```
py -m ensurepip --upgrade 
```
