import csv
import functions_framework
from google.cloud import storage

@functions_framework.http
def key_value_matching(request):
    """
    Returns the value of a given key in a table.
    The table is stored in a bucket on gcp.
    """

    request_json = request.get_json(silent=True)
    request_args = request.args

    storage_client = storage.Client()
    bucket = storage_client.get_bucket("ds-ai-assignment-bucket")

    # Load csv data
    blob = bucket.blob("table.csv")
    blob.download_to_filename("table.csv")
    data = {}
    with open("table.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                data[row[0]] = row[1]

    # Find matching value to key in the request
    key = request_args.get('key') if request_args else request_json.get('key')
    value = data.get(key, 'Key not found')
    
    # Trailing "\n" to avoid "%" at line end in unix-based terminals
    return f"{value}\n"