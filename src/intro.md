# Introduction

**[Ultima](https://ultimabi.uk/)** is a service which allows you to define, compute and breakdown the key performance metrics of your business.

This user guide is a walk through of `ultibi`, a python library by **Ultima**, applied to a very specific case - **[Fundamental Review of the Trading Book's Standardised Approach](https://en.wikipedia.org/wiki/Fundamental_Review_of_the_Trading_Book)**. For a more general usecase refer to the general user guide. Here we will focus on FRTB only.

# Why to use `ultibi`

- The calculation goes as per **[FRTB SA Paper](https://www.bis.org/bcbs/publ/d457.pdf)** and aims to be fully compliant(although not certified). **[ultibi](https://ultimabi.uk/)** supports **[CRR2](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/108255)** parameter set out of the box. Switch between the two is as easy as setting `jurisdiction` to `CRR2` or `BCBS`.

- `ultibi` is very flexible and allows you to override any of the prescribed parameters (such as `girr_delta_rho_infl_base_low`) via `calc_params` argument. This essentually means that you can define your own parameter sets as per any regulatory requirements (eg non BCBS/CRR2). This also means that you can **stress test** against changes in the values of the prescribed (aka hard coded by ISDA) parameters.

- Everything you need for analysis: [Filtering](./filters.md), [Overriding](./override.md), [Adding Trades](./add_row.md) and so on.

- Blazingly [fast](./performace.md).
