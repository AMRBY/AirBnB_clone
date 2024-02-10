#!/usr/bin/env python3
""" unique engine storage
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
