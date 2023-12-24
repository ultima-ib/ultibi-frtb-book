# Introduction

**`ultibi`** is a free(subject to license agreement) python library by **[Ultima](https://github.com/ultima-ib/ultima)**. **`ultibi`** is a framework for building Pivot Tables and Cubes to display and drill through the key metrics for your data.

This userguide will provide examples of the functionality. We pick - **[Fundamental Review of the Trading Book's Standardised Approach](https://en.wikipedia.org/wiki/Fundamental_Review_of_the_Trading_Book)** to serve as a great usecase example due to it's intense compute and memory demands.

# Why to use `ultibi`

- Breakdown and drillthrough your computation

- Everything you need for analysis: [Filtering](./filters.md), [Overriding](./override.md), [Adding Trades](./add_row.md) and so on.

- Blazingly [fast](./performace.md).

# Why to use `ultibi` for **FRTB**

- The calculation goes as per **[FRTB SA Paper](https://www.bis.org/bcbs/publ/d457.pdf)** (Note: `ultibi` is not (yet) certified by ISDA. Always check the output against your own interpretation of the regulation) and aims to be fully compliant(although not certified). **`ultibi`** supports **[CRR2](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/108255)** parameter set out of the box. Switch between the two is as easy as setting `jurisdiction` to `CRR2` or `BCBS`.

- `ultibi` is very flexible and allows you to override any of the prescribed parameters (such as `girr_delta_rho_infl_base_low`) via `calc_params` argument. This essentually means that you can define your own parameter sets as per any regulatory requirements (eg non BCBS/CRR2). This also means that you can **stress test** against changes in the values of the prescribed (aka hard coded by ISDA) parameters.
