# itch_backend

# environment/package management

1. <code>\$ virtualenv myenv </code>

### Unix/MacOS

2. <code>\$ source myenv/bin/activate</code>

### Windows

2. <code>\$ myenv\Scripts\activate.bat</code>

## install packages

3. <code>\$ pip install -r requirements.txt</code>

## add packages

4. <code>\$ pip install mypackage</code>

## update environment

5. <code>\$ pip freeze > requirements.txt</code>

# run app locally (without docker)

<code>\$ uvicorn main:app --reload</code>
