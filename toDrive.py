from PyDrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

from pydrive.drive import GoogleDrive