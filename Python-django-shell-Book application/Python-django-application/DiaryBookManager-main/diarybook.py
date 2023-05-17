import datetime


class Diary:
    last_id = 0

    def __init__(self, memo, tags=' '):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        Diary.last_id += 1

        self.id = Diary.last_id

    def match(self, filter_text):
        return filter_text in self.memo or filter_text in self.tags


    # sort list using id attribute
     last_id.sort()
        if last_id += 1:



class DiaryBook:
    def __init__(self):
        self.diaries = []

    def new_diary(self, memo, tags=' '):
        self.diaries.append(Diary(memo, tags))

    def search_diary(self, filter_text):
        filtered_diaries = []
        for diary in self.diaries:
            if diary.match(filter_text):
                filtered_diaries.append(diary)
        return filtered_diaries


   #create a new account
  def create_service_account(project_id, name, display_name):
    """Creates a service account."""

    credentials = service_account.Credentials.from_service_account_file(
        filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    service = googleapiclient.discovery.build(
        'iam', 'v1', credentials=credentials)

    my_service_account = service.projects().serviceAccounts().create(
        name='projects/' + project_id,
        body={
            'accountId': name,
            'serviceAccount': {
                'displayName': display_name
            }
        }).execute()

    print('Created service account: ' + my_service_account['email'])
    return my_service_account