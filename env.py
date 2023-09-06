class Env:
    def __init__(self):
        self.var = []
        self.file_path=".env"
        self.__load_env()

    def __load_env(self):
        self.var = self.__read()

    def set_env(self, updates):
        env_vars = self.__read()

        for key, value in updates.items():
            if key in env_vars:
                env_vars[key] = value
            else:
                print(f"La clé '{key}' n'existe pas dans le fichier .env. La variable n'a pas été modifiée.")

        with open(self.file_path, "w", encoding='utf-8') as file:
            for k, v in env_vars.items():
                file.write(f"{k}={v}\n")

        self.var = env_vars
    
    def __read(self):
        with open(self.file_path, "r", encoding='utf-8') as file:
            lines = file.readlines()

        env_vars = {}
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                env_vars[key] = value
        return env_vars