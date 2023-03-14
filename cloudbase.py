import subprocess

class GoogleCloudPlatform:
    def __init__(self, project_id, zone, instance_name):
        self.project_id = project_id
        self.zone = zone
        self.instance_name = instance_name

    def create_project(self):
        # Check if project exists
        existing_projects = subprocess.run(['gcloud', 'projects', 'list', '--format=value(projectId)'], capture_output=True, text=True).stdout.splitlines()
        if self.project_id in existing_projects:
            print(f'Project "{self.project_id}" already exists.')
            return

        # Create project
        subprocess.run(['gcloud', 'projects', 'create', self.project_id])
        print(f'Created project "{self.project_id}".')

        # Enable necessary APIs
        subprocess.run(['gcloud', 'services', 'enable', 'compute.googleapis.com', 'container.googleapis.com', 'cloudbuild.googleapis.com', '--project', self.project_id])

    def create_compute_instance(self):
        # Check if instance exists
        existing_instances = subprocess.run(['gcloud', 'compute', 'instances', 'list', '--format=value(name)', f'--project={self.project_id}', f'--zone={self.zone}'], capture_output=True, text=True).stdout.splitlines()
        if self.instance_name in existing_instances:
            print(f'Compute instance "{self.instance_name}" already exists.')
            return

        # Create instance
        subprocess.run(['gcloud', 'compute', 'instances', 'create', self.instance_name, f'--project={self.project_id}', f'--zone={self.zone}'])
        print(f'Created compute instance "{self.instance_name}".')

        # Configure firewall rules to allow communication with phone
        subprocess.run(['gcloud', 'compute', 'firewall-rules', 'create', 'allow-commands', '--allow', 'tcp:8080', '--source-ranges', '0.0.0.0/0', f'--project={self.project_id}', f'--target-tags={self.instance_name}', f'--description=Allow incoming commands from phone'])

    def get_instance_ip(self):
        # Get external IP address of instance
        output = subprocess.run(['gcloud', 'compute', 'instances', 'describe', self.instance_name, f'--project={self.project_id}', f'--zone={self.zone}', '--format=value(networkInterfaces[0].accessConfigs[0].natIP)'], capture_output=True, text=True)
        return output.stdout.strip()


# Initialize GCP object
	gcp = GoogleCloudPlatform(project_id='my-project', zone='us-central1-a', instance_name='my-instance')

# Create GCP project
	gcp.create_project()

# Create Compute Engine instance
	gcp.create_compute_instance()

# Get instance IP address
	instance_ip = gcp.get_instance_ip()
	print(f'Compute instance IP address: {instance_ip}')