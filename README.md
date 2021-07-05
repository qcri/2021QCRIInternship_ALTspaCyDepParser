# 2021 QCRI Internship spaCy Dependency Parser


#
# Collaborators:

  -  Hadir Teryak
  -  Rohit Singh


# Data

 - Universal Dependecy data for Arabic and English


# Scripts/Commands:
 - python -m spacy convert ar_nyuad-ud-dev.merged.conllu . 
 - python -m spacy convert ar_nyuad-ud-train.conllu . 
 - python -m spacy train config.cfg --gpu-id 0 --output ./output --paths.train ar_nyuad-ud-train.spacy --paths.dev ar_nyuad-ud-dev.spacy
 - python -m spacy train config.cfg --gpu-id 0 --output ./output --paths.train ar_nyuad-ud-train.spacy --paths.dev ar_nyuad-ud-dev.spacy
 - python -m spacy train config.cfg --gpu-id 0 --output ./output --paths.train ar_nyuad-ud-train.spacy --paths.dev ar_nyuad-ud-dev.merged.spacy
 - python -m spacy evaluate ./output/model-best ar_nyuad-ud-test.merged.spacy 
 - python -m spacy convert ar_nyuad-ud-dev.merged-Final.conllu . 
 - python -m spacy convert ar_nyuad-ud-train-Final.conllu . 
 - python -m spacy convert ar_pud-ud-test.conllu . 
 - python -m spacy evaluate ./outputFinal/model-best ar_pud-ud-test.spacy 
 - python -m spacy evaluate ./outputFinal/model-best ar_padt-ud-test.spacy 
 - python -m spacy convert ar_pud-ud-testF.conllu . 
 - python -m spacy convert ar_padt-ud-testF.conllu . 
 - python -m spacy convert ar_nyuad-ud-test-FinalF.conllu . 
 - python -m spacy evaluate ./output/model-best ar_padt-ud-testF.spacy 
 - python -m spacy evaluate ./output/model-best ar_pud-ud-testF.spacy 
 - python -m spacy evaluate ./output/model-best ar_nyuad-ud-test-FinalF.spacy 
  







