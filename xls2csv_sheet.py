import pandas as pd

excel_files = ["IN718_final.xlsx", "Ti6Al4V_final.xlsx", "316_final.xlsx"]

for excel_file in excel_files:
    excel_data = pd.read_excel(excel_file, sheet_name=None)

    for sheet_name, sheet_data in excel_data.items():
        #print(f"Sheet Name: {sheet_name}")
        #print(sheet_data)  # This will print the data for each sheet
        if sheet_name.startswith("IN_") or sheet_name.startswith("Ti_") or sheet_name.startswith("St_"):
            csv_file = sheet_name + '.csv'
            sheet_data.to_csv(csv_file, index=False)
            
            # Create a list to store the lines
            lines_to_keep = []

            # Open the CSV file in read mode
            with open(csv_file, 'r') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    #if line_number != 3 and line_number != 15:
                    newString = line.replace(',','')
                    if len(newString) > 3:
                        #if any(char.isnumeric() for char in line):
                        lines_to_keep.append(line)

            # Reopen the same CSV file in write mode (this will overwrite its contents)
            with open(csv_file, 'w') as file:
                file.writelines(lines_to_keep)
