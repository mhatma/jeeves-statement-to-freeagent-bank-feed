# Jeeves Statement CSV to FreeAgent Bank Feed CSV

Basic Python script to convert **Jeeves** [https://www.tryjeeves.com] statement CSVs into files that can be processed as **FreeAgent** [https://freeagent.com] bank feeds.

Run: 
`python JeevesToFA.py`

Enter the file name/path of the CSV to process (for example **jeeves.csv**).
This will process **jeeves.csv** and output results to **output.csv**.
It will also add a negative sign to any rows from the input file that have a PaymentType of "card". This means that settlements and cashback will remain as positive numbers.
Additionally it will output the "description" as the "MerchantName [UserName]" to identify the source of a charge. 


Please note: This script does not check for the existence of either the input or output CSVs.
