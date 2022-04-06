from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    auth_key: str
    api_key: str
    
    port: int
    db_url: PostgresDsn
    
    # Note: This come's from one's environment variables. The USER environment variable must be set.
    user: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        fields = {
            'db_url': {
                'env': 'DATABASE_URL',
            }
        }
        secrets_dir = './secret_keys'


if __name__ == '__main__':
    print(Settings().dict())
