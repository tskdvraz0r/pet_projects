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
            options: str
    ) -> None:
        
        os.system(command=f"docker --version {options}".strip())
    
    
    class Container:
        
        @classmethod
        def attach(cls) -> None:
            pass
        
        @classmethod
        def commit(
                cls,
                options: str,
                container: str,
                repository: str
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
                options: str
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
                options: str,
                container: str,
        ) -> None:
            
            os.system(command=f"docker container rm {options} {container}".strip())
        
        @classmethod
        def run(
                cls,
                
                options: str,
                image: str,
                command: str,
                arg: str,
                platform: str = "linux/amd64"
        ) -> None:
            
            os.system(command=f"docker container run {options} --platform={platform} {image} {command} {arg}".strip())
        
        @classmethod
        def start(
                cls,
                options: str,
                container: str
        ) -> None:
            
            os.system(command=f"docker container start {options} {container}".strip())
        
        @classmethod
        def stats(cls) -> None:
            pass
        
        @classmethod
        def stop(
                cls,
                options: str,
                container: str
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
                options: str,
                repository: str =""
        ) -> None:
            
            os.system(command=f"docker image ls {options} {repository}".strip())

        @classmethod
        def prune(cls) -> None:
            pass
        
        @classmethod
        def pull(
                cls,
                options: str,
                name: str
        ) -> None:
            
            os.system(command=f"docker image pull {options} {name}".strip())
        
        @classmethod
        def push(cls) -> None:
            pass
        
        @classmethod
        def rm(cls) -> None:
            pass
        
        @classmethod
        def save(cls) -> None:
            pass
        
        @classmethod
        def tag(cls) -> None:
            pass