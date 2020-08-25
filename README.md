# itch_backend

`PYTHON 3.7.2`

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

# Test model-->

- once get `get_predictions` in `predictions_handler.py` is good to go and uncomment the commented lines
- `virtual_env` is activated with all DS packages for model installed
- `test_imgs` directory populated

  ### in terminal from root proj directory run

  ## <code>\$ sh model_test.sh</code>

  # DO NOT FORGET TO PIP FREEZE AND COMMIT TO SEPARATE BRANCH
