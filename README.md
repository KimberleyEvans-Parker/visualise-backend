# visualise-backend

This is the backend that will be used to provide visualisations for the frontend

## Developing

Firstly, generate a virtual environment as so:

```sh
python3 -m venv .env
```

This will create a directory called `.env`, which will contain your virtual environment. To actually activate the environment, source the relevant `activate` script nestled under `.env/bin` (e.g. `.env/bin/activate` for bash, or `.env/bin/Activate.ps1` for PowerShell). To exit the virtual environment, just use the command `deactivate`.

Once activated, direct your IDE/Editor to use the python within your virtual environment. In VSCode press `CTRL + SHIFT + P` to open the command menu, then enter `Python: Select Interpreter`, and hit `Enter`. You will need to navigate the list down to the one that contains a python within your `$CURRENT_DIRECTORY/.env/bin` directory.

Now you will need to install the required dependencies via:

```sh
pip install -r requirements.txt
```

Now you should be all set to go!
