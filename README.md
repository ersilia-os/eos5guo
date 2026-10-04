# ErG 2D Descriptors

Reduces a molecule to 315 numbers describing pharmacophoric features and the topological distances between them, deliberately discarding atomic detail. Stiefl and colleagues at Eli Lilly built ErG for scaffold hopping: by representing only which functional groups are present and how far apart they sit, two molecules built on unrelated skeletons can register as similar if they display the same features in the same arrangement. The abstraction that makes this possible also means fine structural differences are invisible.

This model was incorporated on 2024-03-06.Last packaged on 2026-08-31.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5guo`
- **Slug:** `erg-fingerprints`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Fingerprint`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `315`
- **Output Consistency:** `Fixed`
- **Interpretation:** 315 descriptors encoding pharmacophore features and their topological separations.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 0 |
| feat_001 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 1 |
| feat_002 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 2 |
| feat_003 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 3 |
| feat_004 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 4 |
| feat_005 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 5 |
| feat_006 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 6 |
| feat_007 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 7 |
| feat_008 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 8 |
| feat_009 | float |  | Extended reduced graph (ErG) pharmacophore descriptor bit index 9 |

_10 of 315 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5guo](https://hub.docker.com/r/ersiliaos/eos5guo)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5guo.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5guo.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `501`
- **Image Size (Mb):** `546.58`

**Computational Performance (seconds):**
- 10 inputs: `30.26`
- 100 inputs: `20.07`
- 10000 inputs: `29.74`

### References
- **Source Code**: [https://www.rdkit.org/docs/source/rdkit.Chem.rdReducedGraphs.html](https://www.rdkit.org/docs/source/rdkit.Chem.rdReducedGraphs.html)
- **Publication**: [https://doi.org/10.1021/ci050457y](https://doi.org/10.1021/ci050457y)
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
