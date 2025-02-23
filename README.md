# IC_LLM_NOTEBOOK

A python notebook to interact with DFINITY's [LLM Canister](https://forum.dfinity.org/t/introducing-the-llm-canister-deploy-ai-agents-with-a-few-lines-of-code/41424)

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
