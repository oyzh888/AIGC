# AItist 


## Environment set up
1. Set up the python environment
- Set open AI key
Please go to openai playground to setup your own openAI key. And modify the `os.environ["OPENAI_API_KEY"] ` at ` python_backend/utils.py`
- Run
```bash
cd python_backend
pip install -r requirements.txt
```

2. Set up figma environment
- Download figma desktop version from https://www.figma.com/downloads/
- https://www.figma.com/plugin-docs/setup

```bash
sudo npm install -g typescript
# Open your figma app
# Go to Menu > Plugins > Development > New Plugin...
# Or bind the existing figma plugin at `AItist/figma_plugin`

cd figma_plugin
npm install --save-dev @figma/plugin-typings

# Open VScode
# ⌘⇧B (Ctrl-Shift-B for Windows)
# Select tsc: watch - tsconfig.json
```


## Run the example code
Download figma file from 
https://www.figma.com/file/IFT6MeKwPzBTAX5W8XyrOT/Untitled?node-id=0%3A1&t=9zArGGbJ0SK2a95P-1

Backend
```bash
cd python_backend
sh run.sh
```

Frontend

Follow instuctions at https://www.figma.com/plugin-docs/setup
and use Figma App and VS code to run the plugin at `AItist/figma_plugin`

## Hint
It's recommended to download a https://www.postman.com to test the APIs

More info:
[AItist Dev Environment](https://nxkc7zi6j8.larksuite.com/wiki/wikuskEtd4Y3Yqp1rQbfRLXdDtf)



