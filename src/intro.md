# Introduction

**[ultima](https://ultimabi.uk/)** is a tool which allows you to define, compute and breakdown the key performance metrics of your business.

This user guide is a walk through of **[ultima](https://ultimabi.uk/)** applied to a very particular case - **[Fundamental Review of the Trading Book's Standardised Approach](https://en.wikipedia.org/wiki/Fundamental_Review_of_the_Trading_Book)**. For a more general usecase refer to the general user guide. Here we will focus on FRTB only.

# Why to use Ultima

- The calculation goes as per **[FRTB SA Paper](https://www.bis.org/bcbs/publ/d457.pdf)** and aims to be fully compliant(although not certified). **[Ultima](https://ultimabi.uk/)** supports **[CRR2](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/108255)** parameter set out of the box. Switch between the two is as easy as setting `jurisdiction` to `CRR2` or `BCBS`.

- **[Ultima](https://ultimabi.uk/)** is very flexible and allows you to override any of the prescribed parameters (such as `girr_delta_rho_infl_base`) via `calc_params` argument. This essentually means that you can define your own parameter sets as per any regulatory requirements (eg non BCBS/CRR2). This also means that you can **stress test** against changes in the values of the prescribed (aka hard coded by ISDA) parameters.

-
