# IC_LLM_NOTEBOOK

A python notebook to interact with DFINITY's [LLM Canister](https://forum.dfinity.org/t/introducing-the-llm-canister-deploy-ai-agents-with-a-few-lines-of-code/41424)

```python
MODEL = "llama3.1:8b"

system_prompt = "You are a helpful assistant."
user_prompt = "How big is the sun?"
messages = []
messages = call_llm_canister(
    model=MODEL,
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    messages=messages,
    debug_verbose=0,
)

# Print the whole conversation
print("---------------------------------------------------------")
print("This is the full conversation with the LLM Canister:")
pprint.pprint(messages)
```

Gives this result:
```bash
---------------------------------------------------------
This is the full conversation with the LLM Canister:
[{'content': 'You are a helpful assistant.', 'role': {'system': None}},
 {'content': 'How big is the sun?', 'role': {'user': None}},
 {'content': 'The sun is the star at the center of our solar system and is '
             'massive. Here are a few key dimensions to help you understand '
             'its size:\n'
             '\n'
             "1. **Diameter**: The sun's diameter is approximately 1,392,684 "
             'kilometers (865,374 miles). This is about 109 times larger in '
             'diameter than the Earth.\n'
             '\n'
             '2. **Radius**: If we calculate the radius by dividing the '
             'diameter by 2, we get approximately 696,000 kilometers (432,000 '
             "miles) as the sun's radius.\n"
             '\n'
             "3. **Volume**: The sun's volume is enormous due to its large "
             'size. Its volume is approximately 1.412 x 10^18 km^3 (3.938 x '
             '10^17 mi^3). This is about 1.3 million times larger than the '
             'total volume of Earth.\n'
             '\n'
             "4. **Mass**: The sun's mass is about 2 x 10^30 kilograms, or "
             'approximately 330,000 times heavier than the Earth.',
  'role': {'assistant': None}}]
```

# Setup

## Install dfx

```bash
sh -ci "$(curl -fsSL https://internetcomputer.org/install.sh)"

# Configure your shell
source "$HOME/.local/share/dfx/env"
```

## Clone the repo

```bash
# Clone this repo
git clone git@github.com:onicai/ic_llm_notebook.git
```

## Create a Python environment with dependencies installed

We recommend using [Miniconda](https://docs.anaconda.com/miniconda/install/)

```bash
# create a conda environment
conda create --name ic-llm python=3.11
conda activate ic-llm

# from ic_llm_notebook root folder
pip install -r requirements.txt
```

## VS Code

- Open the notebook: `ic-llm.ipynb`
- As kernel select the conda environment: `ic-llm`
- Run
