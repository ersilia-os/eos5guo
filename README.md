# ErG 2D Descriptors

The Extended Reduced Graph (ErG) approach uses the description of pharmacophore nodes to encode molecular properties, with the goal of correctly describing pharmacophoric properties, size and shape of molecules. It was benchmarked against Daylight fingerprints and outperformed them in 10 out of 11 cases. ErG descriptors are well suited for scaffold hopping approaches.

This model was incorporated on 2024-03-06.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5guo`
- **Slug:** `erg-fingerprints`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Descriptor`, `Fingerprint`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `315`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representing ErG fingerprint values

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_000 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 0 |
| dim_001 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 1 |
| dim_002 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 2 |
| dim_003 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 3 |
| dim_004 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 4 |
| dim_005 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 5 |
| dim_006 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 6 |
| dim_007 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 7 |
| dim_008 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 8 |
| dim_009 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 9 |

_10 of 315 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5guo](https://hub.docker.com/r/ersiliaos/eos5guo)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5guo.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5guo.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `495`
- **Image Size (Mb):** `429.94`


### References
- **Source Code**: [https://www.rdkit.org/docs/source/rdkit.Chem.rdReducedGraphs.html](https://www.rdkit.org/docs/source/rdkit.Chem.rdReducedGraphs.html)
- **Publication**: [https://pubs.acs.org/doi/10.1021/ci050457y](https://pubs.acs.org/doi/10.1021/ci050457y)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2005`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5guo
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5guo
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
