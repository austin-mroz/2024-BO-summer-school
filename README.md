
<h1 align="center">
    <br>
    <img src="./imgs/loop.png" alt="Web-BO" width="200">
    <br>
    Bayesian optimization for guided chemical design
    <br>
</h1>

<h4 align="center">Notebooks and scripts to support Sargent Centre for Process Systems Engineering 2024 BO Summer School</h4>

<p align="center">
    <a href="#key-features">key features</a> •
    <a href="#installation-instructions">installation instructions</a> •
    <a href="#examples">examples</a> •
    <a href="#acknowledgements">acknowledgements</a> •
    <a href="#license">license</a>
</p>

<br>

## key features

This repo contains tutorial notebooks and additional resources for the 2024 Sargent Process Engineering Bayesian optimization summer shool.

## installation instructions

```console
foo@bar:~$ git clone https://github.com/austin-mroz/2024-BO-summer-school
foo@bar:~$ cd 2024-BO-summer-school
foo@bar:~/webBO$ conda env create -p ./.venv -f environment.yml
foo@bar:~/webBO$ conda activate ./.venv
```

## optimisation task demonstration

To help you get familiar with all that Web-BO has to offer, we provide an optimization case study that takes advantage of existing reaction emulators to acquire the experimental measurements.

This case study concerns optimizing the coupling of 3-bromoquinoline with
3,5-dimethylisoxazole-4-boronic acid pinacol ester in the presence of
1,8-diazobicyclo[5.4.0]undec-7-ene (DBU) and THF/water, Figure 1.

<h5 align="center">
<img src="./imgs/reizman_reaction.png"
    class="img-fluid" width="300">

Figure 1. Suzuki-Miyaura cross-coupling reaction involved in this case study.
</h5>
The parameter space involved in this optimisation task is detailed in Figure 2.

<h5 align="center">
<img src="./imgs/parameter_space.png" class="img-fluid" width="300">

Figure 2. Parameter space spanned by this
case study includes 3 continuous variables (catalyst loading, temperature,
and residence time) and 1 categorical variable (catalyst).
</h5>
The catalyst options are presented in Figure 3.

<h5 align="center">
<img src="./imgs/catalyst_options.png" class="img-fluid" width="300">

Figure 3. The catalyst options included in
this study.

</h5>

This case study takes advantage of the experiment emulators offered by the <a    zhref="https://github.com/sustainable-processes/summit" class="tooltip-test" title="Tooltip">Summit</a> package. Specifically, the <a href="https://gosummit.readthedocs.io/en/latest/experiments_benchmarks/implemented_benchmarks.html#cross-coupling-emulator-benchmarks" class="tooltip-test" title="Tooltip">Suzuki-Miyaura Cross Coupling Emulator</a>.

## acknowledgements
This work was co-developed by Dr. Lauren Lee (Assistant Professor, UCL) and Dr. Austin Mroz (AI in Science Research Fellow, Imperial College London)

## license
