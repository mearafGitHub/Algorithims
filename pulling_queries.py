
def pull_(repository, query, s):
    # s is starting point in 1 based array
    repository.sort()
    ith_query = []
    for i in range(s-1, len(query)):
        for repo in repository:

            if repo.lower().startswith(query[0: i+1].lower()):
                if len(ith_query) < 3:
                    ith_query.append(repo.lower())
        ith_query.sort()
    return ith_query

data = ['Mouse','Mobile', 'mouse_Pad', 'MonItor', 'Gobgle',
        'Goodle', 'Moneypot', 'Goose','Google', 'Amazon', 'Apple']
d = ['abc', 'abccc', 'abccccdd']

q = 'mobile'
print(pull_(data, q, 2))
print(pull_(data, 'go', 2))
