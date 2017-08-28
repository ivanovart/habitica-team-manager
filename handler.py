import utils
from habitica import HabiticaUser


def cron(event, context):
    users = utils.get_users()
    for user in users:
        print("User: %s" % user)
        habitica_user = HabiticaUser(user['user_id'], user['token'])
        print("Need cron? %s" % habitica_user.data['needsCron'])
        if habitica_user.data['needsCron']:
            habitica_user.make_request('POST', 'cron')
    return True
