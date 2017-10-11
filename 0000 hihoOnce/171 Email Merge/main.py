from __future__ import print_function
from collections import defaultdict, deque

# load data
N = int(raw_input())

email_users = defaultdict(lambda: [])
user_emails = {}
user_id = {}
for i in range(N):
    line = raw_input()
    user, n_email, emails = line.split(None, 2)
    n_email = int(n_email)
    emails = emails.split()

    user_id[user] = i
    user_emails[user] = emails
    for email in emails:
        email_users[email].append(user)

# BFS
checked_emails = set()
result = []
for email, users in email_users.iteritems():
    if email not in checked_emails:
        checked_emails.add(email)
        checked_users = set()
        todo_users = deque(users)

        while todo_users:
            todo_user = todo_users.popleft()
            if todo_user not in checked_users:
                checked_users.add(todo_user)
                for todo_email in user_emails[todo_user]:
                    if todo_email not in checked_emails:
                        checked_emails.add(todo_email)
                        todo_users.extend(email_users[todo_email])

        if checked_users:
            user_group = list(checked_users)
            user_group.sort(key=lambda u: user_id[u])
            result.append(user_group)

# output
result.sort(key=lambda ug: user_id[ug[0]])

for user_group in result:
    print(' '.join(user_group))
