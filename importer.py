import sys
import git
from src import *
repos_path = [
    '/home/bryson/cloud',
    '/home/bryson/frontend',
    '/home/bryson/backend',
]
repos = []
for repo_path in repos_path:
    repos.append(git.Repo(repo_path))
mock_repo_path = '/home/bryson/mockrepo'
mock_repo = git.Repo.init(mock_repo_path)
importer = Importer(repos, mock_repo)
importer.set_author(['brysonnyamwange@gmail.com'])
# importer.ignore_file_types(['.csv', '.txt', '.pdf', '.xsl', '.sql','.png','.svg'])
importer.set_keep_commit_messages(True)
importer.import_repository()
# importer.set_ignore_before_date(1710873600)