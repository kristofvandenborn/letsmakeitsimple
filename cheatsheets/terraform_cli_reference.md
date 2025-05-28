# Terraform CLI Commands and Arguments Explained

This document provides a detailed reference of commonly used Terraform CLI commands, including their arguments and usage examples.

---

## terraform init

Initializes a Terraform configuration directory.

**Arguments:**
- `-backend=true|false`: Configure the backend.
- `-backend-config=PATH`: Supply a backend configuration.
- `-get=true|false`: Download modules.
- `-input=true|false`: Ask for input if necessary.
- `-lock=true|false`: Lock the state file.
- `-lock-timeout=0s`: Duration to retry a state lock.
- `-upgrade`: Upgrade modules and plugins.

**Example:**
```bash
terraform init -backend=true -upgrade
```

---

## terraform plan

Generates an execution plan showing what Terraform will do.

**Arguments:**
- `-var 'key=value'`: Set a variable.
- `-var-file=FILENAME`: Load variable values from file.
- `-out=FILENAME`: Save the plan to a file.
- `-input=false`: Disable interactive input.
- `-refresh=true|false`: Update state prior to planning.
- `-target=RESOURCE`: Focus on specific resources.

**Example:**
```bash
terraform plan -var 'region=us-west-2' -out=tfplan
```

---

## terraform apply

Applies the changes required to reach the desired state.

**Arguments:**
- `FILENAME`: Apply a saved plan file.
- `-auto-approve`: Skip interactive approval.
- `-input=false`: Disable input.
- `-lock=true|false`: Lock the state file.
- `-var` and `-var-file`: Same as in plan.

**Example:**
```bash
terraform apply -auto-approve
```

---

## terraform destroy

Destroys all managed infrastructure.

**Arguments:**
- `-auto-approve`: Skip confirmation.
- `-target=RESOURCE`: Destroy specific resource.
- `-var`, `-var-file`, `-input`, `-lock`: Same as apply.

**Example:**
```bash
terraform destroy -auto-approve
```

---

## terraform validate

Validates the configuration files.

**Arguments:**
- `-json`: Output in JSON format.
- `PATH`: Path to configuration directory.

**Example:**
```bash
terraform validate
```

---

## terraform fmt

Formats Terraform configuration files.

**Arguments:**
- `-recursive`: Format all files in subdirectories.
- `-check`: Check if files are formatted.
- `-diff`: Show diffs.
- `-list=true|false`: Show changed files.

**Example:**
```bash
terraform fmt -recursive
```

---

## terraform state

Advanced manipulation of the Terraform state.

**Subcommands:**
- `list`: List resources.
- `mv`: Move items.
- `pull`: Pull current state.
- `push`: Push local state.
- `rm`: Remove resource from state.
- `show`: Show a resource in state.

**Example:**
```bash
terraform state list
terraform state rm aws_instance.example
```

---

## terraform output

Reads outputs from the state file.

**Arguments:**
- `-json`: Output in JSON format.

**Example:**
```bash
terraform output
terraform output -json
```

---

## terraform import

Imports existing infrastructure into Terraform.

**Arguments:**
- `RESOURCE_NAME ID`: Resource address and ID.

**Example:**
```bash
terraform import aws_instance.example i-1234567890abcdef0
```

---

## terraform taint / untaint

Marks or unmarks a resource for recreation.

**Example:**
```bash
terraform taint aws_instance.example
terraform untaint aws_instance.example
```

---

## terraform console

Interactive console for evaluating expressions.

**Example:**
```bash
terraform console
> var.region
```

---

## terraform graph

Generates a graph of the dependency.

**Arguments:**
- `-draw-cycles`: Show cycles.
- `-type=plan|apply`: Type of graph.

**Example:**
```bash
terraform graph | dot -Tpng > graph.png
```

---

## terraform login / logout

Authenticate with Terraform Cloud or Enterprise.

**Example:**
```bash
terraform login
terraform logout
```

---

## terraform providers

Shows providers used in the configuration.

**Example:**
```bash
terraform providers
```

---

## terraform version

Shows the Terraform version.

**Example:**
```bash
terraform version
```

---

## terraform -help

Shows help for Terraform CLI or a specific command.

**Example:**
```bash
terraform -help
terraform plan -help
```
