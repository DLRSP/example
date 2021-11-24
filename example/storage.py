from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootCachedS3Boto3Storage(S3Boto3Storage):
    """
    S3 storage backend that saves the files locally, too.
    """

    def __init__(self, *args, **kwargs):
        super(StaticRootCachedS3Boto3Storage, self).__init__(*args, **kwargs)
        self.location = "static"
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage"
        )()

    def save(self, name, content, max_length=None):
        self.local_storage._save(name, content)
        super(StaticRootCachedS3Boto3Storage, self).save(
            name, self.local_storage._open(name)
        )
        return name


class MediaRootCachedS3Boto3Storage(S3Boto3Storage):
    """
    S3 storage backend that saves the files locally, too.
    """

    def __init__(self, *args, **kwargs):
        super(MediaRootCachedS3Boto3Storage, self).__init__(*args, **kwargs)
        self.location = "media"
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage"
        )()

    def save(self, name, content, max_length=None):
        self.local_storage._save(name, content)
        super(MediaRootCachedS3Boto3Storage, self).save(
            name, self.local_storage._open(name)
        )
        return name


class PublicMediaS3Boto3Storage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False


class PrivateMediaS3Boto3Storage(S3Boto3Storage):
    location = "private"
    default_acl = "private"
    file_overwrite = False
    custom_domain = False
