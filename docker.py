import docker

# Create a Docker client
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Start a container
container = client.containers.run("image_name", detach=True)
print(f"Started container with ID: {container.id}")