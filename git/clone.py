import fire
import os
import shutil


class Clone(object):
    """Git clone related"""

    def clone(self, repo_path=None, path=None):
        if not repo_path:
            print('Please specify repo name: mimic user/repo')
            return

        # none 0 means success
        return not os.system(f'hub clone --depth=1 --branch=master {repo_path} {path}')

    def remove_git_dir(self, path=None):
        if not path:
            path = os.getcwd()

        shutil.rmtree(f'{path}/.git')

    def mimic(self, repo_path=None, path=None):
        """Clone from github without .git directory"""
        repo = repo_path.split('/')[-1]

        if not path:
            path = repo

        if not self.clone(repo_path, path):
            return

        self.remove_git_dir(path)
        print(f'cd {path}')


if __name__ == '__main__':
    fire.Fire(Clone)
