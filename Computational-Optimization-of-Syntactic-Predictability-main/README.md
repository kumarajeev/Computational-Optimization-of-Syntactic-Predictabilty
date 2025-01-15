# Computational Optimization of Syntactic Predictability

## Overview
This project is all about understanding how words work together in a sentence. We aim to make better predictions about word relationships using a method called Information Locality Theory. By analyzing large text collections, we look for patterns in how words connect. Our ultimate goal is to create smart algorithms that can write sentences with perfect word flow, helping computers understand and process human language more naturally.

## Methodology

1. **Data Preparation**:
    - Read the English corpus from the SUD directory.
    - Parsed the corpus using the `conllu` library.

2. **Graph Construction**:
    - Created nodes for each word in the sentences and represented them in a directed graph using the `NetworkX` library.
    - Identified heads and dependents and formed edges between them.

3. **Calculating Predictability Measures**:
    - Applied measures from the `measures.py` file to calculate Dependency Length (DL) and Intervener Complexity (IC), represented by dependency depth.
    - Stored this data, including direction of the edge, sentence ID, and the identity of each head-dependent pair, in a separate file.

4. **Pointwise Mutual Information (PMI)**:
    - Calculated PMI between word pairs in the corpus using the `collect_pmi.py` file, which uses Information Locality Theory.
    - Combined PMI results with other predictability measures (DL and IC) in separate files.
    - In the `DL_vs_PMI.ipynb` file, calculated DL and PMI for each head and dependent in the corpus, plotted the results, and observed the trends.
    - Noted a correlation of -0.139 between DL and PMI after averaging PMIs with the same DL values.
    - Similarly, analyzed trends in the `DL_vs_IC.ipynb` file.

5. **Sentence Generation Algorithms**:
    - Designed algorithms to generate sentences while maintaining consistent PMIs between word pairs.
    - Calculated DL using the established trends and minimized DL error using RMS or cross-entropy functions.
    - The raw code for this process is available in the `Random_conditions_DL_based_RNAs.py` and `treegen.py` files.

## Results
- **DL vs PMI**: Found a correlation of -0.139 between Dependency Length (DL) and Pointwise Mutual Information (PMI).
- **DL vs IC**: Determined a strong correlation of 0.99 between Intervener Complexity (IC) and Dependency Length (DL), indicating that DL significantly increases with IC.

## Future Work
- Continue refining sentence generation algorithms to maintain PMI consistency and minimize DL error using RMS and cross-entropy minimization.
- Explore additional methods to enhance syntactic predictability analysis.
