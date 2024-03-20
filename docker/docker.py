# ==================================================
# IMPORTS
# ==================================================
import os


# ==================================================
# CLASS
# ==================================================
class Docker:
    
    @classmethod
    def version(
            cls,
            options: str = ""
    ) -> None:
        
        os.system(command=f"docker --version {options}".strip())
    
    
    class Builder:
        
        @classmethod
        def build(
                cls,
                options: str = "",
                path_or_url: str = ""
        ) -> None:
            
            os.system(command=f"docker image build {options} {path_or_url}".strip())
        
        
        @classmethod
        def prune(cls) -> None:
            
            os.system(command="docker build prune")
    
    
    class BuildX:
        
        @classmethod
        def bake(
                cls,
                options: str = "",
                target: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx bake {options} {target}".strip())
        
        @classmethod
        def build(
                cls,
                options: str = "",
                path_or_url: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx build {options} {path_or_url}".strip())
        
        @classmethod
        def create(
                cls,
                options: str = "",
                context_or_endpoint: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx create {options} {context_or_endpoint}".strip())
        
        @classmethod
        def debug(cls) -> None:
            
            os.system(command="docker buildx debug")
        
        @classmethod
        def debug_build(
                cls,
                options: str = "",
                path_or_url: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx debug build {options} {path_or_url}".strip())
        
        @classmethod
        def du(cls) -> None:
            
            os.system(command="docker buildx du")
        
        @classmethod
        def imagetools(cls) -> None:
            
            os.system(command="docker buildx imagetools")
        
        @classmethod
        def imagetools_create(
                cls,
                options: str = "",
                source: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx imagetools create {options} {source}".strip())
        
        @classmethod
        def imagetools_inspect(
                cls,
                options: str = "",
                name: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx imagetools inspect {options} {name}".strip())
        
        @classmethod
        def inspect(
                cls,
                name: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx inspect {name}".strip())
        
        @classmethod
        def ls(cls) -> None:
            
            os.system(command="docker buildx ls")
        
        @classmethod
        def prune(cls) -> None:
            
            os.system(command="docker buildx prune")
        
        @classmethod
        def rm(
                cls,
                options: str = "",
                name: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx rm {options} {name}".strip())
        
        @classmethod
        def stop(
            cls,
            name: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx stop {name}".strip())
        
        @classmethod
        def use(
            cls,
            options: str = "",
            name: str = ""
        ) -> None:
            
            os.system(command=f"docker buildx use {options} {name}".strip())
        
        @classmethod
        def version(cls) -> None:
            
            os.system(command="docker buildx version")
    
    
    class Checkpoint:
        
        @classmethod
        def create(
                cls,
                options: str = "",
                container: str = "",
                checkpoint: str = ""
        ) -> None:
            
            os.system(command=f"docker checkpoint create {options} {container} {checkpoint}".strip())
        
        @classmethod
        def ls(
                cls,
                options: str = "",
                container: str = "",
        ) -> None:
            
            os.system(command=f"docker checkpoint ls {options} {container}".strip())
        
        @classmethod
        def rm(
                cls,
                options: str = "",
                container: str = "",
                checkpoint: str = ""
        ) -> None:
            
            os.system(command=f"docker checkpoint rm {options} {container} {checkpoint}".strip())
    
    
    class Compose:
        pass
    
    
    class Config:
        pass
    
    
    class Container:
        
        @classmethod
        def attach(cls) -> None:
            pass
        
        @classmethod
        def commit(
                cls,
                container: str,
                repository: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker container commit {options} {container} {repository}".strip())
        
        @classmethod
        def cp(cls) -> None:
            pass
        
        @classmethod
        def create(cls) -> None:
            pass
        
        @classmethod
        def diff(cls) -> None:
            pass
        
        @classmethod
        def _exec(cls) -> None:
            pass
        
        @classmethod
        def export(cls) -> None:
            pass
        
        @classmethod
        def inspect(cls) -> None:
            pass
        
        @classmethod
        def kill(cls) -> None:
            pass
        
        @classmethod
        def logs(cls) -> None:
            pass
        
        @classmethod
        def ls(
                cls,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker container list {options}".strip())
        
        @classmethod
        def pause(cls) -> None:
            pass
        
        @classmethod
        def port(cls) -> None:
            pass
        
        @classmethod
        def prune(cls) -> None:
            pass
        
        @classmethod
        def rename(cls) -> None:
            pass
        
        @classmethod
        def restart(cls) -> None:
            pass
        
        @classmethod
        def rm(
                cls,
                container: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker container rm {options} {container}".strip())
        
        @classmethod
        def run(
                cls,
                image: str,
                options: str = "",
                platform: str = "linux/amd64",
                command: str = "",
                arg: str = ""
        ) -> None:
            
            os.system(command=f"docker container run {options} --platform={platform} {image} {command} {arg}".strip())
        
        @classmethod
        def start(
                cls,
                container: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker container start {options} {container}".strip())
        
        @classmethod
        def stats(cls) -> None:
            pass
        
        @classmethod
        def stop(
                cls,
                container: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker container stop {options} {container}".strip())
        
        @classmethod
        def top(cls) -> None:
            pass
        
        @classmethod
        def unpause(cls) -> None:
            pass
        
        @classmethod
        def update(cls) -> None:
            pass
        
        @classmethod
        def wait(cls) -> None:
            pass
    
    
    class Context:
        pass
    
    
    class Image:
        
        @classmethod
        def build(cls) -> None:
            pass
        
        @classmethod
        def history(cls) -> None:
            pass
        
        @classmethod
        def _import(cls) -> None:
            pass
        
        @classmethod
        def inspect(cls) -> None:
            pass
        
        @classmethod
        def load(cls) -> None:
            pass
        
        @classmethod
        def ls(
                cls,
                options: str = "",
                repository: str = ""
        ) -> None:
            
            os.system(command=f"docker image ls {options} {repository}".strip())

        @classmethod
        def prune(cls) -> None:
            pass
        
        @classmethod
        def pull(
                cls,
                name: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker image pull {options} {name}".strip())
        
        @classmethod
        def push(cls) -> None:
            pass
        
        @classmethod
        def rm(
                cls,
                image: str,
                options: str = ""
        ) -> None:
            
            os.system(command=f"docker image rm {options} {image}".strip())
        
        @classmethod
        def save(cls) -> None:
            pass
        
        @classmethod
        def tag(cls) -> None:
            pass


    class Manifest:
        pass
    
    
    class Network:
        pass
    
    
    class Node:
        pass
    
    
    class Plugin:
        pass
    
    
    class Scout:
        pass
    
    
    class Secret:
        pass
    
    
    class Service:
        pass
    
    
    class Stack:
        pass
    
    
    class Swarm:
        pass
    
    
    class System:
        pass
    
    
    class Trust:
        pass
    
    
    class Volume:
        pass




