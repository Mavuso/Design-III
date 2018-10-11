
from datetime import datetime
from tinydb_serialization import Serializer



class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime 

    def encode(self, obj):
        return obj.strftime("%Y-%m-%d %H:%M")

    def decode(self, s):
        return datetime.strptime(s, "%Y-%m-%d %H:%M")


