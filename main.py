import argparse
import os
import requests
import smtplib
from email.message import EmailMessage

def fetch_all_datasource_ids():
    return [1, 2, 3]

def get_last_mde_job_status_by_ds_id(ds_id):
    if ds_id == 1:
        return 'FAILED'
    if ds_id == 2:
        return 'SUCCESSFUL'
    if ds_id == 3:
        return 'SUCCESSFUL'

def get_ds_owner_ids_by_ds_id(ds_id):
    return [100, 101]

def get_ds_owner_email_address_by_user_id(user_id):
    if user_id == 100:
        return 'nicholas.wilson@alation.com'
    if user_id == 101:
        return 'matt.sullivan@alation.com'

def get_ds_owner_email_addresses_by_ds_id(ds_id):
    ds_owner_ids = get_ds_owner_ids_by_ds_id(ds_id)
    ds_owner_email_addresses = []
    for user_id in ds_owner_ids:   
        ds_owner_email_address = get_ds_owner_email_address_by_user_id(user_id)
        ds_owner_email_addresses.append(ds_owner_email_address)
    return ds_owner_email_addresses

def send_email(recipients, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "your_email@example.com"
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.send_message(msg)

def notify_ds_admins_by_email(ds_id, ds_owner_email_addresses):
    subject = f'Metadata Extraction (MDE) Job Failed for Data Source ID: {ds_id}'
    body = f'Metadata Extraction (MDE) Job Failed for Data Source ID: {ds_id}'
    send_email(ds_owner_email_addresses, subject, body)

def main():
    # Create arg parser
    parser = argparse.ArgumentParser(description='Script to fetch glossary terms by glossary ID.')

    # Add arguments
    parser.add_argument(
        '--token',
        type=str,
        default=os.environ.get('ALATION_TOKEN', None),
        required=os.environ.get('ALATION_TOKEN', None) is None,
        help='Alation API Token'
    )

    parser.add_argument(
        '--base_url',
        type=str,
        default=os.environ.get('ALATION_BASE_URL', None),
        required=os.environ.get('ALATION_BASE_URL', None) is None,
        help='Base URL for your Alation instance (i.e., "alation.mydomain.com")'
    )

    args = parser.parse_args()

    api_token = args.token
    base_url = args.base_url

    # 1. Get all datasource IDs
    all_datasource_ids = fetch_all_datasource_ids()
    for ds_id in all_datasource_ids:
        print(f'Checking status of MDE for ds_id: {ds_id}')

        # 2. Get status of last MDE job
        last_mde_job_status = get_last_mde_job_status_by_ds_id(ds_id)
        
        if last_mde_job_status == "FAILED":
            # 3. If applicable, email datasource admins
            ds_owner_email_addresses = get_ds_owner_email_addresses_by_ds_id(ds_id)
            print(f'Will email the following datasource admins: {", ".join(ds_owner_email_addresses)}')
            notify_ds_admins_by_email(ds_owner_email_addresses)


if __name__ == "__main__":
    main()