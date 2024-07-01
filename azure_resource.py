import os
import logging
import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv
from resource_graph import run_azure_rg_query
def list_resources_in_azure(subscription_id:str):
    """
    List azure resources per subscription
    :return:
    """
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential=credential, subscription_id=subscription_id)

    resources = resource_client.resources.list()
    resource_details = []
    for resource in resources:
        resource_dict = {}
        print(resource)
        resource_dict['name'] = resource.name
        resource_dict['resource_id'] = resource.id
        resource_dict['resource_location'] = resource.location
        resource_dict['resource_tag'] = resource.tags
        resource_dict['sku'] = resource.sku
        resource_dict['resource_type'] = resource.type
        resource_details.append(resource_dict)

    return resource_details




def main():
    """test code"""
    load_dotenv()
    parser = argparse.ArgumentParser('Azure resources listing..')
    parser.add_argument("--subscription_name", help='Azure subscription name', required=True, type=str)

    args = parser.parse_args()
    subscription_name = args.subscription_name
    logging.info("Proccess started......")
    subscription_id = run_azure_rg_query(subscription_name=subscription_name)
    list_resources = list_resources_in_azure(subscription_id=subscription_id)
    print(f'Total number of resources in Azure subscription - {subscription_name} is : {len(list_resources)}')


if __name__ == "__main__":
    main()