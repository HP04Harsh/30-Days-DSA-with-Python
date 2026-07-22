from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient  # type: ignore[reportMissingImports]

# Create a DefaultAzureCredential instance
credential = DefaultAzureCredential()
subscription_id = "your-subscription-id"
resource_group_name = "your-resource-group-name"

# Create a ResourceManagementClient instance
resource_client = ResourceManagementClient(credential, subscription_id)

print(f"Creating resource group '{resource_group_name}' in subscription '{subscription_id}'...")

#create the resource group
rg_client = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {
        "location": "eastus"  # Specify the desired location for the resource group
    }
)
print(f"Resource group '{resource_group_name}' created successfully.")
