"""Frozen lexical rules from the previous institutional run."""
import re

PATTERNS = {'am': 'additive manufactur\\w*|powder bed fusion|selective laser melting|directed energy deposition|laser metal deposition|laser deposition|\\b[sl]pbf\\b|\\b[sl]lm\\b|\\bded\\b', 'metal': 'metal\\w*|alloy\\w*|titanium|\\bti[- ]?6al[- ]?4v\\b|inconel|nickel|\\bsteel\\b', 'learning': 'machine learning|deep learning|neural network\\w*|data[- ]driven|random forest|gaussian process|support vector|transformer|\\bgnns?\\b|\\bsvr\\b|large language model', 'physical_model': 'physical model|physics|thermodynamic\\w*|solidification|finite element|numerical simulat\\w*|mechanistic|\\bcalphad\\b|lattice boltzmann', 'microstructure': 'microstructur\\w*|grain\\w*|crystallographic|\\bphase\\w*', 'properties': 'mechanical propert\\w*|tensile|fatigue|strength|toughness|residual stress|deformation|porosity', 'experiment': 'experiment\\w*|characterization|measurement\\w*|\\bebsd\\b|microscop\\w*', 'ic': 'circuit\\w*|chip|semiconductor|\\bvlsi\\b|\\bcmos\\b|\\basics?\\b|layout|lithograph\\w*', 'eda': 'electronic design automation|netlist|physical design|placement|prerouting|pre-routing|timing|logic synthesis|hotspot|mask optimization|lithograph\\w*', 'timing': 'timing|delay|\\bpvt\\b|standard cell|cell librar\\w*', 'layout': 'layout|placement|routing|hotspot|mask|lithograph\\w*', 'data': 'dataset\\w*|data set\\w*|benchmark\\w*|training data|data preparation|opencores|netlist\\w*', 'validation': 'verif\\w*|validat\\w*|experimental|simulation|design flow|benchmark\\w*'}

RX = {k: re.compile(v, re.I) for k, v in PATTERNS.items()}

def tokens(text):
    words = re.findall('[a-z][a-z0-9]*', text.lower())
    roots = [('manufactur', 'manufacture'), ('predict', 'predict'), ('model', 'model'), ('optimiz', 'optimize'), ('optimis', 'optimize'), ('simulat', 'simulate'), ('mechanic', 'mechanical'), ('experiment', 'experiment'), ('validat', 'validate')]
    result = []
    for word in words:
        for stem, replacement in roots:
            if word.startswith(stem):
                word = replacement
                break
        else:
            if len(word) > 4 and word.endswith('s'):
                word = word[:-1]
        result.append(word)
    return result
