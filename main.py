import argparse
import os
import requests

def fetch_all_datasource_ids():
    return [1, 2, 3, 4, 5]

def get_owner_ids_by_ds_id(ds_id):
    return [100, 101]

def get_ds_owner_email_address_by_user_id(user_id):
    if user_id == 100:
        return 'nicholas.wilson@alation.com'
    if user_id == 101:
        return 'matt.sullivan@alation.com'

def get_ds_owner_email_addresses_by_ds_id(ds_id):
    ds_owner_ids = get_owner_ids_by_ds_id(ds_id)
    ds_owner_email_addresses = []
    for user_id in ds_owner_ids:   
        ds_owner_email_address = get_ds_owner_email_address_by_user_id(user_id)
        ds_owner_email_addresses.append(ds_owner_email_address)
    return ds_owner_email_addresses

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
        ds_owner_email_addresses = get_ds_owner_email_addresses_by_ds_id(ds_id)
        print(f'Will email owners: {", ".join(ds_owner_email_addresses)}')

if __name__ == "__main__":
    main()