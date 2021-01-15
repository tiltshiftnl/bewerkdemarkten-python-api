from git.repo.base import Repo
from .settings import settings

class Git:
    def clone():
        try:
            print(f'Using existing repo in {settings.REPOSITORY_DIR}')
            Repo(settings.REPOSITORY_DIR)
        except:
            print('Repo does not exist')
            Repo.clone_from(settings.GIT_REPOSITORY, settings.REPOSITORY_DIR)
