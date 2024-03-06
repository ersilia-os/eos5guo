# ErG 2D Descriptors

The Extended Reduced Graph (ErG) approach uses the description of pharmacophore nodes to encode molecular properties, with the goal of correctly describing pharmacophoric properties, size and shape of molecules. It was benchmarked against Daylight fingerprints and outperformed them in 10 out of 11 cases. ErG descriptors are well suited for scaffold hopping approaches.

## Identifiers

* EOS model ID: `eos5guo`
* Slug: `erg-descs`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Integer`
* Output Shape: `List`
* Interpretation: Vector representing SMILES

## References

* [Publication](https://pubs.acs.org/doi/10.1021/ci050457y)
* [Source Code](https://www.rdkit.org/docs/source/rdkit.Chem.rdReducedGraphs.html)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos5guo)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5guo.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos5guo) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/ci050457y) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a BSD-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!