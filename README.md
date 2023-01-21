# Steps needed to run the project locally: 
1. extract the content of static.zip
ensure you have similar file structure
![image](https://user-images.githubusercontent.com/111225040/213848292-7a081c52-b079-42a1-b6a3-0bdcd38aeb66.png)

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

