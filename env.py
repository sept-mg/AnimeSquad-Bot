def load_env(file_path = ".env"):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    env_vars = {}
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=")
            env_vars[key] = value
    
    return env_vars

token = load_env()['TOKEN']
