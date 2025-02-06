import argparse
import pandas as pd
import yaml

with open("../translations.yaml", "r") as f:
    t = yaml.safe_load(f)


def compare_xlsx_columns(file_path):
    """
    Compares all rows of each column in the provided XLSX file.
    Skips columns ending with '_e'. If a column has more than one unique
    value, it prints a difference summary along with the 'short' column
    value for each row.
    """
    # Read the XLSX file into a DataFrame
    df = pd.read_excel(file_path)

    excluded_columns = ["created_date", "modified_date", "id", "short"]
    # Filter out columns that end with "_e"
    cols_to_check = [col for col in df.columns if not col.endswith(
        "_e") and not col.endswith("_comment") and col not in excluded_columns]

    # Iterate over each allowed column
    agreement_counter = 0
    disagreement_counter = 0
    for col in cols_to_check:
        unique_vals = df[col].unique()

        # If there's more than one unique value, print differences
        if len(unique_vals) > 1:
            print(f"Column '{col}' has differences!")
            print(f"{t['q'][col]['head'].strip("#").strip()}")

            # Print row-by-row differences
            for idx, row in df.iterrows():
                short_val = row["short"] if "short" in df.columns else "N/A"
                col_val = row[col]
                try:
                    choices = t['q'][col]['choices']
                    choice = [choice[1] for choice in choices if choice[0] == col_val][0]
                    print(f"  Row {idx}: short='{short_val}', choice='{choice}'")
                except:
                    print(f"  Row {idx}: short='{short_val}', {col}='{col_val}'")
            print("\n")
            disagreement_counter = disagreement_counter +1
        else:
            agreement_counter = agreement_counter +1
    print("\n")
    print(f"Total agreement: {agreement_counter} / {agreement_counter + disagreement_counter}")
    print(f"Percentage agreement: {(100 * agreement_counter) / (agreement_counter + disagreement_counter)}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Compare columns in an XLSX file across all rows."
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the XLSX file to compare."
    )

    # Parse command line arguments
    args = parser.parse_args()

    # Run the comparison
    compare_xlsx_columns(args.file_path)


if __name__ == "__main__":
    main()
