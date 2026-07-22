from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Create a DefaultAzureCredential instance
credential = DefaultAzureCredential()
subscription_id = "your-subscription-id" 
resource_group_name = "your-resource-group-name"
vm_name = "your-vm-name"
compute_client = ComputeManagementClient(credential, subscription_id)

run_command_parameters = {
    'command_id': 'RunShellScript',
    'script': ['echo Hello, World!']
}

poller = compute_client.virtual_machines.begin_run_command(
    resource_group_name,
    vm_name,
    run_command_parameters
)

result = poller.result()
for output in result.value:
    print(output.message)