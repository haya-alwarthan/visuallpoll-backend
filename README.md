# Steps needed to run the project locally: 
1. extract the content of static.zip
ensure you have similar file structure
![image](https://user-images.githubusercontent.com/111225040/213848310-731759d1-b2f5-449e-8317-5ebc89ab2d0a.png)


2. Create a virtual enviroment with python verion>=3.7 & <3.11(3.9 is preferred) and run install the requirements with commands:
```
py -m virtualenv -p="<path to python-exe >" venv
.\venv\Scripts\activate
pip install -r requiremnts.txt
```
3. run the server:
```
python -m flask run
```

