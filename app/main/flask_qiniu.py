try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin
import qiniu as QiniuClass


class Qiniu(object):
    def __init__(self):
        self._access_key = ''
        self._secret_key = ''
        self._bucket_name = ''
        domain = ''
        self._base_url = 'http://' + domain

    def save(self, data, filename=None):
        auth = QiniuClass.Auth(self._access_key, self._secret_key)
        token = auth.upload_token(self._bucket_name)
        return QiniuClass.put_data(token, filename, data)

    def url(self, filename):
        return urljoin(self._base_url, filename)

    def private_url(self, filename):
        auth = QiniuClass.Auth(self._access_key, self._secret_key)
        return auth.private_download_url(urljoin(self._base_url, filename), expires=3600)
