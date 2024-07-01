import logging
import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.billing import BillingManagementClient
from dotenv import load_dotenv
from resource_graph import run_azure_rg_query
from common_util import get_six_months_of_dates


def list_billing_in_azure(subscription_id:str):
    """
    List azure resources per subscription
    :return:
    """
    credential = DefaultAzureCredential()
    billing_client = BillingManagementClient(credential=credential, subscription_id=subscription_id)
    # invoices = billing_client.invoices.list_by_billing_subscription()
    date_ranges = get_six_months_of_dates()
    for i in date_ranges:
        period_start_date = i[0]
        period_end_date = i[1]
        invoices = billing_client.invoices.list_by_billing_subscription(period_start_date=period_start_date, period_end_date=period_end_date)
        print(invoices)
        for invoice in invoices:
            print(f"Invoice ID: {invoice.id}")
            print(f"Invoice Amount: {invoice.amount_due}")
            print(f"Billing Period Start Date: {invoice.billing_period_start_date}")
            print(f"Billing Period End Date: {invoice.billing_period_end_date}")
            print(f"Invoice URL: {invoice.invoice_url}")
            print("----")



def main():
    """test code"""
    load_dotenv()
    parser = argparse.ArgumentParser('Azure resources listing..')
    parser.add_argument("--subscription_name", help='Azure subscription name', required=True, type=str)

    args = parser.parse_args()
    subscription_name = args.subscription_name
    logging.info("Proccess started......")
    subscription_id = run_azure_rg_query(subscription_name=subscription_name)
    list_resources = list_billing_in_azure(subscription_id=subscription_id)
    # print(f'Total number of resources in Azure subscription - {subscription_name} is : {len(list_resources)}')


if __name__ == "__main__":
    main()