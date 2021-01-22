# Reinforcement Learning in Stock Trading Algorithm with Ensemble Approach


## Abstract
Reinforcement learning is a sub-field of machine learning which is getting popularity in the alpha research. Ensemble strategy using multiple reinforcement learning algorithms was proposed in this paper as an alternative to buy and hold approach. Proximal Policy Optimization (PPO), Advantage Actor Critic (A2C) and Deep Deterministic Policy Gradient (DDPG) algorithms were used to build a robust algorithm that can learn the stock market behavior in different environment. The proposed ensemble approach had failed to outperform the buy and hold approach of individual components of S&P 100 index in terms of accumulated return. However, the algorithm had successfully avoid the big plunge in stock market worldwide due to covid-19 crisis in year 2020.

<img src=figs/stock_trading.png width="600">

## Installation:
```shell
git clone https://github.com/seongkiem/wqu_capstone.git
```



### Prerequisites
For [OpenAI Baselines](https://github.com/openai/baselines), you'll need system packages CMake, OpenMPI and zlib. Those can be installed as follows

#### Ubuntu

```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev libgl1-mesa-glx
```

#### Mac OS X
Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the following:
```bash
brew install cmake openmpi
```

#### Windows 10

To install stable-baselines on Windows, please look at the [documentation](https://stable-baselines.readthedocs.io/en/master/guide/install.html#prerequisites).
    
### Create and Activate Virtual Environment (Optional but highly recommended)
cd into this repository
```bash
cd wqu_capstone
```
Under folder /wqu_capstone, create a virtual environment
```bash
pip install virtualenv
```
Virtualenvs are essentially folders that have copies of python executable and all python packages. 

**Virtualenvs can also avoid packages conflicts.**

Create a virtualenv **venv** under folder /wqu_capstone
```bash
virtualenv -p python3 venv
```
To activate a virtualenv:
```
source venv/bin/activate
```

## Dependencies

The script has been tested running under **Python >= 3.6.0**, with the folowing packages installed:

```shell
pip install -r requirements.txt
```

### Questions

### About Tensorflow 2.0: https://github.com/hill-a/stable-baselines/issues/366

If you have questions regarding TensorFlow, note that tensorflow 2.0 is not compatible now, you may use

```bash
pip install tensorflow==1.15.4
 ```

If you have questions regarding Stable-baselines package, please refer to [Stable-baselines installation guide](https://github.com/hill-a/stable-baselines). Install the Stable Baselines package using pip:
```
pip install stable-baselines[mpi]
```

This includes an optional dependency on MPI, enabling algorithms DDPG, GAIL, PPO1 and TRPO. If you do not need these algorithms, you can install without MPI:
```
pip install stable-baselines
```

Please read the [documentation](https://stable-baselines.readthedocs.io/) for more details and alternatives (from source, using docker).


## Run DRL Ensemble Strategy
```shell
python run_DRL.py
```

## Status

<details><summary><b>Version History</b> <i>[click to expand]</i></summary>
<div>

* 1.0.1
	Changes: added ensemble strategy
* 0.0.1
    Simple version
</div>
</details>

## Data
The stock data we use is pulled from yahoo finance.


### Ensemble Strategy
Our purpose is to create a highly robust trading strategy. So we use an ensemble method to automatically select the best performing agent among PPO, A2C, and DDPG to trade based on the Sharpe ratio. The ensemble process is described as follows:
* __Step 1__. We use a growing window of 𝑛 months to retrain our three agents concurrently. In this paper we retrain our three agents at every 3 months.
* __Step 2__. We validate all 3 agents by using a 12-month validation- rolling window followed by the growing window we used for train- ing to pick the best performing agent which has the highest Sharpe ratio. We also adjust risk-aversion by using turbulence index in our validation stage.
* __Step 3__. After validation, we only use the best model which has the highest Sharpe ratio to predict and trade for the next quarter.
<img src=figs/data.PNG width="500">

## Performance
<img src=figs/performance.png>
