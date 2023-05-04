# Stardate Calculator with Century Prefix

This Stardate Calculator is a Python script that calculates the current stardate based on a custom reference date and conversion factor. The stardate format is inspired by Star Trek: The Next Generation (TNG) and includes the current century as a prefix. The resulting format is "CCYYYYYY.Z", where "CC" represents the current century, "YYYYYY" represents the progressive count of stardate units, and "Z" is the decimal portion.

## Usage

To use the Stardate Calculator with Century Prefix, run the provided Python script (`stardate_calculator.py`) in a Python environment. The script will output the current stardate, including the century prefix, based on the custom reference date and conversion factor used.

```bash
python stardate.py
```

## Customization

The script uses a reference date of January 1, 0 (1 BCE) and a conversion factor of 2.7378 stardate units per Earth day. You can modify these values within the script to create your own personalized stardate system.

## Interpretation

The stardate format "CCYYYYYY.Z" consists of three parts:

1. "CC": A two-digit integer representing the current century (e.g., 21 for the 21st century).
2. "YYYYYY": A six-digit integer part representing the progressive count of stardate units since the reference date.
3. ".Z": A decimal portion with one decimal place, representing a fraction of a day (ranging from 0 to 0.9).

The stardate number increases as time progresses, with the integer part increasing by one for every full day and the decimal part representing the fraction of a day. This format is inspired by TNG stardates but does not adhere to canonical Star Trek stardate calculations. The stardate is calculated based on the custom reference date and conversion factor used in the script (2.7378 stardate units per Earth day).