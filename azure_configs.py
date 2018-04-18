import azure.storage.file.fileservice

fs = azure.storage.file.fileservice.FileService(
    account_name='sensitivedata', 
    sas_token='?sv=2018-03-28&ss=f&srt=sco&sp=rl&se=2022-03-29T03:16:58Z&st=2019-03-28T19:16:58Z&spr=https&sig=SHtj6MONQN%2FHz%2BIDxx%2BWaB3NrgUYSbPD8b3cY3lhFIo%3D')

fs.get_file_to_path('secrets', None, 'config.txt', 'config')
