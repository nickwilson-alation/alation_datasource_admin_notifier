# Alation Datasource Admin Notifier
Notifies relevant Alation data source admins when corresponding MDE jobs fail.
## Overview

This script checks the last Metadata Extraction (MDE) job status for all data sources in an Alation instance. If the last job failed, the script sends a notification to the admins of the respective data source.

## Prerequisites

- Python 3.x
- Required Python packages: `argparse`, `requests`

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed.
3. Install the required Python packages if not already installed:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Environment Variables

The script uses the following environment variables for configuration:

- `ALATION_TOKEN`: Your Alation API token.
- `ALATION_BASE_URL`: The base URL of your Alation instance (e.g., `alation.mydomain.com`).

You can set these environment variables in your terminal:

```sh
export ALATION_TOKEN='your_alation_token'
export ALATION_BASE_URL='alation.mydomain.com'
```

### Command-Line Arguments

The script also accepts the following command-line arguments:

- `--token`: Alation API token (overrides `ALATION_TOKEN` environment variable).
- `--base_url`: Base URL for your Alation instance (overrides `ALATION_BASE_URL` environment variable).

### Running the Script

To run the script, use the following command:

```sh
python script_name.py
```

You can also pass the command-line arguments directly:

```sh
python script_name.py --token your_alation_token --base_url alation.mydomain.com
```

### Script Workflow
1. **Fetch All Data Sources**: The script fetches all data sources from the Alation instance.
2. **Check Last MDE Job Status**: For each data source, it checks the status of the last MDE job.
3. **Send Notification**: If the last MDE job failed, the script sends an email notification to the admins of the respective data source.

## Disclaimer

This project and all the code contained within this repository is provided "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the project is with you.

The author, including Alation, shall not be responsible for any damages whatsoever, including direct, indirect, special, incidental, or consequential damages, arising out of or in connection with the use or performance of this project, even if advised of the possibility of such damages.

Please understand that this project is provided for educational and informational purposes only. Always ensure proper testing, validation and backup before implementing any code or program in a production environment.

By using this project, you accept full responsibility for any and all risks associated with its usage.