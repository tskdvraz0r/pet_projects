import os

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
    def ps(cls, options: str = "") -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker ps", которая выводит информацию об активных docker-контейнерах на хосте.
            При использовании необязательного атрибута "all", будет показана информация о всех docker-контейнерах на хосте.

        Args:
            all (bool, optional): Необязательный аргумент, отвечающий за вывод ВСЕХ docker-контейнеров на хосте.
        """
        
        if options:
            os.system(command=f"docker ps {options}")
        else:
            os.system(command="docker ps")
    
    
    @classmethod
    def pull(cls, image: str) -> None:
        """
        Notes:
            Метод вызывает bash-комманду "docker pull <image>:<tag>"

        Args:
            image (str): Название образа. При необходимости можно указать тег;
        """
        
        os.system(command=f"docker pull {image}")
    
    
    @classmethod
    def rm(cls, name_or_id: str) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker rmi";
            Удаление Docker-образа;

        Args:
            name_or_id (str): Имя образа или id;
        """
        
        os.system(command=f"docker rm {name_or_id}")
    
    @classmethod
    def rmi(cls, image_or_id: str) -> None:
        """
        Notes:
            Метод вызывает Bash-команду "docker rmi";
            Удаление Docker-образа;

        Args:
            image_or_id (str): Имя образа (с тегом или без) или id.
        """
        
        os.system(command=f"docker rmi {image_or_id}")
        
         
    @classmethod
    def run(
            cls,
            image: str,
            options: str = "",
            platform: str = "linux/amd64",
    ) -> None:
        """
        Notes:
            Метод вызывает bash-команду "docker run", которая запускает контенейр из образа;

        Args:
            image (str): Название образа;
            options (str, optional): Дополнительные опции;
            platform (str, optional): Платформа. По умолчанию "linux/amd64";
        """
        
        if options:
            os.system(command=f"docker run {options} --platform={platform} {image}")
        else:
            os.system(command=f"docker run --platform={platform} {image}")

    @classmethod
    def stop(cls, name: str) -> None:
        
        os.system(command=f"docker stop {name}")
    
    @classmethod
    def start(cls, name: str) -> None:
        
        os.system(command=f"docker start {name}")

    
    @classmethod
    def commit(cls, name: str, new_name: str) -> None:
        
        os.system(command=f"docker commit {name} {new_name}")
