from git.repo.base import Repo
from .settings import settings

class Git:
    def clone():
        try:
            print('Using existing repo in /tmp/bewerkdemarkten-repo')
            Repo('/tmp/bewerkdemarkten-repo')
        except expression as identifier:
            print('Repo does not exist')
            Repo.clone_from(settings.GIT_REPOSITORY, '/tmp/bewerkdemarkten-repo')
