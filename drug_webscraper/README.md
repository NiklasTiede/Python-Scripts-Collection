
Task: Collecting InChI strings of all FDA-approved drugs (1985 - 2019).

1. download list of approved-drugs, preprocess data
2. retrieve InChI of each drug by its proprietary name (scrape cactus.nci.nih.gov API) using `trivial_to_inchi.py` script
3. InChI's not representing pharmaceutical active ingredients (salts/very small molecules) were filtered out

Result: for 648 out of 1633 drugs a valid InChI could be retrieved (39.7 %).
