FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

RUN pip install rdkit==2023.9.5

WORKDIR /repo
COPY . /repo
