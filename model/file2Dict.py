import json
class File2Dict():

    @staticmethod
    def read(filename):
        with open(filename,'r') as arq:
            content_file = arq.read()
            dictionary = json.loads(content_file)

        return dictionary

