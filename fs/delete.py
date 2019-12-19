import fire
import os
import shutil


class Delete(object):
    """Remove file and directorys"""

    def rmm(self, *path):
        """
        This command is currently MACOS ONLY,
        it will remove files by moving them to system Trash directory
        """
        if not len(path):
            print('Empty path, aborting')
            return

        trash_dir = '~/.Trash'
        str_path = ' '.join(path)
        os.system(f'mv {str_path} {trash_dir}')


if __name__ == '__main__':
    fire.Fire(Delete)
