
# 🛠️ Terraform CLI Command Reference

## Core Workflow Commands

| Command   | Description |
|-----------|-------------|
| `init`    | Initialize a working directory with Terraform configuration files. |
| `validate`| Check whether the configuration is syntactically valid. |
| `plan`    | Show the changes Terraform will make to reach the desired state. |
| `apply`   | Apply the changes required to reach the desired state. |
| `destroy` | Destroy the Terraform-managed infrastructure. |

## Configuration & Inspection

| Command     | Description |
|-------------|-------------|
| `console`   | Interactive console for evaluating Terraform expressions. |
| `fmt`       | Format configuration files to canonical style. |
| `output`    | Show output values from the root module. |
| `providers` | Show providers required for the configuration. |
| `show`      | Show human-readable output of Terraform state or plan. |
| `version`   | Show Terraform version. |
| `graph`     | Generate a DOT-format graph of the resource dependencies. |

## Resource & State Management

| Command       | Description |
|---------------|-------------|
| `import`      | Import existing infrastructure into Terraform. |
| `refresh`     | Update the state file with real infrastructure. *(Deprecated in favor of `apply`)* |
| `taint`       | Mark a resource for recreation during the next apply. |
| `untaint`     | Remove the taint state from a resource. |
| `state`       | Advanced state management (list, mv, pull, push, rm, show). |
| `force-unlock`| Manually unlock the state. |

## Workspace Management

| Command     | Description |
|-------------|-------------|
| `workspace` | Manage multiple workspaces (list, new, select, delete, show). |

## Cloud & Credential Management

| Command | Description |
|--------|-------------|
| `login` | Authenticate to Terraform Cloud or other remote backends. |
| `logout`| Remove credentials for Terraform Cloud. |

## Testing (Terraform 1.6+)

| Command | Description |
|---------|-------------|
| `test`  | Run automated tests against Terraform configurations. |

## Modules

| Command   | Description |
|-----------|-------------|
| `get`     | Download and update modules mentioned in the configuration. |
| `metadata`| Show module or provider metadata. |

## Miscellaneous

| Command | Description |
|---------|-------------|
| `help`  | Show help for any Terraform command. |
