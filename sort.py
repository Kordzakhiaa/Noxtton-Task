from github import Github

ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)


class SortResult:
    """
    This class provides to sort repository name by ascending or descending order
    """

    def __init__(self, repo_name: str):
        self.repo_name = repo_name

    def check_repo_quantity(self):
        """This method checks if searched repositories found or not"""
        result = g.search_repositories(query=self.repo_name)
        total = result.totalCount

        if total == 0:
            return False
        return True

    def ascending(self):
        """Sorting repositories in ascending"""
        result_ascending = g.search_repositories(query=self.repo_name, sort='stars', order='asc')
        total = result_ascending.totalCount

        print(f'\nFound {total} repos which includes provided string\n')

        counter = 1

        for repo in result_ascending:
            if repo.name.lower() == self.repo_name.lower():
                print(f'{counter}. {repo.full_name}, {repo.stargazers_count} stars')
                counter += 1

        print(f'\nIgnored repos {result_ascending.totalCount - (counter - 1)}')

    def descending(self):
        """Sorting repositories in descending"""
        result_descending = g.search_repositories(query=self.repo_name, sort='stars', order='desc')
        total = result_descending.totalCount

        print(f'Found {total} repos which includes provided string\n')

        counter = 1

        for repo in result_descending:
            if repo.name.lower() == self.repo_name.lower():
                print(f'{counter}. {repo.full_name}, {repo.stargazers_count} stars')
                counter += 1

        print(f'\nIgnored repos {result_descending.totalCount - (counter - 1)}')
