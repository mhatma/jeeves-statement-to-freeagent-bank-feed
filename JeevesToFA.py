# Jeeves CSV to FreeAgent basic "bank feed" CSV.
# Converts Jeeves statements to the format described here:
# https://support.freeagent.com/hc/en-gb/articles/115001222564
# MW <matt@portforward.uk> 

# Import some helpful libraries
from datetime import datetime;
import csv;

# TODO: 
# Here - check file for errors before continuing
filename = input("Enter filename to process: ");
output_filename = "output.csv";

# FreeAgent expected columns
# date - format dd/mm/yyyy
# amount - formatted as a float with 2 decimal places
# description - string 
column_map = {
    'date':         'PostedDate',
    'amount':       'TransactionAmount',
    'description':  'MerchantName',
    'user':         'UserName',
    'payment_type': 'PaymentType',
};

# Convert date to the format FA expects
def convDate(val):
    return datetime.fromisoformat(val).strftime('%d/%m/%Y');
    
# Get the appropriate value from array of values, using the FreeAgent field names as reference
def getCol(colName, vals):
    global column_map, headers;
    return vals[headers.index(column_map[colName])];

# Read through the Jeeves CSV
with open(filename, newline='') as JeevesCSV:
    reader = csv.reader(JeevesCSV);

    # Open our new CSV for writing
    writer = csv.writer(open(output_filename, 'w', newline='\n'));

    # Use first line as headers
    headers = next(reader);

    # Loop through rest of the rows
    i = 0;
    for row in reader:
        # Write generated array to file.
        writer.writerow([
            convDate(getCol("date", row)), 
            # Add a negative sign if the payment type is "cards"
            # To keep settlements + cashback as positive numbers
                ('','-')[getCol("payment_type", row) == 'cards'] + 
                getCol("amount", row),
            # Append the "user" that posted the transaction to the description.
            getCol("description", row) + ' [' + getCol('user', row) + ']'
        ]);
        i += 1;

print("Done. Output", i, "rows to", output_filename);