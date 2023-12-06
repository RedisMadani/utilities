# Logic Apps (Preview) DevOps Guide

This repository contains a sample Logic App (preview) project, along with examples of Azure deployment and GitHub Actions for CI/CD.

## Prerequisites

Before proceeding, make sure you have the following:

- An Azure Subscription.
- Azure Storage Account or Emulator.
- Visual Studio Code (VS Code).
- Logic App Tools List.

## Local Development

To run the project locally, follow the provided [documentation](https://docs.microsoft.com/azure/logic-apps/create-stateful-stateless-workflows-visual-studio-code#run-test-and-debug-locally).

### Setting up your project in VS Code

1. Clone the repository locally and open the `github-sample` folder in VS Code.
2. Navigate to the `logic` folder and create a `local.settings.json` file with the following content:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "azureblob-connectionKey": "",
    "BLOB_CONNECTION_RUNTIMEURL": ""
  }
}
```

3. "AzureWebJobsStorage" is used for local development in Visual Studio Code, setting up a local data store for your logic app project and workflows to use in your local development environment. You can use the Azurite storage emulator for this purpose.
4. "azureblob-connectionKey" will be automatically generated in later steps. Keep it blank for now. This key is used for raw authentication credentials for the local VS Code project to access the Azure hosted API connection.
5. "BLOB_CONNECTION_RUNTIMEURL" is the endpoint URL for the blob connection hosted on Azure. This URL will be generated in the next steps.

### Setting up your API Connections

This project uses the Azure Storage Blob connection. To run this project locally, you need to generate local credentials for your connection within the `connections.json` file: "azureblob-connectionKey" and the connection runtime URL. Follow these steps:

1. Right-click on the `EventTrigger` workflow.json file and select "Yes" when prompted to use connections from Azure. Choose your Subscription and Resource Group.

2. In the workflow designer, create a new blob connection from scratch. This will generate the required local values for the connection.

3. Once the connection is created, copy the "azureblob-connectionKey" and connection runtime URL from `connections.json` to the clipboard. You can then delete the duplicate connection, as it won't be needed anymore.

4. Update your `local.settings.json` file with the copied values.

### Running your Project in VS Code

- Go to the `Run` tab and hit the play icon to run the application.
- Right-click on `workflow.json` under your `EventProcessor` folder and click `Overview`.
- Use the provided callback URL to trigger your workflow.
- Your workflow will run and add a new blob into your storage account.

## DevOps

The repository includes examples of GitHub Actions for continuous integration and deployment (CI/CD) of Logic Apps.

### ARM Deployment

The `ARM` folder contains the ARM templates required to deploy all the necessary logic app resources:

- `connectors-template.json` deploys an Azure Storage connection.
- `la-template.json` deploys the following resources:
  - Logic app.
  - App service plan.
  - Storage account.

### GitHub Actions

The `.github` folder contains examples of GitHub Actions workflows for both application deployment and infrastructure as code (IaC) deployment.

#### The Sample Pipeline Explained

The sample separates the infrastructure deployment (`IaC_deploy.yml`) and the logic app build and deploy (`logicapp_deploy.yml`) into separate pipelines.

Whenever you push a change to your ARM template folder or manually trigger the `IaC_deploy` pipeline, GitHub Actions will deploy your infrastructure. This pipeline will:

- Deploy the logic app infrastructure and API connections into their respective resource groups.
- Set access policies on the connections.
- Update the Logic Apps app settings with all connection credentials.

Once this has run successfully, it will trigger the Logic Apps build and deploy pipeline, which will build the logic app and deploy it to the newly created environment. If you make changes only to your `logic` folder, only the Logic Apps Build and Deploy pipeline will run, allowing you to avoid deploying the infrastructure on every push.

> **Note**: These are example pipelines that are relatively condensed. You are free to separate them into separate pipelines based on your specific DevOps process (e.g., separate pipelines for build, release, infrastructure deployments, etc.).

### Q & A

Q: Why do I have to recreate the operation that uses the API connection?

- A: Currently, the designer does not allow selecting or creating a new connection when a `connections.json` file does not already exist. The only way around this is to recreate the operation using the connection or create any operation using that connection inside a new workflow file.

Q: Why do I need to get a connection key to run locally?

- A: When running Logic Apps locally, the connection needs to use the 'Raw' authentication method for connections to work. When deploying to Azure, the authentication method needs to be `ManagedIdentity`.