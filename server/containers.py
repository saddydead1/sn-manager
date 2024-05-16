import docker

client = docker.from_env()


def containers_list() -> list:
    result = list()

    for i in client.containers.list(all=True):
        result.append(client.containers.get(i.id).attrs['Config']['Image'])

    return result

