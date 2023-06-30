from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder
import os


class UploadFiles():

    def __init__(self, site_url, account, password, target_url):
        self.site_url = site_url
        self.account = account
        self.password = password
        self.target_url = target_url

    # share point connection
    def get_sharepoint_connection(self):
        # Initialize the user credentials
        user_credentials = UserCredential(self.account, self.password)
        # create client context object
        try:
            ctx = ClientContext(self.site_url).with_credentials(user_credentials)
            print('success')
            return ctx
        except:
            print('error')
            return None


    def upload_large_file_to_sharepoint(self, ctx, local_path):
        size_chunk=1000000
        target_folder = ctx.web.get_folder_by_server_relative_url(self.target_url)
        
        def print_upload_progress(offset):
            file_size = os.path.getsize(local_path)
            print("Uploaded '{0}' bytes from '{1}'...[{2}%]".format(offset, file_size, round(offset / file_size * 100, 2)))
        
        with open(local_path, 'rb') as f:
            uploaded_file = target_folder.files.create_upload_session(f, size_chunk, print_upload_progress).execute_query()

        print('File {0} has been uploaded successfully'.format(uploaded_file.serverRelativeUrl))


   