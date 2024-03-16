import os
from subprocess import Popen

class Docker:
    
    @classmethod
    def v(cls) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker -v", которая возвращает версию установленного docker;
        """
        
        os.system(command="docker -v")
    
    @classmethod
    def images(cls) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker images", которая выводит список docker-образов на хосте;
        """
        
        os.system(command="docker images")
    
    @classmethod
    def ps(cls, all: bool = False) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker ps", которая выводит информацию об активных docker-контейнерах на хосте.
            При использовании необязательного атрибута "all", будет показана информация о всех docker-контейнерах на хосте.

        Args:
            all (bool, optional): Необязательный аргумент, отвечающий за вывод ВСЕХ docker-контейнеров на хосте.
        """
        
        if all:
            os.system(command="docker ps -a")
        else:
            os.system(command="docker ps")
    
    @classmethod
    def pull(cls, image: str, tag: str = "") -> None:
        
        if tag:
            os.system(command=f"docker pull {image}:{tag}")
        else:
            os.system(command=f"docker pull {image}")
    
    @classmethod
    def rm(
            cls,
            name_or_id: str
    ) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker rmi";
            Удаление Docker-образа;

        Args:
            image (str): Имя образа или id.
            tag (str, optional): Тег образа. Опционально, но только в том случае, если в "image" не был указан id!
        """
        
        os.system(command=f"docker rmi {name_or_id}")
    
    @classmethod
    def rmi(
            cls,
            image: str,
            tag: str = ""
    ) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker rmi";
            Удаление Docker-образа;

        Args:
            image (str): Имя образа или id.
            tag (str, optional): Тег образа. Опционально, но только в том случае, если в "image" не был указан id!
        """
        
        if tag:
            os.system(command=f"docker rmi {image}:{tag}")
        else:
            os.system(command=f"docker rmi {image}")
    
    @classmethod
    def run(
            cls,
            image: str,
            tag: str = "",
            rm: bool = False,
            it: bool = False,
            platform: str = "linux/amd64",
    ) -> None:
        """
        Notes:
            Метод вызывает bash-команду "docker run", которая запускает контенейр из образа;

        Args:
            image (str): Название образа;
            tag (str, optional): Тег образа;
            rm (bool, optional): Требуется ли удалить контейнер после завершения работы;
            platform (str, optional): Платформа. По умолчанию "linux/amd64";
        """
        
        if rm:
            Popen(
                [
                    "docker",
                    "run",
                    "--rm" if rm else "",
                    f"--platform={platform}",
                    f"{image}:{tag}" if tag else f"{image}",
                ]
            )
        else:
            Popen(
                [
                    "docker",
                    "run",
                    f"--platform={platform}",
                    f"{image}:{tag}" if tag else f"{image}",
                ]
            )

    @classmethod
    def stop(cls, name: str) -> None:
        
        os.system(command=f"docker stop {name}")
    
    @classmethod
    def start(cls, name: str) -> None:
        
        os.system(command=f"docker start {name}")
